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
- [ ] Prix du Diagnostic Stratégique : `450 € HT / diagnostic`.
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

## Visuels et vidéos

- [ ] Valider le choix et le cadrage des photographies fournies. Chacune sert
      à plusieurs endroits : voir le tableau de `GUIDE-VISUELS.md`.
- [ ] Confirmer les droits d’usage commercial de chaque photographie.
- [ ] Confirmer que le portrait de la fondatrice est celui à publier.
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
- [x] Hébergeur : **Vercel Inc.**, 440 N Barranca Ave #4133, Covina,
      CA 91723, États-Unis.
- [ ] Forme juridique et capital social.
- [ ] Adresse du siège.
- [ ] SIRET du siège, greffe du RCS et date d’immatriculation.
- [ ] Numéro de TVA intracommunautaire, si applicable.
- [ ] Code APE et son libellé.
- [ ] Nom de la directrice de publication.
- [ ] Bureau d’enregistrement du domaine `amelie-invest.com`.
- [ ] Adresse du profil LinkedIn :
      `https://www.linkedin.com/company/amelie-partners` : page publiée ?

Les données de l’éditeur n’ont pas pu être vérifiées depuis cet
environnement : l’accès à `annuaire-entreprises.data.gouv.fr` y est bloqué.
Rien n’a donc été deviné ; seul le SIREN transmis par Eric est inscrit, et
toutes les autres lignes restent marquées « à compléter » dans la page.
- [ ] Mentions des activités réglementées éventuellement exercées : carte
      professionnelle, garantie financière, assurance de responsabilité civile
      professionnelle.
- [ ] Médiateur de la consommation, si l’activité y est soumise.
- [ ] Politique de confidentialité complétée.
- [x] Calendly : prestataire déclaré, avec un lien vers sa politique.
- [x] Hébergeur : Vercel, déclaré.
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
