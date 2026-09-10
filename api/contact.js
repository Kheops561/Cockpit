/**
 * Réception du formulaire de contact · fonction serveur Vercel.
 *
 * Le site reste un ensemble de fichiers statiques : cette fonction est le
 * seul morceau de code exécuté côté serveur. Elle reçoit le formulaire et
 * fait partir le message par l'API Resend.
 *
 * Conséquence importante : les pages n'appellent aucun domaine tiers. Le
 * navigateur ne parle qu'au site lui-même, sur `/api/contact`. C'est cette
 * fonction, et elle seule, qui contacte Resend. La clé d'API vit dans les
 * variables d'environnement du projet Vercel et ne figure pas dans le dépôt.
 *
 * Installation : voir INSTALLATION-FORMULAIRE.md.
 */

/**
 * Les destinataires. `CONTACT_TO` et `CONTACT_CC` acceptent plusieurs
 * adresses séparées par une virgule ou un point-virgule :
 *
 *   CONTACT_TO = contact@amelie-invest.com, amelie@amelie-invest.com
 *   CONTACT_CC = assistante@amelie-invest.com
 *
 * Les adresses en copie voient le message et se voient entre elles ; c'est
 * l'usage attendu ici, entre collaborateurs. Le visiteur, lui, ne voit
 * jamais cette liste : il ne reçoit pas ce message, il l'envoie.
 */
const ADRESSE = /^[^@\s,;]+@[^@\s,;]+\.[A-Za-z]{2,}$/;

/**
 * On colle rarement une liste d'adresses toute propre. Cette lecture accepte
 * donc ce qui sort d'un carnet d'adresses ou d'un copier-coller :
 *
 *   contact@x.fr, amelie@x.fr          séparateurs virgule, point-virgule
 *   AMELIE DUONG <anhthu@gmail.com>    la forme « Nom <adresse> »
 *   Eric Boileau eric@joytalents.com   un nom collé devant, sans chevrons
 *   une adresse par ligne              retours à la ligne
 *
 * Seule l'adresse est retenue, jamais le nom : une adresse nue ne peut rien
 * injecter dans les en-têtes du courrier, et le destinataire voit de toute
 * façon le nom que son propre carnet lui donne.
 */
function adresses(brut, defaut = '') {
  return String(brut || defaut)
    .split(/[,;\n\r]+/)
    .map((morceau) => {
      const t = morceau.trim();
      if (!t) return '';
      // « Nom <adresse> » : on ne garde que ce qui est entre chevrons.
      const chevrons = t.match(/<([^<>]+)>/);
      if (chevrons) return chevrons[1].trim();
      // « Nom adresse » sans chevrons : l'adresse est le dernier mot.
      if (/\s/.test(t)) return t.split(/\s+/).pop();
      return t;
    })
    .filter((a) => ADRESSE.test(a))
    .slice(0, 10);
}

const DESTINATAIRES = adresses(process.env.CONTACT_TO, 'contact@amelie-invest.com');
const COPIES = adresses(process.env.CONTACT_CC);
// Une seule adresse suffit à écrire « écrivez-nous directement à… ».
const DESTINATAIRE = DESTINATAIRES[0] || 'contact@amelie-invest.com';

const EXPEDITEUR = process.env.CONTACT_FROM
  || 'Amélie & Partners <site@amelie-invest.com>';

const QUALITES = ['Particulier', 'Professionnel', 'Société (SCI, holding)', 'Autre'];

// Les douze profils d'investisseur, plus la sortie honnête pour qui ne se
// reconnaît dans aucun. Cette liste doit rester le miroir exact de celle du
// formulaire : ce qui arrive d'ailleurs est ramené à « Je ne sais pas
// encore » plutôt que recopié tel quel dans le courrier.
const PROFILS = [
  'Primo-investisseur · se constituer un patrimoine',
  'Investisseur locatif · générer des revenus réguliers',
  'Rentier · vivre des revenus immobiliers',
  'Investisseur patrimonial · préserver et développer son capital',
  'Chasseur de rendement · maximiser la rentabilité',
  'Marchand de biens · acheter, rénover, revendre',
  'Investisseur fiscal · réduire sa fiscalité',
  'Professionnel ou entrepreneur · développer un portefeuille',
  'Investisseur familial · transmettre un patrimoine',
  'Investisseur opportuniste · saisir une occasion',
  'Investisseur en SCPI · investir sans gérer un bien',
  'Investisseur institutionnel · placer des capitaux importants',
  'Je ne sais pas encore',
];

const ECHEANCES = [
  'Dans les trois mois',
  'Dans trois à six mois',
  'Dans six à douze mois',
  'Au-delà d’un an',
  'Pas de date fixée',
];

/** Caractères de contrôle : ils n'ont rien à faire dans un courrier. */
const CONTROLES = /[\u0000-\u0008\u000B\u000C\u000E-\u001F\u007F]/g;

/** Le corps arrive en formulaire encodé ou en JSON selon l'appelant. */
function lireCorps(req) {
  let brut = req.body;
  if (!brut) return {};
  // Selon la configuration, l'hébergeur remet parfois le corps sans l'avoir
  // décodé : un tampon d'octets plutôt qu'une chaîne. On le ramène au texte
  // avant d'aller plus loin.
  if (Buffer.isBuffer(brut)) brut = brut.toString('utf8');
  if (typeof brut === 'object') return brut;
  if (typeof brut === 'string') {
    const type = String(req.headers['content-type'] || '');
    if (type.includes('application/json')) {
      try {
        return JSON.parse(brut);
      } catch (e) {
        return {};
      }
    }
    return Object.fromEntries(new URLSearchParams(brut));
  }
  return {};
}

function veutJson(req) {
  const accept = String(req.headers.accept || '');
  return accept.includes('application/json')
    || String(req.headers['x-requested-with'] || '') === 'fetch';
}

/** Nettoie une valeur : retours normalisés, contrôles retirés, longueur bornée. */
function champ(corps, nom, max = 500) {
  const v = corps[nom];
  if (typeof v !== 'string') return '';
  return v.replace(/\r\n|\r/g, '\n').replace(CONTROLES, '').trim().slice(0, max);
}

/**
 * Sans JavaScript, la fonction renvoie le visiteur sur la page d'où il
 * vient. Cette page est portée par un champ caché du formulaire, mais elle
 * n'est jamais reprise telle quelle : seules les pages de cette liste sont
 * acceptées. Sans ce garde-fou, n'importe qui pourrait faire rediriger le
 * formulaire vers l'adresse de son choix.
 */
const PAGES_RETOUR = ['formulaire.html', 'contact.html'];
const PAGE_DEFAUT = 'formulaire.html';

function pageRetour(corps) {
  const v = champ(corps, 'retour', 40);
  return PAGES_RETOUR.includes(v) ? v : PAGE_DEFAUT;
}

function repondre(req, res, code, message, ok = false, page = PAGE_DEFAUT) {
  if (veutJson(req)) {
    res.status(code).json({ ok, message });
    return;
  }
  // Sans JavaScript : retour sur la page, résultat en paramètre.
  res.setHeader('Location', `/${page}?envoi=${ok ? 'ok' : 'erreur'}#formulaire`);
  res.status(303).end();
}

module.exports = async function handler(req, res) {
  // Un appel en GET sert de controle d'installation : ouvrir
  // `/api/contact` dans un navigateur dit si les variables sont en place,
  // sans rien reveler de leur contenu. C'est la reponse a « le formulaire ne
  // marche pas » : soit la fonction n'est pas deployee et la page est
  // introuvable, soit elle repond et l'on voit tout de suite ce qui manque.
  if (req.method === 'GET') {
    res.setHeader('Cache-Control', 'no-store');
    return res.status(200).json({
      ok: true,
      fonction: 'contact',
      cle: Boolean(process.env.RESEND_API_KEY),
      expediteur: Boolean(process.env.CONTACT_FROM),
      destinataires: DESTINATAIRES.length,
      copies: COPIES.length,
    });
  }

  if (req.method !== 'POST') {
    return repondre(req, res, 405, 'Méthode non autorisée.');
  }

  const corps = lireCorps(req);
  const page = pageRetour(corps);

  // Piège à robots : ce champ est masqué et doit rester vide. Aucun service
  // extérieur n'est appelé pour cette vérification. On répond « reçu » sans
  // rien envoyer : un robot ne doit pas apprendre qu'il a été repéré.
  if (champ(corps, 'site_web', 200) !== '') {
    return repondre(req, res, 200, 'Message reçu.', true, page);
  }

  // Un formulaire rempli en moins de trois secondes ne l'a pas été par une
  // personne. Sans JavaScript le champ reste vide et le contrôle est ignoré.
  const pose = parseInt(champ(corps, 'pose', 20), 10);
  if (Number.isFinite(pose) && pose > 0 && (Date.now() / 1000 - pose) < 3) {
    return repondre(req, res, 200, 'Message reçu.', true, page);
  }

  const prenom = champ(corps, 'prenom', 80);
  const nom = champ(corps, 'nom', 80);
  const courriel = champ(corps, 'courriel', 180);
  const indicatif = champ(corps, 'indicatif', 8);
  const telephone = champ(corps, 'telephone', 40);
  let qualite = champ(corps, 'qualite', 60);
  let profil = champ(corps, 'profil', 80);
  let echeance = champ(corps, 'echeance', 40);
  const message = champ(corps, 'message', 5000);
  const consent = champ(corps, 'consentement', 20) !== '';

  const manques = [];
  if (!prenom) manques.push('le prénom');
  if (!nom) manques.push('le nom');
  if (!/^[^@\s]+@[^@\s]+\.[A-Za-z]{2,}$/.test(courriel)) {
    manques.push('une adresse e-mail valide');
  }
  if (!qualite) manques.push('à quel titre vous écrivez');
  if (!profil) manques.push('le profil dont vous vous sentez le plus proche');
  if (!echeance) manques.push('votre échéance');
  if (message.length < 20) manques.push('quelques lignes sur votre situation');
  if (!consent) manques.push('votre accord pour le traitement des informations');

  if (manques.length) {
    return repondre(req, res, 422, `Il manque ${manques.join(', ')}.`, false, page);
  }

  // Les listes ne prennent que les valeurs proposées : on ne fait pas
  // confiance à ce qui arrive.
  if (!QUALITES.includes(qualite)) qualite = 'Autre';
  if (!PROFILS.includes(profil)) profil = 'Je ne sais pas encore';
  if (!ECHEANCES.includes(echeance)) echeance = 'Pas de date fixée';

  const tel = telephone ? `${indicatif} ${telephone}`.trim() : 'non communiqué';
  const texte = [
    `Prénom : ${prenom}`,
    `Nom : ${nom}`,
    `Adresse e-mail : ${courriel}`,
    `Téléphone : ${tel}`,
    `Vous êtes : ${qualite}`,
    `Profil d’investisseur : ${profil}`,
    `Échéance : ${echeance}`,
    '',
    'Message :',
    message,
    '',
    '--',
    'Envoyé depuis le formulaire de contact d’amelie-invest.com.',
  ].join('\n');

  const cle = process.env.RESEND_API_KEY;
  if (!cle) {
    console.error('[contact] RESEND_API_KEY absente des variables du projet.');
    return repondre(req, res, 500, 'Le formulaire n’est pas encore configuré. '
      + `Écrivez directement à ${DESTINATAIRE}.`, false, page);
  }

  try {
    const r = await fetch('https://api.resend.com/emails', {
      method: 'POST',
      headers: {
        Authorization: `Bearer ${cle}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        from: EXPEDITEUR,
        to: DESTINATAIRES.length ? DESTINATAIRES : [DESTINATAIRE],
        ...(COPIES.length ? { cc: COPIES } : {}),
        reply_to: courriel,
        subject: `Formulaire de contact · ${prenom} ${nom}`,
        text: texte,
      }),
    });

    if (!r.ok) {
      // Le détail part dans le journal Vercel, jamais vers le visiteur : il
      // ne doit rien apprendre de la configuration.
      console.error('[contact] Resend a répondu', r.status, await r.text());
      return repondre(req, res, 502, 'L’envoi a échoué. Réessayez dans un moment, '
        + `ou écrivez directement à ${DESTINATAIRE}.`, false, page);
    }
  } catch (err) {
    console.error('[contact] appel à Resend impossible :', err);
    return repondre(req, res, 502, 'L’envoi a échoué. Réessayez dans un moment, '
      + `ou écrivez directement à ${DESTINATAIRE}.`, false, page);
  }

  return repondre(req, res, 200, 'Message envoyé. Nous répondons sous un jour ouvré.', true, page);
};
