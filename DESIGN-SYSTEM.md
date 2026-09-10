# Design system · Amélie & Partners

Territoire de marque : un cabinet d’investissement et une maison éditoriale
parisienne. Calme, précision, indépendance, méthode, décision. Angles francs,
peu d’ombres, grands espaces, photographie architecturale.

Tout est défini dans `assets/css/styles.css`, dans la section « 1 tokens ».
Modifier une valeur là met à jour tout le site.

## Couleurs

Palette reprise du site d’origine. Ne pas la modifier sans validation.

| Rôle | Variable | Valeur |
|---|---|---|
| Bleu nuit | `--ink` | `#12283c` |
| Bleu nuit adouci | `--ink-soft` | `#1d3549` |
| Ivoire (fond) | `--paper` | `#f8f5ef` |
| Ivoire secondaire | `--paper-soft` | `#efebe4` |
| Lavande | `--lavender` | `#cbb5df` |
| Lavande claire | `--lavender-soft` | `#eee7f4` |
| Lavande sombre (accent) | `--lavender-dark` | `#75508f` |
| Rouille | `--rust` | `#a05234` |
| Rouille claire | `--rust-soft` | `#ead4c6` |
| Rouille éclaircie (fond sombre) | `--rust-light` | `#d08a63` |
| Texte courant | `--text` | `#273744` |
| Texte secondaire | `--muted` | `#52616c` |

### Contrastes

Rapports calculés selon WCAG 2.1 (le détail du calcul est reproductible : voir
plus bas). Tous atteignent au moins le niveau AA pour du texte courant.

| Combinaison | Rapport | Niveau |
|---|---|---|
| Texte courant `#273744` sur ivoire `#f8f5ef` | 11,24:1 | AAA |
| Bleu nuit `#12283c` sur ivoire | 13,84:1 | AAA |
| Ivoire sur bleu nuit (bouton principal) | 13,84:1 | AAA |
| Blanc sur bleu nuit | 15,06:1 | AAA |
| Texte secondaire `#52616c` sur ivoire | 5,87:1 | AA |
| Lavande sombre `#75508f` sur ivoire | 5,85:1 | AA |
| Rouille `#a05234` sur ivoire | 5,14:1 | AA |
| Texte secondaire sur ivoire secondaire `#efebe4` | 5,38:1 | AA |
| Lavande sombre sur ivoire secondaire | 5,35:1 | AA |
| Rouille sur ivoire secondaire | 4,71:1 | AA |
| Lavande `#cbb5df` sur bleu nuit | 8,04:1 | AAA |
| Rouille éclaircie `#d08a63` sur bleu nuit | 5,38:1 | AA |

La lavande claire `#cbb5df` ne sert de couleur de texte **que sur fond bleu
nuit** (surtitres, libellés). Sur ivoire, elle est réservée aux filets, aux
fonds et aux repères.

Le rapport le plus juste du site est la rouille sur ivoire secondaire
(4,71:1) : il tient pour du texte courant, mais ne descendez pas cette
couleur plus bas et ne l’employez pas sous 14 px.

La rouille de marque `#a05234` ne se lit **pas** sur le bleu nuit (2,69:1).
Sur fond sombre, employez `--rust-light` `#d08a63` : c’est la même couleur
éclaircie, et elle passe le niveau AA.

## La marque

Le logo est un **entrelacs de trois boucles**, en lavande, fourni par la
marque et employé tel quel : `assets/images/logo.png`. Il n’est ni
recomposé ni recoloré. Sur `approche.html`, il se pose à l’apparition comme
un cachet, une rotation courte, puis plus rien. Jamais d’animation continue.

La lavande se détache aussi bien sur l’ivoire que sur le bleu nuit, si bien
qu’un seul fichier sert dans tous les contextes.

| Où | Fond |
|---|---|
| En-tête | Ivoire, à côté du nom |
| Pied de page | Bleu nuit |
| Schéma de `approche.html` | Ivoire secondaire |
| Onglet du navigateur (`favicon.png`) | Bleu nuit |
| Partage sur les réseaux (`og-image.jpg`) | Bleu nuit, avec le nom |

**À faire trancher.** Le bloc logo fourni porte la signature `PARTENAIRE
STRATÉGIQUE DES INVESTISSEURS IMMOBILIERS` et écrit `AMELIE & PARTNERS` sans
accent. Les instructions de marque retiennent `Investir avec méthode ·
Décider avec clarté` et `AMÉLIE & PARTNERS` avec accent : c’est cette version
qui figure sur le site. Voir `A-VALIDER-AVANT-LIVE.md`.

## Typographie

- **Source Serif 4** : grands titres uniquement (`h1` à `h4`, `.pull`).
- **Inter** : corps de texte, cartes, boutons, témoignages, navigation.
- **Caveat** : exception unique et volontaire : la note manuscrite de la
  fondatrice et sa signature, sur `a-propos.html`. Jamais un titre, jamais un
  bouton, jamais un contenu informatif.

Pas d’italique décoratif. Les polices sont locales (`assets/fonts/`), sous
licence SIL OFL 1.1 (`assets/fonts/OFL.txt`) : aucun appel à un service de
polices externe, donc aucun traceur tiers de ce fait.

### Le vietnamien

Le sous-jeu « latin étendu » s’arrête avant `U+1EA0`, et c’est précisément là
que vivent la plupart des lettres vietnamiennes accentuées, avec `ơ`, `ư`, `đ`
et `ă`. Inter et Source Serif 4 ont donc chacune un **troisième fichier**,
`*-vietnamese.woff2`, déclaré avec sa propre plage : le navigateur ne le
charge que s’il rencontre ces caractères, et les pages françaises et anglaises
n’en téléchargent pas un octet. Les pages vietnamiennes le préchargent, comme
elles préchargent le latin.

**Caveat n’existe pas en vietnamien** : Google ne publie pas ce sous-jeu, et
les lettres à ton n’y sont pas dessinées. Sur les pages vietnamiennes, et sur
elles seules, les deux blocs manuscrits de la carte postale prennent donc le
serif du site en italique (section 48 de `styles.css`). Le geste reste le même
— le trait qui se dessine, le trajet, le filet — mais la lettre est lisible et
entière. Les deux autres emplois de Caveat, la note et la citation d’Amélie,
ne sont pas concernés : ce sont ses mots, ils restent en français.

### Échelle

| Usage | Variable | Valeur |
|---|---|---|
| Titre de premier écran | `--type-display` | `clamp(2.25rem, 4.6vw, 4.25rem)` |
| Titre de section | `--type-title` | `clamp(2rem, 3.6vw, 3.125rem)` |
| Sous-titre | `--type-heading` | `clamp(1.5rem, 2.4vw, 2.125rem)` |
| Titre de carte | `--type-card` | `clamp(1.1875rem, 1.8vw, 1.4375rem)` |
| Corps | aucune | `1.0625rem`, interligne 1,65 |
| Surtitre (`.eyebrow`) | aucune | `0.75rem`, majuscules, interlettrage `.16em` |

## Rythme

- Largeur de lecture : `--wrap` = 1200 px ; `--wrap-narrow` = 780 px.
- Marge latérale : `--gutter` = `clamp(1.25rem, 4vw, 3rem)`.
- Hauteur de section : `--section-y` = `clamp(4rem, 9vw, 8.5rem)`.
- Rayon des angles : **0**. Aucun arrondi, sauf les points et pastilles.

## Points de rupture

| Largeur | Ce qui change |
|---|---|
| < 560 px | Tout est empilé. |
| 560 px | Le schéma des quatre étapes passe sur deux colonnes. |
| 640 px | Le fil du parcours (`a-propos`) apparaît. |
| 700 px | Grilles de deux et quatre cartes sur deux colonnes. |
| 900 px | Les duos texte + image passent côte à côte. |
| 960 px | Grilles de trois et quatre colonnes ; trait du schéma. |
| 1024 px | Portrait détaché sur le bandeau de tête. |
| **1200 px** | Navigation complète et bouton d’en-tête ; en dessous, menu déroulant. Apparitions latérales autorisées. |
| 1400 px | Libellés du fil du parcours. |

## Composants

`assets/css/styles.css` est numéroté par sections : boutons (5), en-tête (6),
bandeau de tête (7), cadres et visuels (8), duo texte + image (9), cartes
(10), étapes (11), listes (12), chiffres (13), témoignages (14), FAQ (15),
bandeau d’appel (16), mises en avant (17), formulaire (18), pied de page
(19), fil d’ariane (20), article (21), page 404 (22), mouvement réduit (23),
bloc de réservation (24), vidéos (25), parcours de la fondatrice (26), fil du
parcours (27), schéma des quatre étapes (28), page témoignages (29),
feuillets du processus (30), carte de témoignage (32), carte de tarif (33),
carrousel (34), voile de transition (35), citation pleine largeur (36),
schéma des étapes (37), promesse en deux volets (38), accompagnements en
diapositives (39), fiche pédagogique (40).

Trois compléments récents :

- `.grid--survol` : sur un groupe de cartes, celle que l’on vise s’avance et
  ses voisines s’effacent. L’effet est purement décoratif, aucune information
  n’y est cachée, et il disparaît sous `prefers-reduced-motion`.
- `.card--vedette` : une carte visuelle dont l’image passe à gauche plutôt
  qu’en tête, pour ne pas devenir démesurée sur une pleine largeur.
- Un bouton posé directement dans une carte ne s’étire plus : `.card > .btn`
  garde sa largeur propre. Une `.btn-row` dans une carte se cale en bas,
  détachée par un filet : deux cartes côte à côte, de contenus inégaux,
  alignent quand même leurs boutons.
- Le bouton fantôme se remplit de bleu nuit, pas de lavande : sur l’ivoire
  d’une carte, un aplat violet pesait plus que l’action qu’il porte.
- `.page-<nom>` : chaque page porte sa classe sur `<body>`, ce qui permet de
  régler une page seule. `a-propos` s’en sert pour resserrer sa colonne à
  1180 px.
- La fiche pédagogique se lit en deux colonnes : le sommaire tient la gauche
  et suit la lecture (`position: sticky`), le texte défile à droite. Le
  sommaire vient en premier dans le document, ce qui est aussi son ordre au
  clavier. Les deux colonnes gardent la même hauteur : sans cela le sommaire,
  aussi court que son contenu, n’aurait aucune course et son maintien en
  place serait sans effet.
- Le PDF de la fiche est fabriqué par `outils/fiche-pdf.py`, qui pose la
  classe `pdf` sur la racine avant d’imprimer et demande les fonds. Ces
  règles ne s’appliquent qu’au fichier fabriqué : couleurs de la maison,
  bandeau bleu nuit en tête, surtitres rouille, notions clés sur lavande, et
  une mise en page resserrée (trois pages au lieu de six). Le visiteur qui
  imprime la page depuis son navigateur garde la version sobre, en noir sur
  blanc, qui n’use pas d’encre.
- La fiche se télécharge en PDF et se partage par `mailto:` avec un message
  déjà rédigé. Rien n’est calculé au clic, aucun service n’est appelé : les
  deux liens fonctionnent sans JavaScript.
- `overflow-x: clip` plutôt que `hidden` sur le corps du document : le
  débordement latéral est retenu de la même façon, mais le corps ne devient
  pas une zone de défilement, ce qui préserve le comportement des éléments
  collés à l’écran. Repli en `hidden` là où `clip` n’existe pas.
- Le planning du Diagnostic (`.planning`) : un fil horizontal porte quatre
  moments datés ; sous 900 px le fil se redresse en colonne. C’est une liste
  ordonnée, lisible sans la moindre feuille de style.
- Les verdicts portent un cachet tracé à l’apparition, retracé au survol.
  Purement ornemental : le nom du verdict et son explication sont écrits
  juste en dessous. Neutralisé sous `prefers-reduced-motion`.
- Le repère de la page ouverte, dans le menu de tête comme dans le menu
  déroulant, est en lavande sombre : la même couleur que le filet qui se
  déroule au survol.
- Les liens du pied de page se tiennent comme ceux du menu de tête : pas de
  trait permanent, un filet lavande qui se déroule au survol et au focus.
- Le formulaire de contact : chaque champ porte un pictogramme dans sa marge
  gauche, deux champs courts tiennent sur une ligne (`.form__duo`), et le
  champ visé prend un halo lavande. Les messages d’erreur s’écrivent sous
  leur champ (`.field__erreur`), jamais avant que le champ ait été quitté ou
  l’envoi tenté. Sans JavaScript, le navigateur affiche ses propres bulles :
  c’est le script qui pose `novalidate`, jamais le HTML. En fenêtre, le titre
  et le bloc d’envoi restent en place et seuls les champs défilent.
- `.prix` : le bloc de tarification d’un accompagnement. Un surtitre rouille,
  le montant en Source Serif, ce qu’il couvre, puis le premier pas offert
  détaché par un filet. `.prix--attente` sert aux formats dont le périmètre
  n’est pas arrêté : il n’affiche aucun montant.
- Les diapositives des accompagnements glissent en changeant : le format
  sortant part du côté opposé à la lecture, l’entrant arrive de l’autre. Le
  script pose `--diapo-sens` (1 ou -1) et coupe brièvement la transition le
  temps de reposer le format caché du bon côté, sans quoi il traverserait
  tout le bloc. Neutralisé sous `prefers-reduced-motion`.
- La frise chronologique de `a-propos` se fond : le fil est estompé à ses deux
  extrémités par un masque en dégradé, sa progression démarre en fondu, et le
  coussin des libellés prend la couleur du fond qu’il traverse. Les libellés
  n’apparaissent qu’une fois le fil posé (`.est-pose`), pour qu’un premier
  calcul fait sur une mise en page mouvante ne les laisse pas en haut de page.
- `data-defilement="<millisecondes>"` sur un carrousel : la piste avance
  toute seule et revient au début une fois arrivée au bout. Le script ajoute
  alors une commande de pause visible, atteignable au clavier, à la suite des
  chevrons. Le défilement s’interrompt au survol et au focus **dans la
  piste** (pas sur les commandes, sinon il ne repartirait jamais), quand le
  bloc sort de l’écran et quand l’onglet passe à l’arrière-plan. Il ne
  démarre pas du tout sous `prefers-reduced-motion`, et pas non plus quand la
  piste ne déborde pas. Aujourd’hui : la page `temoignages.html`, à 7 s.

### Icônes

Chevrons et pictogrammes **vectoriels monochromes**, dessinés dans le HTML.
Aucun émoji, aucune flèche Unicode, aucune bibliothèque d’icônes.

## Animations

Le mouvement explique le rythme de lecture ; il ne distrait pas et ne porte
jamais d’information seule.

| Effet | Où |
|---|---|
| Apparition au défilement (`.reveal`) | Partout |
| Ken Burns lent | Bandeaux de tête |
| Parallaxe très légère | Visuels marqués `data-parallax` |
| Zoom au survol | Cadres `.frame--zoom` |
| Voile lumineux | Cadres `.frame--sheen` |
| Filet qui se dessine | Cadres `.frame--underline` |
| Bandeau des témoignages | Section Témoignages |
| Réservation en deux temps | Bloc « Parlons de… » |
| Parcours : trajet tracé et avion qui le suit | `a-propos.html` |
| Fil de lecture vertical | `a-propos.html` |
| Les cinq étapes qui défilent, onglets et curseur glissant | `approche.html` |
| Couloir de photographies en perspective | `a-propos.html` |
| Chiffres : pictogrammes, décompte, réaction au survol | `index.html`, `a-propos.html` |
| Vidéos en boucle, muettes | Bandeaux équipés |

### Règles non négociables

1. **`prefers-reduced-motion`** neutralise toutes les animations. Les vidéos
   ne sont alors pas chargées.
2. **Sans JavaScript**, tout le contenu est visible et navigable : les
   apparitions ne sont armées que si le script s’exécute (`html.js`).
3. Toute animation en boucle a une **commande d’arrêt** visible et au clavier.
4. Aucune information n’existe uniquement dans une animation ou une image :
   la carte du parcours et le schéma doublent des textes présents à côté.
