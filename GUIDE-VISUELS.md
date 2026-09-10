# Guide des visuels

Les visuels en place sont les **photographies fournies par la marque**,
recadrées et compressées pour chaque emplacement. Le portrait de la
fondatrice, les vues parisiennes et le logo viennent tous du même jeu de
fichiers d’origine.

Chaque photographie sert à plusieurs endroits, sous des cadrages différents.
Le tableau plus bas dit lequel va où.

## Comment remplacer une image

1. Préparer la photographie au format **JPEG**, aux dimensions indiquées dans
   le tableau ci-dessous (ou proportionnelles).
2. La nommer **exactement** comme le fichier existant.
3. La déposer dans `assets/images/`, en écrasant l’ancienne.
4. Lancer `python3 outils/dimensions-images.py`, qui recale les attributs
   `width` et `height` du HTML sur le nouveau fichier.
5. Si le sujet de l’image change, corriger son texte alternatif dans les
   pages concernées.

L’étape 4 compte : ces attributs réservent la place de l’image pendant le
chargement. S’ils sont faux, la page sursaute sous les yeux du visiteur.

### Recommandations

- Poids : viser **moins de 200 Ko** par image. Les fichiers actuels tiennent
  tous sous ce seuil ; le premier écran de l’accueil pèse environ 330 Ko de
  photographies.
- Cadrage : les bandeaux de tête reçoivent un voile bleu nuit assez dense sur
  la gauche, où se pose le texte. Choisir des images dont le sujet est plutôt
  à droite, et éviter les zones très claires à gauche.
- Style : photographie architecturale et éditoriale, lumière naturelle,
  cadrages calmes. Pas de photographie d’illustration générique.
- Droits : n’utiliser que des images dont l’usage commercial est acquis.

### Texte alternatif

Chaque image porte un attribut `alt`. Les images purement décoratives ont un
`alt` vide, c’est volontaire et correct. Si vous remplacez une image
décorative par une image porteuse de sens, décrivez-la dans son `alt`.

## Vidéos

Les vidéos se déposent dans `assets/videos/` avec les noms exacts indiqués
plus bas. Voir aussi `assets/videos/LISEZ-MOI.txt`.

- MP4, codec H.264, **sans son** (les vidéos sont toujours muettes).
- 1920 × 1080 au maximum, 8 à 15 secondes, boucle propre.
- **Moins de 4 Mo** par fichier.

Si le fichier est absent ou illisible, ou si le visiteur a demandé moins
d’animation dans les réglages de son appareil, la photographie du même
emplacement reste affichée. Le site peut donc être publié avant que les
vidéos soient prêtes.

### Ajouter une vidéo sur un autre bandeau

Dans le `<div class="hero__media …">` de la page concernée, ajouter après
la balise `<img>` :

```html
<video class="hero__video" data-video muted loop playsinline preload="metadata"
       poster="assets/images/NOM-DE-LA-PHOTO.jpg"
       aria-label="Vidéo d’ambiance, sans son, en boucle." tabindex="-1">
  <source src="assets/videos/MA-VIDEO.mp4" type="video/mp4">
</video>
<button class="videobtn" type="button" data-video-toggle aria-pressed="false" hidden
        data-label-pause="Mettre la vidéo en pause" data-label-play="Reprendre la vidéo">
  <svg class="icon" width="12" height="12" viewBox="0 0 12 12" fill="none" aria-hidden="true" focusable="false"><path d="M4 2v8M8 2v8" stroke="currentColor" stroke-width="1.4" stroke-linecap="square"/></svg><span data-video-label>Mettre la vidéo en pause</span>
</button>
```

La commande de pause est obligatoire : une vidéo qui tourne en boucle doit
toujours pouvoir être arrêtée.

## Emplacements

| Fichier | Dimensions | Poids | Pages |
|---|---|---|---|
| `a-propos.mp4` | à venir | à venir | a-propos.html |
| `accompagnement-diagnostic.jpg` | 1320 × 880 | 205 Ko | accompagnements.html, index.html |
| `accompagnement-financement.jpg` | 1100 × 733 | 194 Ko | accompagnements.html, index.html |
| `accompagnement-recherche.jpg` | 1100 × 733 | 99 Ko | accompagnements.html, index.html |
| `accompagnement-trajectoire.jpg` | 1100 × 733 | 82 Ko | accompagnements.html, index.html |
| `approche-capital.jpg` | 1080 × 810 | 159 Ko | approche.html, index.html |
| `approche-methode.jpg` | 900 × 1125 | 230 Ko | approche.html, index.html |
| `approche-principes.jpg` | 1080 × 810 | 189 Ko | a-propos.html |
| `couloir-01.jpg` | 540 × 750 | 93 Ko | a-propos.html |
| `couloir-02.jpg` | 540 × 750 | 68 Ko | a-propos.html |
| `couloir-03.jpg` | 540 × 750 | 57 Ko | a-propos.html |
| `couloir-04.jpg` | 540 × 750 | 90 Ko | a-propos.html |
| `couloir-05.jpg` | 540 × 750 | 89 Ko | a-propos.html |
| `couloir-06.jpg` | 540 × 750 | 88 Ko | a-propos.html |
| `couloir-07.jpg` | 540 × 750 | 56 Ko | a-propos.html |
| `couloir-08.jpg` | 540 × 750 | 74 Ko | a-propos.html |
| `couloir-09.jpg` | 540 × 750 | 86 Ko | a-propos.html |
| `couloir-10.jpg` | 540 × 750 | 89 Ko | a-propos.html |
| `couloir-11.jpg` | 540 × 750 | 59 Ko | a-propos.html |
| `couloir-12.jpg` | 540 × 750 | 91 Ko | a-propos.html |
| `cta-fond.jpg` | 1600 × 720 | 133 Ko | a-propos.html, accompagnements.html, approche.html, index.html, ressource-3-effets.html, ressources.html, temoignages.html |
| `diagnostic-pour-qui.jpg` | 620 × 775 | 155 Ko | diagnostic.html |
| `feuillet-acheter.jpg` | 760 × 950 | 249 Ko | ressources.html |
| `feuillet-arbitrer.jpg` | 760 × 950 | 106 Ko | ressources.html |
| `feuillet-financer.jpg` | 760 × 950 | 83 Ko | ressources.html |
| `hero-a-propos.jpg` | 1600 × 900 | 171 Ko | a-propos.html |
| `hero-accompagnements.jpg` | 1600 × 900 | 316 Ko | accompagnements.html |
| `hero-accueil.jpg` | 1600 × 900 | 191 Ko | index.html |
| `hero-approche.jpg` | 1600 × 900 | 137 Ko | approche.html |
| `hero-contact.jpg` | 1600 × 900 | 109 Ko | contact.html, formulaire.html |
| `hero-diagnostic.jpg` | 1600 × 900 | 178 Ko | diagnostic.html |
| `hero-mentions.jpg` | 1600 × 720 | 145 Ko | cgv.html, confidentialite.html, mentions-legales.html |
| `hero-ressources.jpg` | 1600 × 900 | 198 Ko | ressource-3-effets.html, ressources.html |
| `hero-temoignages.jpg` | 1600 × 900 | 202 Ko | temoignages.html |
| `parcours-paris.jpg` | 620 × 775 | 146 Ko | a-propos.html |
| `parcours-vietnam.jpg` | 620 × 775 | 131 Ko | a-propos.html |
| `paris-01.jpg` | 660 × 880 | 82 Ko | index.html |
| `paris-02.jpg` | 660 × 880 | 76 Ko | formulaire.html, index.html |
| `paris-03.jpg` | 660 × 880 | 113 Ko | index.html |
| `paris-04.jpg` | 660 × 880 | 118 Ko | index.html |
| `paris.mp4` | à venir | à venir | index.html |
| `portrait-amelie-jardin.jpg` | 620 × 775 | 132 Ko | diagnostic.html |
| `portrait-amelie-large.jpg` | 960 × 1200 | 157 Ko | a-propos.html |
| `portrait-amelie.jpg` | 860 × 1075 | 138 Ko | index.html |
| `ressource-3-effets.jpg` | 1300 × 731 | 128 Ko | ressource-3-effets.html, ressources.html |
| `ressource-couverture.jpg` | 1300 × 731 | 128 Ko | ressources.html |
| `temoignages-vitrine.jpg` | 620 × 775 | 85 Ko | temoignages.html |

Trois fichiers ne figurent pas dans ce tableau :

- `assets/images/logo.png` : le logo de la marque, tel que fourni : trois
  boucles entrelacées en lavande, sur fond transparent.
- `assets/images/favicon.png` (180 × 180) : icône de l’onglet du navigateur :
  le logo sur le bleu nuit de la marque.
- `assets/images/og-image.jpg` (1200 × 630) : image affichée quand un lien du
  site est partagé sur les réseaux ou dans une messagerie : le bloc marine
  fourni avec le logo, recadré au format des réseaux.

## Le logo

Le logo est le **fichier fourni par la marque**, employé tel quel : un
entrelacs de trois boucles, en lavande, sur fond transparent. Il apparaît
deux fois par page (en-tête et pied de page), plus une fois sur
`approche.html`, à côté du schéma des quatre étapes.

La lavande se détache aussi bien sur l’ivoire que sur le bleu nuit : un seul
fichier suffit pour tous les contextes, sans variante de couleur.

Pour le remplacer, déposer le nouveau fichier sous le nom `logo.png` dans
`assets/images/`, puis lancer `python3 outils/dimensions-images.py`. Si vous
disposez d’une version vectorielle (`.svg`), elle sera plus nette sur les
écrans à forte densité et plus légère : dans ce cas, il faut aussi remplacer
`logo.png` par `logo.svg` dans les balises `<img class="mark…">` des pages.

Le fichier fourni sert de référence : `logo.png` est aussi la source de
`favicon.png`.

## Le couloir de photographies

La section « Paris, au quotidien » de `a-propos.html` fait remonter douze
vues parisiennes vers le lecteur, `couloir-01.jpg` à `couloir-12.jpg`. Elles
sont recadrées au rapport des cartes, 540 × 750, et tiennent chacune sous
95 Ko : le couloir en affiche vingt-quatre à la fois.

Pour en ajouter ou en retirer, modifier la liste passée à `couloir(...)` dans
la page. Le rail de gauche part six vues plus loin que celui de droite, de
sorte que les deux côtés ne montrent jamais la même image à la même
profondeur : gardez donc un nombre de vues au moins égal au nombre de cartes
par rail, sinon des répétitions apparaissent.

## Le parcours de la fondatrice

Le bloc « parcours » de `a-propos.html` accepte **une ou deux**
photographies. Avec une seule, elle occupe toute la largeur du cadre ; avec
deux, le bloc devient un diptyque Viêt Nam / Paris, en format portrait.

Les deux photographies sont en place : `parcours-paris.jpg`, la tour Eiffel
vue depuis la Seine, et `parcours-vietnam.jpg`, la tour de la Tortue sur le
lac Hoan Kiem. Elles sont recadrées en 620 × 775, centrées un peu au-dessus
du milieu pour garder le monument entier.

Deux drapeaux, France et Viêt Nam, marquent les extrémités du trajet dessiné
au centre. Ils sont vectoriels, écrits dans la page, et décoratifs : le nom du
lieu est écrit juste à côté. Ce sont les deux seules touches de couleur hors
palette du site.

## Ce qui est le plus visible

Par ordre d’importance, si vous ne changez que quelques images :

1. `portrait-amelie.jpg` : le portrait de la fondatrice, présent dès le
   premier écran de l’accueil.
2. `hero-accueil.jpg` : le bandeau du premier écran.
3. `hero-diagnostic.jpg` et `hero-accompagnements.jpg` : les deux pages qui
   mènent à la prise de rendez-vous.
4. `paris-01` à `paris-04.jpg` : la mosaïque et la galerie parisiennes.

## Après tout remplacement

```bash
python3 outils/dimensions-images.py   # recale width et height
python3 outils/verifier-site.py       # doit renvoyer « Aucune erreur »
```
