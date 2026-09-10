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

const DESTINATAIRE = process.env.CONTACT_TO || 'contact@amelie-invest.com';
const EXPEDITEUR = process.env.CONTACT_FROM
  || 'Amélie & Partners <site@amelie-invest.com>';

const QUALITES = ['Particulier', 'Professionnel', 'Société (SCI, holding)', 'Autre'];
const PROFILS = ['Premier projet immobilier', 'Patrimoine déjà constitué',
  'Arbitrage ou refinancement', 'Autre'];

/** Caractères de contrôle : ils n'ont rien à faire dans un courrier. */
const CONTROLES = /[\u0000-\u0008\u000B\u000C\u000E-\u001F\u007F]/g;

/** Le corps arrive en formulaire encodé ou en JSON selon l'appelant. */
function lireCorps(req) {
  const brut = req.body;
  if (!brut) return {};
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

function repondre(req, res, code, message, ok = false) {
  if (veutJson(req)) {
    res.status(code).json({ ok, message });
    return;
  }
  // Sans JavaScript : retour sur la page, résultat en paramètre.
  res.setHeader('Location', `/contact.html?envoi=${ok ? 'ok' : 'erreur'}#formulaire`);
  res.status(303).end();
}

module.exports = async function handler(req, res) {
  if (req.method !== 'POST') {
    return repondre(req, res, 405, 'Méthode non autorisée.');
  }

  const corps = lireCorps(req);

  // Piège à robots : ce champ est masqué et doit rester vide. Aucun service
  // extérieur n'est appelé pour cette vérification. On répond « reçu » sans
  // rien envoyer : un robot ne doit pas apprendre qu'il a été repéré.
  if (champ(corps, 'site_web', 200) !== '') {
    return repondre(req, res, 200, 'Message reçu.', true);
  }

  // Un formulaire rempli en moins de trois secondes ne l'a pas été par une
  // personne. Sans JavaScript le champ reste vide et le contrôle est ignoré.
  const pose = parseInt(champ(corps, 'pose', 20), 10);
  if (Number.isFinite(pose) && pose > 0 && (Date.now() / 1000 - pose) < 3) {
    return repondre(req, res, 200, 'Message reçu.', true);
  }

  const prenom = champ(corps, 'prenom', 80);
  const nom = champ(corps, 'nom', 80);
  const courriel = champ(corps, 'courriel', 180);
  const indicatif = champ(corps, 'indicatif', 8);
  const telephone = champ(corps, 'telephone', 40);
  let qualite = champ(corps, 'qualite', 60);
  let profil = champ(corps, 'profil', 60);
  const message = champ(corps, 'message', 5000);
  const consent = champ(corps, 'consentement', 20) !== '';

  const manques = [];
  if (!prenom) manques.push('le prénom');
  if (!nom) manques.push('le nom');
  if (!/^[^@\s]+@[^@\s]+\.[A-Za-z]{2,}$/.test(courriel)) {
    manques.push('une adresse e-mail valide');
  }
  if (!qualite) manques.push('à quel titre vous écrivez');
  if (!profil) manques.push('où vous en êtes');
  if (message.length < 20) manques.push('quelques lignes sur votre situation');
  if (!consent) manques.push('votre accord pour le traitement des informations');

  if (manques.length) {
    return repondre(req, res, 422, `Il manque ${manques.join(', ')}.`);
  }

  // Les listes ne prennent que les valeurs proposées : on ne fait pas
  // confiance à ce qui arrive.
  if (!QUALITES.includes(qualite)) qualite = 'Autre';
  if (!PROFILS.includes(profil)) profil = 'Autre';

  const tel = telephone ? `${indicatif} ${telephone}`.trim() : 'non communiqué';
  const texte = [
    `Prénom : ${prenom}`,
    `Nom : ${nom}`,
    `Adresse e-mail : ${courriel}`,
    `Téléphone : ${tel}`,
    `Vous êtes : ${qualite}`,
    `Où j’en suis : ${profil}`,
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
      + `Écrivez directement à ${DESTINATAIRE}.`);
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
        to: [DESTINATAIRE],
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
        + `ou écrivez directement à ${DESTINATAIRE}.`);
    }
  } catch (err) {
    console.error('[contact] appel à Resend impossible :', err);
    return repondre(req, res, 502, 'L’envoi a échoué. Réessayez dans un moment, '
      + `ou écrivez directement à ${DESTINATAIRE}.`);
  }

  return repondre(req, res, 200, 'Message envoyé. Nous répondons sous un jour ouvré.', true);
};
