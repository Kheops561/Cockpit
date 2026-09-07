# À valider avant la mise en ligne publique

Le site est techniquement exploitable. Les éléments ci-dessous doivent être
confirmés par Amélie avant de considérer la publication comme définitive.

## Décidé

- [x] Domaine : **amelie-invest.com** (sans `www`). Il est déjà inscrit dans
      les balises canoniques, `sitemap.xml`, `robots.txt` et les données
      structurées. Si la décision change, relancer
      `python3 outils/donnees-structurees.py` après avoir modifié le domaine
      dans ce script, puis reprendre `sitemap.xml`, `robots.txt` et les
      `<link rel="canonical">` des treize pages.

## Identité et conversion — priorité haute

- [ ] Adresse e-mail publique : `contact@amelie-invest.com` — boîte créée et
      relevée ?
- [ ] Lien Calendly : `https://calendly.com/amelie-partners` — compte actif,
      créneau de **30 minutes** publié ?
- [ ] Durée du premier échange : 30 minutes.
- [ ] Prix du Diagnostic Stratégique : `450 € HT / diagnostic`.
- [ ] Zone d’intervention : Paris pour la recherche ; France au cas par cas
      pour la stratégie et l’arbitrage.

## Nouveau public : les professionnels — à relire mot à mot

La page `professionnels.html` a été écrite pour ce site. Elle n’existait pas
sur la version précédente. Rien n’y est chiffré et aucun tarif nouveau n’y
figure, mais son périmètre engage le cabinet.

- [ ] Valider le périmètre annoncé : revenus non salariés et capacité réelle,
      murs d’activité et locaux professionnels, détention et arbitrages.
- [ ] Valider la limite affichée : « ne délivre pas de conseil juridique,
      fiscal ou comptable et ne se substitue pas aux professionnels
      réglementés — expert-comptable, notaire, avocat, courtier ».
- [ ] Confirmer que la recherche immobilière peut concerner des locaux
      professionnels, ou faire retirer cette réponse de la FAQ.
- [ ] Vérifier la FAQ « détenir en nom propre ou en société » : la réponse
      renvoie explicitement la décision aux conseils réglementés.

## Preuves sociales — priorité haute

- [ ] Autorisation de publication pour chacun des huit témoignages.
- [ ] Validation des prénoms, initiales, âges, métiers, entreprises, villes et
      résultats cités.
- [ ] Validation des chiffres : `> 35`, `> 25 M€`, `> 75`, `> 80`.
- [ ] Conservation de la phrase : `Chaque témoignage reflète une expérience
      individuelle ; les résultats varient selon les situations.`

Le taux de 98 % n’est affiché nulle part, en attente d’une définition, d’une
base et d’une période auditées.

## Visuels et vidéos

- [ ] Remplacer les visuels provisoires par de vraies photographies — voir
      `GUIDE-VISUELS.md` pour les noms de fichiers et l’ordre de priorité.
- [ ] Déposer les vidéos d’ambiance dans `assets/videos/` (`accueil.mp4`,
      `paris.mp4`, `a-propos.mp4`). Tant qu’elles sont absentes, la
      photographie s’affiche et le navigateur enregistre une requête sans
      réponse, sans effet visible.
- [ ] Créer une image Open Graph 1200 × 630 px dédiée à la marque
      (`assets/images/og-image.jpg`).
- [ ] Vérifier les droits d’usage commercial de chaque image.
- [ ] Valider la carte du parcours de `a-propos.html` : elle est stylisée et
      décorative, elle ne prétend pas être une carte géographique.

## Mentions légales et données — obligatoire avant live

- [ ] Dénomination sociale exacte.
- [ ] Forme juridique et capital social.
- [ ] Adresse du siège.
- [ ] SIREN/SIRET, RCS et ville d’immatriculation.
- [ ] Numéro de TVA intracommunautaire, si applicable.
- [ ] Nom de la directrice de publication.
- [ ] Coordonnées et identité de l’hébergeur retenu.
- [ ] Mentions des activités réglementées éventuellement exercées : carte
      professionnelle, garantie financière, assurance de responsabilité civile
      professionnelle.
- [ ] Médiateur de la consommation, si l’activité y est soumise.
- [ ] Politique de confidentialité complétée.
- [ ] Liste des prestataires recevant des données : Calendly, messagerie,
      hébergeur, mesure d’audience, CRM éventuel.
- [ ] Durées de conservation et base légale des données.
- [ ] Bandeau de consentement installé **avant** tout traceur non essentiel.

Les fichiers `mentions-legales.html` et `confidentialite.html` sont des
modèles de travail : chaque mention à compléter y est signalée en couleur.
Ils doivent être relus et adaptés par un professionnel du droit ; ce ne sont
pas des conseils juridiques.

## Formulaire de contact

- [ ] Décider s’il faut un formulaire. Le code est prêt et commenté dans
      `contact.html` ; il faut un service de traitement (Formspree, Netlify
      Forms, Basin…) et l’ajouter à la politique de confidentialité. Tant que
      ce choix n’est pas fait, la page propose la réservation Calendly et
      l’adresse e-mail, sans formulaire qui perdrait les messages.

## Référencement et mesure — recommandé

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

- Treize pages rendues dans Chromium à 375, 768, 1024, 1200 et 1440 px :
  aucun débordement horizontal, aucune erreur JavaScript.
- Liens internes, ancres, ressources référencées, titres, descriptions et
  attributs `alt` vérifiés par `outils/verifier-site.py`.
- Huit témoignages présents, textes et attributions identiques à ceux de la
  version d’origine, mention sur la variabilité des résultats conservée.
- Contrastes calculés selon WCAG 2.1 — voir `DESIGN-SYSTEM.md`.
- Comportement sans JavaScript vérifié dans le code : contenus visibles, menu
  déplié, FAQ native, réservation accessible par lien direct.

Aucun contrôle sur appareil réel ni sur Safari ou Firefox n’a été effectué.
