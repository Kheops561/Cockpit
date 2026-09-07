# Amélie & Partners — site amelie-invest.com

Site statique, en français, pour un cabinet de conseil en stratégie
d’investissement immobilier.

Aucune compilation, aucun gestionnaire de paquets, aucune dépendance
externe : ce sont des fichiers HTML, une feuille de styles, un script et des
médias. Polices comprises, tout est hébergé avec le site.

## Ouvrir le site

Double-cliquer sur `index.html` suffit pour lire les pages. Pour que tout se
comporte comme en ligne (chemins, polices, vidéos), servir le dossier :

```bash
python3 -m http.server 8000
# puis ouvrir http://localhost:8000
```

## Mettre en ligne

Le contenu du dossier est le site : il se dépose tel quel chez n’importe quel
hébergeur statique (Netlify, Vercel, Cloudflare Pages, OVH, o2switch…).
Points à régler côté hébergeur :

- pointer le domaine `amelie-invest.com` sur la racine du dossier ;
- forcer HTTPS et rediriger `www` vers le domaine sans `www` ;
- déclarer `404.html` comme page d’erreur ;
- envoyer `https://amelie-invest.com/sitemap.xml` à Google Search Console.

## Arborescence

```
index.html                 Accueil
approche.html              Notre approche (schéma des 4 étapes + méthode)
accompagnements.html       Les quatre accompagnements
diagnostic.html            Diagnostic Stratégique — 450 € HT
ressources.html            La bibliothèque
ressource-3-effets.html    Ressource « Les 3 effets dans l’immobilier »
a-propos.html              La fondatrice, la carte du parcours, le fil de lecture
contact.html               Réserver ou écrire
mentions-legales.html      Modèle à compléter
confidentialite.html       Modèle à compléter
404.html                   Page introuvable

assets/css/styles.css      Toute la mise en forme, commentée et numérotée
assets/css/fonts.css       Déclaration des polices locales
assets/js/site.js          Menu, apparitions, témoignages, vidéos, fil, schéma
assets/fonts/              Inter, Source Serif 4, Caveat + licences OFL
assets/images/             Photographies et logo — voir GUIDE-VISUELS.md
assets/videos/             Vidéos d’ambiance (à déposer — voir le LISEZ-MOI)

outils/verifier-site.py    Vérifie liens, ancres, ressources, invariants
outils/donnees-structurees.py  Régénère le JSON-LD de l’accueil et du diagnostic
outils/dimensions-images.py    Recale width et height sur les fichiers réels

DESIGN-SYSTEM.md           Couleurs, typographie, composants, animations
GUIDE-VISUELS.md           Chaque emplacement d’image et de vidéo
A-VALIDER-AVANT-LIVE.md    Ce qu’Amélie doit confirmer avant publication
CLAUDE.md                  Instructions permanentes pour toute reprise
```

## Modifier un texte

Les textes sont directement dans les fichiers `.html`. L’en-tête et le pied de
page sont répétés dans chaque page : une modification de navigation doit être
reportée dans les onze fichiers. Les caractères accentués sont écrits en
clair ; les apostrophes typographiques utilisent `&rsquo;`.

## Vérifier avant de publier

```bash
python3 outils/verifier-site.py
```

Le script contrôle les liens internes, les ancres, les ressources
référencées, les titres, les descriptions, les attributs `alt`, la présence
des huit témoignages et de la mention sur la variabilité des résultats.

## Ce qui n’est pas encore décidé

Voir `A-VALIDER-AVANT-LIVE.md`. Les mentions légales et la politique de
confidentialité sont des modèles de travail à faire relire par un
professionnel du droit.
