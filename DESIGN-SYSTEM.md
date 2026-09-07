# Design system — Amélie & Partners

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

La lavande claire `#cbb5df` ne sert de couleur de texte **que sur fond bleu
nuit** (surtitres, libellés). Sur ivoire, elle est réservée aux filets, aux
fonds et aux repères.

Le rapport le plus juste du site est la rouille sur ivoire secondaire
(4,71:1) : il tient pour du texte courant, mais ne descendez pas cette
couleur plus bas et ne l’employez pas sous 14 px.

## La marque

Le logo est un **entrelacs de boucles** : chaque boucle part du centre, se
déploie vers l’extérieur et revient en se croisant elle-même, si bien que les
brins de boucles voisines se chevauchent et forment un nœud à claire-voie.

Sa construction est **paramétrée par le nombre de boucles**. Quatre boucles
pour la marque elle-même ; autant de boucles que d’étapes lorsqu’elle sert de
repère dans un schéma. Sur `approche.html`, les quatre boucles correspondent
aux quatre étapes et se dessinent l’une après l’autre, au rythme des étapes
qu’elles représentent.

| Où | Boucles | Comportement |
|---|---|---|
| En-tête et pied de page | 4 | Statique, à côté du nom |
| Onglet du navigateur (`favicon.svg`) | 4 | Statique, lavande sur bleu nuit |
| Schéma de `approche.html` | 4 | Chaque boucle se dessine avec son étape |
| Fichier autonome (`assets/images/logo.svg`) | 4 | Lavande sombre sur fond transparent |

Le tracé actuel est une **reconstruction** en SVG. Si le fichier source
officiel du logo existe, il remplace avantageusement `assets/images/logo.svg`
et les tracés inscrits dans les pages — voir `GUIDE-VISUELS.md`.

Pour produire une variante à un autre nombre de boucles :

```bash
python3 outils/marque.py 5      # affiche le SVG d'une marque à cinq boucles
```

## Typographie

- **Source Serif 4** — grands titres uniquement (`h1` à `h4`, `.pull`).
- **Inter** — corps de texte, cartes, boutons, témoignages, navigation.
- **Caveat** — exception unique et volontaire : la note manuscrite de la
  fondatrice et sa signature, sur `a-propos.html`. Jamais un titre, jamais un
  bouton, jamais un contenu informatif.

Pas d’italique décoratif. Les polices sont locales (`assets/fonts/`), sous
licence SIL OFL 1.1 (`assets/fonts/OFL.txt`) : aucun appel à un service de
polices externe, donc aucun traceur tiers de ce fait.

### Échelle

| Usage | Variable | Valeur |
|---|---|---|
| Titre de premier écran | `--type-display` | `clamp(2.25rem, 4.6vw, 4.25rem)` |
| Titre de section | `--type-title` | `clamp(2rem, 3.6vw, 3.125rem)` |
| Sous-titre | `--type-heading` | `clamp(1.5rem, 2.4vw, 2.125rem)` |
| Titre de carte | `--type-card` | `clamp(1.1875rem, 1.8vw, 1.4375rem)` |
| Corps | — | `1.0625rem`, interligne 1,65 |
| Surtitre (`.eyebrow`) | — | `0.75rem`, majuscules, interlettrage `.16em` |

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
parcours (27), schéma des quatre étapes (28).

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
| Tracé et étapes du parcours | `a-propos.html` |
| Fil de lecture vertical | `a-propos.html` |
| Trait et étapes du schéma | `approche.html` |
| Vidéos en boucle, muettes | Bandeaux équipés |

### Règles non négociables

1. **`prefers-reduced-motion`** neutralise toutes les animations. Les vidéos
   ne sont alors pas chargées.
2. **Sans JavaScript**, tout le contenu est visible et navigable : les
   apparitions ne sont armées que si le script s’exécute (`html.js`).
3. Toute animation en boucle a une **commande d’arrêt** visible et au clavier.
4. Aucune information n’existe uniquement dans une animation ou une image :
   la carte du parcours et le schéma doublent des textes présents à côté.
