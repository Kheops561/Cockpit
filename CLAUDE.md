# Instructions permanentes — Amélie & Partners

Site de conseil en stratégie d’investissement immobilier, publié sur
`amelie-invest.com`. Lire `README.md`, `DESIGN-SYSTEM.md`, `GUIDE-VISUELS.md`
et `A-VALIDER-AVANT-LIVE.md` avant toute modification.

## Nature du projet

Site **statique** : HTML, CSS, JavaScript simple. Aucune compilation, aucun
gestionnaire de paquets, aucune dépendance externe, aucun framework. Ne pas
introduire React, Next.js, Tailwind, shadcn, TypeScript ni aucun script
distant. Si une idée d’interface vient d’un composant React, la réécrire en
HTML, CSS et JavaScript simple pour ce site.

## Mission

Préserver et renforcer un site lisible, attirant, professionnel, crédible et
orienté vers la réservation d’un premier échange. Le territoire de marque est
celui d’un cabinet d’investissement et d’une maison éditoriale parisienne :
calme, précision, indépendance, méthode et décision.

## Invariants de marque

- Nom : `AMÉLIE & PARTNERS`.
- Marque : un entrelacs de **quatre boucles**, dessiné en SVG dans les pages.
  Il reste identique partout : ne pas le recomposer, ne pas faire varier son
  nombre de boucles selon le contexte, ne pas l’animer. Voir
  `DESIGN-SYSTEM.md` et `outils/marque.py`.
- Signature du logo : `Investir avec méthode · Décider avec clarté`.
- Promesse principale : `Votre partenaire stratégique pour réussir vos projets
  immobiliers.`
- Finalité : `Le patrimoine n’est pas une fin. C’est un moyen de gagner en
  liberté de choix.`
- Ton : posé, concret, exigeant, pédagogique. Jamais agressif, tapageur ou
  fondé sur une promesse d’enrichissement.
- Ordre narratif : promesse de marque → publics → expérience → approche →
  accompagnements → témoignages → premier échange → FAQ.
- Les textes commerciaux parlent au nom de la marque. Éviter « J’accompagne »,
  « mon approche », « mes ressources ». Les citations et témoignages gardent
  leur voix. Ne pas inventer une équipe, des associés ou des partenaires non
  confirmés.
- Bandeau de tête de l’accueil : label `AMÉLIE & PARTNERS`, titre `Votre
  partenaire stratégique pour réussir vos projets immobiliers.`, sous-titre
  `De la stratégie à la mise en œuvre, Amélie & Partners accompagne les
  investisseurs pour financer, acquérir et piloter leur patrimoine
  immobilier.`
- Portrait : `Amélie-Thu DUONG — Fondatrice & Investisseuse à Paris depuis
  2014`.
- Ne jamais copier l’identité graphique ou les textes d’un site de référence.

## Offre

Source commerciale prioritaire : `AEP_OFFRE_V3_Amelie_Partners_Reference_2026.pdf`.

Quatre formats : **Diagnostic Stratégique**, **Stratégie de Financement**,
**Recherche immobilière à Paris**, **Trajectoire Investisseur**.

Diagnostic : **450 € HT**, questionnaire préparatoire, session de 75 minutes,
Note de Diagnostic & Décision, cadrage gratuit de 30 minutes. Verdicts :
AVANCER, PRÉPARER, RESTRUCTURER, APPROFONDIR, SUSPENDRE.

Les périmètres et tarifs des trois autres offres restent à finaliser. Ne pas
réintroduire les anciens forfaits ni la sélection Premium. Le taux de 98 %
reste retiré de l’affichage en attendant une définition, une base et une
période auditées. La réussite est une destination recherchée, jamais une
garantie. Les méthodes non lancées restent confidentielles.

## Deux publics

`particuliers.html` et `professionnels.html` s’adressent respectivement aux
investisseurs particuliers et aux dirigeants, indépendants et professions
libérales. La méthode est la même ; ce qui change est la lecture des
contraintes. La page professionnels affiche une limite explicite : le cabinet
ne délivre pas de conseil juridique, fiscal ou comptable et ne se substitue
pas aux professionnels réglementés. Ne pas retirer cette limite.

## Preuve sociale — ne pas dégrader

- Le titre de la section est `Témoignages`, jamais `Décisions clients`.
- Conserver les huit témoignages et leur bandeau horizontal animé, textes et
  attributions à l’identique.
- Bandeau : défilement continu, pause au survol et au focus, commande de
  pause explicite. En mouvement réduit : défilement manuel, sans animation.
- Pas de compteur de parcours, pas de numérotation des cartes. La partie
  « Œil d’Amélie » reste absente du site.
- Ne jamais inventer, embellir ou modifier un chiffre, un résultat ou un
  témoignage sans validation écrite d’Amélie.
- Toujours conserver la mention indiquant que les résultats varient selon les
  situations.

## Règles de conversion

- CTA principal : `Analyser ma situation` ou `Réserver un premier échange`.
- Le premier écran annonce : 30 minutes gratuites, sans engagement, regard
  indépendant.
- Lien de réservation : `https://calendly.com/amelie-partners`, à confirmer.
- E-mail : `contact@amelie-invest.com`, à confirmer.
- Toute page mène naturellement vers `diagnostic.html`, sans répéter un bouton
  à chaque paragraphe.
- Aucun faux compte à rebours, pop-up agressif, rareté artificielle ou
  affirmation de résultat garanti.

## Design

Palette, typographie, échelle, points de rupture et composants : voir
`DESIGN-SYSTEM.md`. Points essentiels : bleu nuit `#12283c`, ivoire `#f8f5ef`,
lavande `#cbb5df` / `#75508f`, rouille `#a05234` ; Source Serif 4 pour les
grands titres, Inter pour le reste, Caveat pour la seule note manuscrite de
`a-propos.html`. Angles francs, peu d’ombres, grands espaces. Chevrons
vectoriels monochromes : aucun émoji, aucune flèche Unicode.

## Règles techniques non négociables

1. **Sans JavaScript**, tout le contenu reste visible et navigable. Les
   apparitions ne sont armées que sous `html.js`.
2. **`prefers-reduced-motion`** neutralise toutes les animations et empêche le
   chargement des vidéos.
3. Toute animation en boucle a une commande d’arrêt visible et au clavier.
4. Aucune information n’existe uniquement dans une image ou une animation.
5. Les vidéos sont muettes, facultatives et retombent sur une photographie si
   le fichier est absent ou illisible.
6. Aucun appel à un domaine tiers dans les pages : polices, styles et scripts
   sont hébergés avec le site. Seuls Calendly et `mailto:` sont des liens
   sortants.
7. Une seule balise `h1` par page.

## Où modifier

- Pages : les treize fichiers `.html` à la racine.
- Mise en forme : `assets/css/styles.css`, sections numérotées.
- Comportements : `assets/js/site.js`.
- Visuels : `assets/images/` et `assets/videos/` — voir `GUIDE-VISUELS.md`.

L’en-tête et le pied de page sont **répétés dans chaque page**. Une
modification de navigation doit être reportée dans les treize fichiers.

## Méthode obligatoire avant livraison

1. Faire un état des lieux des fichiers concernés avant d’éditer.
2. Annoncer précisément ce qui sera modifié et ce qui sera conservé.
3. Implémenter sans réécrire les contenus validés hors périmètre.
4. Lancer `python3 outils/verifier-site.py` — il doit renvoyer « Aucune
   erreur ».
5. Relancer `python3 outils/donnees-structurees.py` si `index.html` ou
   `diagnostic.html` ont été régénérés.
6. Vérifier le rendu à 375, 768, 1024, 1200 et 1440 px.
7. Vérifier clavier, contrastes, textes alternatifs et mouvement réduit.
8. Donner un résumé des fichiers modifiés, des tests réellement effectués et
   des points qui nécessitent encore une décision d’Amélie.

## Définition de terminé

Une tâche n’est terminée que si elle est visible dans le navigateur,
responsive, accessible au clavier, sans lien cassé, sans régression sur les
témoignages, et avec un chemin clair vers la prise de rendez-vous.
