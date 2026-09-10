# Instructions permanentes · Amélie & Partners

Site de conseil en stratégie d’investissement immobilier, publié sur
`amelie-invest.com`. Lire `README.md`, `DESIGN-SYSTEM.md`, `GUIDE-VISUELS.md`
et `A-VALIDER-AVANT-LIVE.md` avant toute modification.

## Nature du projet

Site **statique** : HTML, CSS, JavaScript simple. Aucune compilation, aucun
gestionnaire de paquets, aucune dépendance externe, aucun framework. Une
seule exception, hors des pages : `api/contact.js`, la fonction serveur qui
reçoit le formulaire de contact et fait partir le message. Le site est
publié sur **Vercel**, qui sert les pages et exécute ce dossier `api/`. Ne
pas introduire React, Next.js, Tailwind, shadcn, TypeScript ni aucun script
distant. Si une idée d’interface vient d’un composant React, la réécrire en
HTML, CSS et JavaScript simple pour ce site.

## Mission

Préserver et renforcer un site lisible, attirant, professionnel, crédible et
orienté vers la réservation d’un premier échange. Le territoire de marque est
celui d’un cabinet d’investissement et d’une maison éditoriale parisienne :
calme, précision, indépendance, méthode et décision.

## Invariants de marque

- Nom : `AMÉLIE & PARTNERS`.
- Marque : le fichier fourni `assets/images/logo.png`, un entrelacs de
  **trois boucles** en lavande. L’employer tel quel : ne pas le redessiner,
  ne pas le recolorer, ne pas faire varier son nombre de
  boucles. Voir `DESIGN-SYSTEM.md`.
- Signature du logo : `Investir avec méthode · Décider avec clarté`.
- Promesse principale : `Votre partenaire stratégique pour réussir vos projets
  immobiliers.`
- Finalité : `Le patrimoine n’est pas une fin. C’est un moyen de gagner en
  liberté de choix.`
- Ton : posé, concret, exigeant, pédagogique. Jamais agressif, tapageur ou
  fondé sur une promesse d’enrichissement.
- Ordre narratif : promesse de marque → expérience → approche →
  accompagnements → témoignages → premier échange → FAQ. Le site ne segmente
  pas ses visiteurs : pas de page ni de parcours « particuliers » ou
  « professionnels ». Le contenu commercial reste celui de la proposition
  d’origine.
- Les textes commerciaux parlent au nom de la marque. Éviter « J’accompagne »,
  « mon approche », « mes ressources ». Les citations et témoignages gardent
  leur voix. Ne pas inventer une équipe, des associés ou des partenaires non
  confirmés.
- Bandeau de tête de l’accueil : label `AMÉLIE & PARTNERS`, titre `Votre
  partenaire stratégique pour réussir vos projets immobiliers.`, sous-titre
  `De la stratégie à la mise en œuvre, Amélie & Partners accompagne les
  investisseurs pour financer, acquérir et piloter leur patrimoine
  immobilier.`
- Portrait : `Amélie-Thu DUONG · Fondatrice & Investisseuse à Paris depuis
  2014`.
- Ne jamais copier l’identité graphique ou les textes d’un site de référence.

## Offre

Source commerciale prioritaire : `AEP_OFFRE_V3_Amelie_Partners_Reference_2026.pdf`.

Quatre formats : **Diagnostic Stratégique**, **Stratégie de Financement**,
**Recherche immobilière à Paris**, **Trajectoire Investisseur**.

Diagnostic : **432 € TTC**, questionnaire préparatoire, session d’une heure,
Note de Diagnostic & Décision, cadrage gratuit de 30 minutes. Verdicts :
AVANCER, PRÉPARER, RESTRUCTURER, APPROFONDIR, SUSPENDRE.

Les périmètres et tarifs des trois autres offres restent à finaliser. Ne pas
réintroduire les anciens forfaits ni la sélection Premium. Le taux de 98 %
reste retiré de l’affichage en attendant une définition, une base et une
période auditées. La réussite est une destination recherchée, jamais une
garantie. Les méthodes non lancées restent confidentielles.

## Preuve sociale · ne pas dégrader

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
grands titres, Inter pour le reste, Caveat pour la carte postale de
`a-propos.html` — son titre et ses noms de lieu — et pour la phrase d’Amélie
posée à côté d’elle. Ces deux blocs, et eux seuls : l’écriture manuscrite
reste rare, c’est ce qui lui donne son poids. Angles francs, peu d’ombres, grands espaces. Chevrons
vectoriels monochromes : aucun émoji, aucune flèche Unicode.

## Règles techniques non négociables

1. **Sans JavaScript**, tout le contenu reste visible et navigable. Les
   apparitions ne sont armées que sous `html.js`.
2. **`prefers-reduced-motion`** neutralise toutes les animations et empêche le
   chargement des vidéos.
3. Toute animation en boucle a une commande d’arrêt visible et au clavier.
   Celle du couloir de photographies est une case à cocher masquée pilotée
   par son étiquette : elle fonctionne donc sans JavaScript.
4. Aucune information n’existe uniquement dans une image ou une animation.
5. Les vidéos sont muettes, facultatives et retombent sur une photographie si
   le fichier est absent ou illisible.
6. Aucun appel à un domaine tiers dans les pages : polices, styles et scripts
   sont hébergés avec le site. La mesure d’audience Vercel fait exception à
   la règle du fichier, pas à celle du domaine : son script est servi par
   l’hébergeur sur `/_vercel/insights/script.js`, un chemin du site
   lui-même, et n’y dépose aucun cookie. Seuls Calendly, LinkedIn et `mailto:` sont des
   liens sortants ; la politique de confidentialité de Calendly est citée
   sur les pages légales. Le formulaire de contact poste sur `/api/contact`,
   c’est-à-dire sur le site lui-même : le navigateur ne s’adresse jamais à
   Resend, seule la fonction serveur le fait, et la clé d’API vit dans les
   variables d’environnement du projet Vercel. Si la fonction ne répond pas,
   la saisie n’est pas perdue : un lien la reprend dans la messagerie du
   visiteur. Voir `INSTALLATION-FORMULAIRE.md`.
7. Une seule balise `h1` par page.

## Langues

Le site est **multilingue** depuis septembre 2026 : français, anglais et
vietnamien. Le français vit à la racine, les autres langues dans un dossier :
`/en/`, `/vi/`. Trois règles tiennent l’ensemble :

1. Les **liens entre pages restent relatifs** (`approche.html`). C’est ce qui
   fait qu’une page anglaise renvoie vers une page anglaise sans qu’on
   l’écrive.
2. Les **fichiers du site s’appellent en absolu** (`/assets/…`), et sont donc
   partagés par toutes les langues.
3. `langues.py` porte les textes de la coquille et la liste `PUBLIEES` : une
   langue n’apparaît dans le sélecteur et dans les `hreflang` que le jour où
   ses pages existent.

Le sélecteur est un **menu déroulant natif** — un `details` — visible à toutes
les largeurs, téléphone compris. Il s’ouvre au clavier, s’annonce avec son
état et fonctionne sans JavaScript ; le script n’ajoute que les deux gestes
qu’un `details` ne connaît pas de lui-même, la touche d’échappement et le clic
à côté. Sa classe est `langues-choix` : `langues`, sans suffixe, appartient
déjà à la phrase « L’échange se tient en… » de la page Contact.

Le vietnamien demande deux fichiers de police de plus, `inter-vietnamese` et
`source-serif-4-vietnamese` : le sous-jeu latin étendu s’arrête avant les
lettres à ton. **Caveat n’existe pas en vietnamien** ; la carte postale de
`a-propos.html` emploie donc le serif du site sur ces pages, par la section 48
de `styles.css`. Voir `DESIGN-SYSTEM.md`.

Décisions prises avec Amélie : **une seule version anglaise** ; les
**citations des témoignages restent en français**, les traduire reviendrait à
les modifier ; les **pages légales ne sont pas traduites**, les autres langues
y renvoient en indiquant que le français fait foi.

Le nom de la marque, sa signature et les noms des offres ne se traduisent
jamais : ce sont des noms propres. Les cinq verdicts non plus : `AVANCER`,
`PRÉPARER`, `RESTRUCTURER`, `APPROFONDIR`, `SUSPENDRE` sont les mots que
porte la Note de Diagnostic & Décision ; la page les explique en anglais sans
les remplacer.

**Le prix reste français et le droit reste français.** 432 € TTC : la
prestation est vendue en France, facturée en France, soumise à la TVA
française. Les pages anglaises écrivent donc le prix en euros et traduisent
« TTC » par « incl. French VAT » ; elles ne convertissent rien. Les renvois
vers les pages légales disent qu’elles sont en français.

L’anglais est **fabriqué à partir du français publié**, pas écrit à part : la
page française sert de source, sa coquille est refaite dans la langue voulue
et son corps est traduit chaîne par chaîne à partir d’un dictionnaire. Une
chaîne absente du dictionnaire arrête la fabrication : aucune phrase ne peut
rester en français par oubli. Conséquence pratique : **traduire vient après
générer**, jamais avant, et une retouche du français se répercute en
relançant la traduction.

Deux précautions valent d’être connues. Les listes déroulantes du formulaire
reçoivent une valeur française explicite avant traduction : le visiteur lit
sa langue, le serveur reçoit ce que `api/contact.js` attend, et le message
qui arrive chez Amélie garde le même vocabulaire quelle que soit la langue.
Et le champ caché `retour`, qui sert au renvoi sans JavaScript, porte le
préfixe de langue ; `api/contact.js` l’accepte, en le contrôlant.

## Où modifier

- Pages : les quatorze fichiers `.html` à la racine, plus un dossier par
  langue supplémentaire.
- Mise en forme : `assets/css/styles.css`, sections numérotées.
- Comportements : `assets/js/site.js`.
- Visuels : `assets/images/` et `assets/videos/`, voir `GUIDE-VISUELS.md`.

L’en-tête et le pied de page sont **répétés dans chaque page**. Une
modification de navigation doit être reportée dans les quatorze fichiers
français, puis dans chaque dossier de langue.

## Méthode obligatoire avant livraison

1. Faire un état des lieux des fichiers concernés avant d’éditer.
2. Annoncer précisément ce qui sera modifié et ce qui sera conservé.
3. Implémenter sans réécrire les contenus validés hors périmètre.
4. Lancer `python3 outils/verifier-site.py` : il doit renvoyer « Aucune
   erreur ».
5. Relancer `python3 outils/donnees-structurees.py` si `index.html` ou
   `diagnostic.html` ont été régénérés, et
   `python3 outils/dimensions-images.py` après tout changement de visuel.
   Puis refabriquer les pages traduites : elles descendent des pages
   françaises et vieillissent dès que celles-ci changent.
6. Vérifier le rendu à 375, 768, 1024, 1200 et 1440 px.
7. Vérifier clavier, contrastes, textes alternatifs et mouvement réduit.
8. Donner un résumé des fichiers modifiés, des tests réellement effectués et
   des points qui nécessitent encore une décision d’Amélie.

## Définition de terminé

Une tâche n’est terminée que si elle est visible dans le navigateur,
responsive, accessible au clavier, sans lien cassé, sans régression sur les
témoignages, et avec un chemin clair vers la prise de rendez-vous.
