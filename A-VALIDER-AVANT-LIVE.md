# À valider avant la mise en ligne publique

Le site est techniquement exploitable. Les éléments ci-dessous doivent être
confirmés par Amélie avant de considérer la publication comme définitive.

## Décidé

- [x] Domaine : **amelie-invest.com** (sans `www`). Il est déjà inscrit dans
      les balises canoniques, `sitemap.xml`, `robots.txt` et les données
      structurées. Si la décision change, relancer
      `python3 outils/donnees-structurees.py` après avoir modifié le domaine
      dans ce script, puis reprendre `sitemap.xml`, `robots.txt` et les
      `<link rel="canonical">` des douze pages.

## Identité et conversion · priorité haute

- [ ] Adresse e-mail publique : `contact@amelie-invest.com` : boîte créée et
      relevée ?
- [x] Lien Calendly : `https://calendly.com/amelie-partners`. Le compte est
      actif et l’événement « Appel de cadrage, 30 minutes » est publié. Sa
      politique de confidentialité est citée sur la page « Données
      personnelles » et dans les mentions légales.
- [ ] Durée du premier échange : 30 minutes.
- [x] Prix du Diagnostic Stratégique : **432 € TTC**, validé par Amélie le
      10 septembre 2026. Repris sur toutes les pages et dans les données
      structurées, qui déclarent désormais la TVA comprise.
- [ ] Zone d’intervention : Paris pour la recherche ; France au cas par cas
      pour la stratégie et l’arbitrage.

## Preuves sociales · priorité haute

- [ ] Autorisation de publication pour chacun des huit témoignages.
- [ ] Validation des prénoms, initiales, âges, métiers, entreprises, villes et
      résultats cités.
- [ ] Validation des chiffres : `> 35`, `> 25 M€`, `> 75`, `> 80`.
- [ ] Conservation de la phrase : `Chaque témoignage reflète une expérience
      individuelle ; les résultats varient selon les situations.`

Le taux de 98 % n’est affiché nulle part, en attente d’une définition, d’une
base et d’une période auditées.

## Identité · à trancher

- [ ] **Signature du logo.** Le bloc fourni porte `PARTENAIRE STRATÉGIQUE DES
      INVESTISSEURS IMMOBILIERS`. Les instructions de marque retiennent
      `Investir avec méthode · Décider avec clarté`, qui est la version
      affichée sur le site. Confirmer laquelle fait foi.
- [ ] **Accent sur le nom.** Le logo écrit `AMELIE & PARTNERS`, le site
      `AMÉLIE & PARTNERS`. Confirmer.
- [ ] Fournir une version vectorielle du logo (`.svg`) si elle existe : plus
      nette sur les écrans à forte densité, et plus légère.

## Formulaire de contact

Le formulaire **prépare un message dans la messagerie du visiteur**, adressé à
la boîte du domaine chez OVH. Il n’envoie rien lui-même, et aucune donnée
saisie ne transite par le site.

C’est le choix retenu tant qu’il n’y a pas d’hébergement qui exécute du code.

**Situation constatée le 10 septembre 2026.** `amelie-invest.com` a son
domaine et ses boîtes aux lettres chez OVH. Le site en ligne, lui, est
construit avec **Showit** et servi depuis une machine Amazon EC2
(75.101.134.27, résolution inverse `ec2-75-101-134-27.compute-1.amazonaws.com`).

## Où publier le site de ce dépôt

**Le site construit ici ne peut pas être publié sur Showit.** Showit est un
éditeur fermé : on y compose des pages dans son interface, on n’y dépose pas
des fichiers HTML, CSS et JavaScript quelconques. Les treize pages doivent
donc être servies ailleurs. À vérifier auprès de Showit si vous y tenez, mais
c’est la règle générale de ce type d’outil.

- [ ] **Décider où vit le site de ce dépôt.** Un hébergement OVH mutualisé
      suffit largement, et rend du même coup possible l’envoi direct du
      formulaire. C’est la voie la plus cohérente : domaine, boîtes et site
      au même endroit, mentions légales exactes.
- [ ] **Décider du sort du site Showit actuel.** Les deux ne peuvent pas
      répondre à la même adresse. Soit le nouveau site le remplace, soit il
      faut choisir un sous-domaine, le temps de la transition.
- [ ] **Les mentions légales déclarent Vercel comme hébergeur.** Ce n’est
      exact que si le site est effectivement servi par Vercel. Tant que
      Showit sert la page, l’hébergeur à déclarer est Showit. Un paragraphe
      d’avertissement figure sur la page ; il devra être retiré une fois
      la bascule faite — voir `CONFIGURATION-DNS.md`.

- [x] **Le formulaire de contact est en service.** Il poste sur
      `api/contact.js`, la fonction serveur du projet Vercel, qui fait
      partir le message par Resend. Les trois entrées DNS sont posées chez
      OVH et vérifiées ; les variables sont en place sur Vercel.

- [x] **La région de traitement Resend est arrêtée** : Irlande
      (`eu-west-1`), dans l’Union européenne. La page « Données
      personnelles » l’écrit.

- [ ] **Resend est éditée par une société de droit américain.** Faire
      confirmer par un professionnel du droit si son accord de traitement
      des données suffit, ou s’il faut citer en plus un mécanisme de
      transfert. La mention est en attente sur la page « Données
      personnelles ».

## Langues · nouveau

Le site existe désormais en **français, anglais et vietnamien**. Onze pages
ont été traduites dans chaque langue ; les trois pages légales restent en
français, et les pages traduites y renvoient en le disant.

- [ ] **Faire relire la version anglaise.** Elle a été écrite avec soin,
      mais c’est la voix du cabinet dans une autre langue : Amélie est la
      seule à pouvoir dire si elle s’y reconnaît. Les pages sont dans
      `en/`, et se lisent depuis le site par le drapeau, en haut à droite.
- [ ] **Les témoignages restent en français** sur la version anglaise, ce
      qui était la décision retenue : ce sont les mots de personnes
      réelles. Confirmer que cela convient, ou décider d’une traduction
      accompagnée de la mention qu’il s’agit d’une traduction.
- [ ] **Faire relire la version vietnamienne**, au même titre que
      l’anglaise, et plus encore : Amélie est vietnamienne, elle jugera
      mieux que quiconque si le ton est juste. Le vouvoiement retenu est
      « quý vị », qui s’adresse au lecteur avec respect sans lui donner
      d’âge ni de rang.
- [ ] **La carte postale de « À propos » change de police en vietnamien.**
      Caveat, l’écriture manuscrite, n’existe pas dans cette langue : les
      lettres à ton n’y sont pas dessinées. Sur les pages vietnamiennes, les
      deux blocs manuscrits prennent donc le serif du site en italique. À
      valider, ou à remplacer par une autre écriture manuscrite couvrant le
      vietnamien — ce serait une quatrième police, donc une décision de
      design.
- [ ] **La carte postale part maintenant de Hanoï.** Le titre dit « De
      Hanoï… à Paris. » et le trajet va de la gauche vers la droite. La
      biographie, elle, continue de dire « Née au Viêt Nam », sans nommer de
      ville : confirmer que Hanoï peut être nommée comme ville de départ.
- [ ] **La fiche PDF « Les 3 effets » est en français.** La page anglaise
      le dit au moment de proposer le téléchargement. Décider si une
      version anglaise du PDF est souhaitée.
- [ ] **Les données structurées (JSON-LD) ne sont posées que sur les pages
      françaises.** Celles qui existent décrivent le cabinet en français ;
      les recopier telles quelles sur `/en/` dirait aux moteurs que la page
      anglaise est française. À reprendre si le référencement anglais
      devient un sujet.
- [ ] **Le prix reste français** — `432 €`, « incl. French VAT » — parce
      que la prestation est vendue et facturée en France. Confirmer que
      c’est bien la règle voulue si des clients hors zone euro se
      présentent.

## Tarifs et durées

- [x] **Le prix du Diagnostic Stratégique** est arrêté à **432 € TTC**
      (Amélie, 10 septembre 2026). Le site affichait `450 € HT` ; tout est
      aligné, mention `TTC` comprise.
- [x] **La durée du Diagnostic Stratégique est arrêtée à une heure**
      (Amélie, 10 septembre 2026). Le site annonçait `75 minutes` ; il annonce
      désormais `1 heure` sur `diagnostic.html`, `accompagnements.html`,
      `contact.html`, l’accueil et dans les descriptions de référencement.
      C’est aussi ce que dit Calendly.
- [ ] Vérifier que `432 € TTC` correspond bien à `360 € HT` dans votre
      comptabilité, et si le montant HT doit figurer à côté.
- [ ] **Relire les conditions générales de vente (`cgv.html`) avec un
      professionnel du droit.** Le modèle fourni parlait du « mentor » ; le
      texte est repris au nom d’Amélie & Partners, sans changer la substance.
      L’avertissement qui le disait en tête de page a été retiré à la demande
      d’Amélie — il s’adressait à elle, pas au client. **L’exigence, elle,
      tient toujours : ce point reste à cocher avant la mise en ligne.**

## Visuels et vidéos

- [ ] **Le portrait ajouté sur `diagnostic.html`** (`portrait-amelie-jardin.jpg`)
      doit-il aussi remplacer le portrait principal de l’accueil et de la page
      « À propos » ? Aujourd’hui les deux coexistent.
- [ ] **Droits sur la photographie « I Love You »** (`temoignages-vitrine.jpg`).
      Elle est installée à votre demande, après réserve de ma part. Son sujet
      est une œuvre de Mr Brainwash, signée et numérotée 55/100, qui occupe
      tout le cadre : ce n’est pas un décor incident. La publier sur un site
      commercial demande de vérifier les droits de reproduction. L’œuvre est
      créditée en légende ; une mention n’est pas une autorisation.
- [ ] **Lisibilité de la mention imprimée sur l’œuvre.** On y lit
      « Terms and conditions may vary ». Sur une page de témoignages, à côté
      de résultats rapportés, cette phrase peut se lire comme une réserve
      ironique. À relire à l’écran avant la mise en ligne.

- [ ] Valider le choix et le cadrage des photographies fournies. Chacune sert
      à plusieurs endroits : voir le tableau de `GUIDE-VISUELS.md`.
- [ ] Confirmer les droits d’usage commercial de chaque photographie.
- [ ] Confirmer que le portrait de la fondatrice est celui à publier.
- [ ] Confirmer les deux photographies de la carte postale de `a-propos.html` :
      la tour Eiffel vue de la Seine et la tour de la Tortue sur le lac Hoan
      Kiem. Le texte alternatif nomme le monument vietnamien ; le dire
      autrement si ce rapprochement n’est pas souhaité.
- [ ] Valider la présence des deux drapeaux, France et Viêt Nam, sur le trajet
      de la carte postale. Ce sont les deux seules touches de couleur hors
      palette du site.
- [ ] Déposer les vidéos d’ambiance dans `assets/videos/` (`accueil.mp4`,
      `paris.mp4`, `a-propos.mp4`). Tant qu’elles sont absentes, la
      photographie s’affiche et le navigateur enregistre une requête sans
      réponse, sans effet visible.
- [ ] Valider l’image de partage (`assets/images/og-image.jpg`), construite à
      partir du bloc marine fourni.
- [ ] Valider la carte du parcours de `a-propos.html` : elle est stylisée et
      décorative, elle ne prétend pas être une carte géographique.

## Mentions légales et données · obligatoire avant live

- [x] Dénomination sociale : **AMÉLIE ET PARTNERS**, nom commercial
      **AMÉLIE & PARTNERS**.
- [x] SIREN : **940 688 377**.
- [x] Hébergeur : **OVH SAS**, SAS au capital de 50 000 000 €, 2 rue
      Kellermann, 59100 Roubaix, France, RCS Lille Métropole
      424 761 419 00045, TVA FR 22 424 761 419.
- [ ] Centre de données retenu, pour pouvoir écrire où sont les serveurs.
- [x] Forme juridique : **SAS**, société par actions simplifiée.
- [x] Siège social : **123 rue des Dames, 75017 Paris**.
- [x] SIRET du siège : **940 688 377 00016**.
- [x] TVA intracommunautaire : **FR08 940 688 377**.
- [x] Code APE : **74.90B**, activités spécialisées, scientifiques et
      techniques diverses.
- [x] Immatriculation au Registre national des entreprises : **11 février
      2025**.
- [ ] Capital social : la fiche d’annuaire ne le donne pas, il figure sur
      les statuts ou l’extrait RNE.
- [ ] Nom de la directrice de publication, à confirmer.
- [ ] Bureau d’enregistrement du domaine `amelie-invest.com`.
- [ ] Adresse du profil LinkedIn :
      `https://www.linkedin.com/company/amelie-partners` : page publiée ?

Les informations d’immatriculation ont été recopiées depuis la fiche
d’annuaire transmise par Eric. Deux lignes restent marquées « à compléter »
en couleur dans la page : le capital social et le nom de la directrice de la
publication.
- [ ] Mentions des activités réglementées éventuellement exercées : carte
      professionnelle, garantie financière, assurance de responsabilité civile
      professionnelle.
- [ ] Politique de confidentialité complétée.
- [x] Calendly : prestataire déclaré, avec un lien vers sa politique.
- [x] Hébergeur : OVH, déclaré. Serveurs dans l’Union européenne, donc
      aucun transfert hors UE à déclarer de ce fait.
- [ ] Reste à déclarer : messagerie, mesure d’audience, CRM éventuel.
- [ ] Durées de conservation et base légale des données.
- [ ] Bandeau de consentement installé **avant** tout traceur non essentiel.

Les fichiers `mentions-legales.html` et `confidentialite.html` sont des
modèles de travail : chaque mention à compléter y est signalée en couleur.
Ils doivent être relus et adaptés par un professionnel du droit ; ce ne sont
pas des conseils juridiques.

## Formulaire de contact

Le formulaire est en place sur `contact.html`. Comme le site est statique et
n’appelle aucun domaine tiers, il n’envoie rien lui-même : à la validation,
le script compose le message dans la messagerie du visiteur, déjà rempli. Le
visiteur reste libre de l’envoyer, et aucune donnée saisie ne transite par le
site. Sans JavaScript, le formulaire reste affiché et l’adresse e-mail est
écrite juste au-dessus.

- [ ] Vérifier que ce fonctionnement convient. Il suppose une messagerie
      configurée chez le visiteur : sur un poste sans client de messagerie,
      le bouton n’ouvre rien et il reste l’adresse écrite à côté.
- [ ] Si Amélie préfère recevoir les messages sans passer par la messagerie
      du visiteur, il faut un service de traitement (Formspree, Netlify
      Forms, Basin…), le déclarer dans la page « Données personnelles », et
      accepter que le site appelle alors un domaine tiers.

## Référencement et mesure · recommandé

- [ ] Connecter Google Search Console ou un équivalent.
- [ ] Envoyer `https://amelie-invest.com/sitemap.xml`.
- [ ] Mesurer au minimum : clic réservation, clic e-mail, visite diagnostic,
      lecture ressource.
- [ ] Choisir un outil de mesure respectueux du consentement.
- [ ] Vérifier les données structurées avec l’outil de test de Google.

## Qualité finale

- [ ] Tests sur iPhone et Android réels.
- [ ] Tests Chrome, Safari et Firefox.
- [ ] Navigation complète au clavier, y compris le menu déroulant, la FAQ, le
      bandeau des témoignages et le bloc de réservation en deux temps.
- [ ] Aucun lien cassé : `python3 outils/verifier-site.py`.
- [ ] Poids des images contrôlé après remplacement.
- [ ] Sauvegarde de la version précédente et procédure de retour arrière.

## Contrôles déjà effectués

- Onze pages rendues dans Chromium à 375, 768, 1024, 1200 et 1440 px :
  aucun débordement horizontal, aucune erreur JavaScript.
- Liens internes, ancres, ressources référencées, titres, descriptions et
  attributs `alt` vérifiés par `outils/verifier-site.py`.
- Huit témoignages présents, textes et attributions identiques à ceux de la
  version d’origine, mention sur la variabilité des résultats conservée.
- Contrastes calculés selon WCAG 2.1, voir `DESIGN-SYSTEM.md`.
- Comportement sans JavaScript vérifié dans le code : contenus visibles, menu
  déplié, FAQ native, réservation accessible par lien direct.

Aucun contrôle sur appareil réel ni sur Safari ou Firefox n’a été effectué.
