# Amélie & Partners · site amelie-invest.com

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

Le site est publié sur **Vercel** : il sert les pages statiques et exécute
la seule fonction serveur du projet, `api/contact.js`, qui reçoit le
formulaire de contact. Un hébergeur strictement statique conviendrait pour
les pages, mais le formulaire n’enverrait alors rien.

Points à régler côté hébergeur :

- pointer le domaine `amelie-invest.com` sur le projet ;
- forcer HTTPS et rediriger `www` vers le domaine sans `www` ;
- déclarer `404.html` comme page d’erreur ;
- renseigner `RESEND_API_KEY` dans les variables d’environnement du projet,
  sans quoi le formulaire répond une erreur — voir
  `INSTALLATION-FORMULAIRE.md` ;
- envoyer `https://amelie-invest.com/sitemap.xml` à Google Search Console.

## Arborescence

```
index.html                 Accueil
approche.html              Notre approche (récapitulatif des 5 étapes)
accompagnements.html       Les quatre accompagnements
diagnostic.html            Diagnostic Stratégique · 432 € TTC
ressources.html            La bibliothèque
ressource-3-effets.html    Ressource « Les 3 effets dans l’immobilier »
temoignages.html           Les huit témoignages, en pile de cartes
a-propos.html              La fondatrice, la carte postale du parcours, le fil de lecture
contact.html               Réserver un créneau ou passer au formulaire
formulaire.html            Le formulaire de contact, sur sa propre page
mentions-legales.html      Modèle à compléter
confidentialite.html       Modèle à compléter
cgv.html                   Conditions générales de vente
404.html                   Page introuvable

en/                        Les mêmes pages en anglais, sauf les pages légales

assets/css/styles.css      Toute la mise en forme, commentée et numérotée
assets/css/fonts.css       Déclaration des polices locales
assets/js/site.js          Menu, apparitions, témoignages, vidéos, fil, schéma
assets/fonts/              Inter, Source Serif 4, Caveat + licences OFL
assets/images/             Photographies et logo, voir GUIDE-VISUELS.md
assets/videos/             Vidéos d’ambiance (à déposer, voir le LISEZ-MOI)

outils/verifier-site.py    Vérifie liens, ancres, ressources, invariants
outils/donnees-structurees.py  Régénère le JSON-LD de l’accueil et du diagnostic
outils/dimensions-images.py    Recale width et height sur les fichiers réels
outils/plan-du-site.py         Réécrit sitemap.xml à partir des pages présentes
outils/traduire-site.py        Fabrique les pages d’une langue depuis le français
outils/traduction/             La machinerie des traductions, voir son LISEZ-MOI

DESIGN-SYSTEM.md           Couleurs, typographie, composants, animations
GUIDE-VISUELS.md           Chaque emplacement d’image et de vidéo
A-VALIDER-AVANT-LIVE.md    Ce qu’Amélie doit confirmer avant publication
CLAUDE.md                  Instructions permanentes pour toute reprise
```

## Modifier un texte

Les textes sont directement dans les fichiers `.html`. L’en-tête et le pied de
page sont répétés dans chaque page : une modification de navigation doit être
reportée dans les quatorze fichiers, puis dans chaque dossier de langue. Les
caractères accentués sont écrits en clair ; les apostrophes typographiques
utilisent `&rsquo;`.

## Les langues

Le français est à la racine ; l’anglais dans `en/`. Les liens entre pages
sont **relatifs**, ce qui fait qu’une page anglaise mène à une page anglaise ;
les fichiers du site s’appellent en **absolu** (`/assets/…`) et servent à
toutes les langues. Le sélecteur de langue, en drapeaux, est une simple liste
de liens : il fonctionne sans JavaScript.

Trois choses ne se traduisent pas. Les **pages légales**, parce que le droit
applicable est le droit français : les pages anglaises y renvoient en le
disant. Les **citations des témoignages**, parce que ce sont les mots de
personnes réelles ; elles portent un `lang="fr"` pour que les lecteurs
d’écran changent de voix, et tout ce qui les entoure est traduit. Le **prix**,
enfin : la prestation est vendue et facturée en France, sous TVA française,
donc la page anglaise écrit 432 € et traduit « TTC » par « incl. French VAT »
sans rien convertir.

L’anglais est fabriqué à partir du français publié : la page anglaise
vieillit dès que la page française change. Après toute retouche du français,
il faut refabriquer les traductions.

## Vérifier avant de publier

```bash
python3 outils/verifier-site.py
```

Le script contrôle les liens internes, les ancres, les ressources
référencées, les titres, les descriptions, les attributs `alt`, la présence
des huit témoignages et de la mention sur la variabilité des résultats. Il
lit aussi les dossiers de langue, et y résout les liens relatifs depuis la
page qui les écrit.

## Ce qui n’est pas encore décidé

Voir `A-VALIDER-AVANT-LIVE.md`. Les mentions légales et la politique de
confidentialité sont des modèles de travail à faire relire par un
professionnel du droit.
