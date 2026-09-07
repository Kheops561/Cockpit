# Guide des visuels

Tous les visuels actuellement en place sont **provisoires** : ce sont des
aplats abstraits aux couleurs de la marque, générés pour que le site soit
présentable immédiatement. Ils sont faits pour être remplacés.

## Comment remplacer une image

1. Préparer la photographie au format **JPEG**, aux dimensions indiquées dans
   le tableau ci-dessous (ou proportionnelles).
2. La nommer **exactement** comme le fichier existant.
3. La déposer dans `assets/images/`, en écrasant l’ancienne.

Rien d’autre à faire : aucun code à modifier. Les dimensions déclarées dans le
HTML servent à réserver la place pendant le chargement ; garder les mêmes
proportions évite que la page sursaute.

### Recommandations

- Poids : viser **moins de 300 Ko** par image, 500 Ko pour un bandeau.
- Cadrage : les bandeaux de tête reçoivent un voile bleu nuit assez dense sur
  la gauche, où se pose le texte. Choisir des images dont le sujet est plutôt
  à droite, et éviter les zones très claires à gauche.
- Style : photographie architecturale et éditoriale, lumière naturelle,
  cadrages calmes. Pas de photographie d’illustration générique.
- Droits : n’utiliser que des images dont l’usage commercial est acquis.

### Texte alternatif

Chaque image porte un attribut `alt`. Les images purement décoratives ont un
`alt` vide — c’est volontaire et correct. Si vous remplacez une image
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

| Fichier | Dimensions actuelles | Pages |
|---|---|---|
| `a-propos.mp4` | — | a-propos.html |
| `accompagnement-diagnostic.jpg` | 1320 × 880 | accompagnements.html, diagnostic.html, index.html |
| `accompagnement-financement.jpg` | 1320 × 880 | accompagnements.html, index.html |
| `accompagnement-recherche.jpg` | 1320 × 880 | accompagnements.html, index.html |
| `accompagnement-trajectoire.jpg` | 1320 × 880 | accompagnements.html, index.html |
| `accueil.mp4` | — | index.html |
| `approche-capital.jpg` | 1280 × 960 | approche.html, index.html |
| `approche-methode.jpg` | 1280 × 960 | approche.html, index.html |
| `approche-principes.jpg` | 1280 × 960 | a-propos.html |
| `cta-fond.jpg` | 1800 × 810 | a-propos.html, accompagnements.html, approche.html, index.html, particuliers.html, professionnels.html, ressource-3-effets.html, ressources.html |
| `hero-a-propos.jpg` | 1800 × 1013 | a-propos.html |
| `hero-accompagnements.jpg` | 1800 × 1013 | accompagnements.html |
| `hero-accueil.jpg` | 1800 × 1013 | index.html |
| `hero-approche.jpg` | 1800 × 1013 | approche.html |
| `hero-contact.jpg` | 1800 × 1013 | contact.html |
| `hero-diagnostic.jpg` | 1800 × 1013 | diagnostic.html |
| `hero-mentions.jpg` | 1800 × 810 | confidentialite.html, mentions-legales.html |
| `hero-particuliers.jpg` | 1800 × 1013 | particuliers.html |
| `hero-professionnels.jpg` | 1800 × 1013 | professionnels.html |
| `hero-ressources.jpg` | 1800 × 1013 | ressource-3-effets.html, ressources.html |
| `paris-01.jpg` | 840 × 1120 | a-propos.html, index.html |
| `paris-02.jpg` | 840 × 1120 | a-propos.html, index.html |
| `paris-03.jpg` | 840 × 1120 | a-propos.html, index.html |
| `paris-04.jpg` | 840 × 1120 | a-propos.html, index.html |
| `paris.mp4` | — | index.html |
| `particuliers-arbitrage.jpg` | 1280 × 960 | particuliers.html |
| `particuliers-locatif.jpg` | 1280 × 960 | particuliers.html |
| `particuliers-premier-achat.jpg` | 1280 × 960 | particuliers.html |
| `portrait-amelie-large.jpg` | 1200 × 1500 | a-propos.html |
| `portrait-amelie.jpg` | 1080 × 1350 | index.html |
| `professionnels-dirigeant.jpg` | 1280 × 960 | professionnels.html |
| `professionnels-murs.jpg` | 1280 × 960 | professionnels.html |
| `professionnels-structuration.jpg` | 1280 × 960 | professionnels.html |
| `public-particuliers.jpg` | 1080 × 1350 | index.html |
| `public-professionnels.jpg` | 1080 × 1350 | index.html |
| `ressource-3-effets.jpg` | 1500 × 844 | ressource-3-effets.html, ressources.html |
| `ressource-couverture.jpg` | 1500 × 844 | ressources.html |
Deux fichiers ne figurent pas dans ce tableau :

- `assets/images/og-image.jpg` (1200 × 630) — image affichée quand un lien du
  site est partagé sur les réseaux ou dans une messagerie. À remplacer par un
  visuel de marque dédié.
- `assets/images/favicon.svg` — icône de l’onglet du navigateur.

## Ce qui est le plus visible

Par ordre d’importance, si vous ne remplacez que quelques images :

1. `portrait-amelie.jpg` et `portrait-amelie-large.jpg` — le portrait de la
   fondatrice, présent dès le premier écran de l’accueil.
2. `hero-accueil.jpg` — le bandeau du premier écran.
3. `public-particuliers.jpg` et `public-professionnels.jpg` — les deux grandes
   cartes d’orientation de l’accueil.
4. `hero-particuliers.jpg`, `hero-professionnels.jpg`, `hero-diagnostic.jpg`.
5. `paris-01` à `paris-04.jpg` — la mosaïque et la galerie parisiennes.

## Regénérer des visuels provisoires

Le script qui a produit les aplats actuels est conservé dans
`outils/visuels-provisoires.py`. Il n’est utile que pour reconstituer des
images de remplacement ; il n’a rien à voir avec la publication.

```bash
python3 outils/visuels-provisoires.py
```

**Attention** : il écrase les fichiers de `assets/images/` portant les mêmes
noms. À ne pas lancer une fois les vraies photographies en place.
