# Les pages traduites

Le site est écrit en français. Les autres langues n’en sont pas des copies
tenues à part : elles sont **fabriquées à partir de la page française
publiée**. C’est le seul moyen de garantir qu’une retouche du français ne
laisse pas derrière elle une page anglaise périmée sans que personne ne s’en
aperçoive.

## Comment une page anglaise est faite

On prend `contact.html`, on la coupe en quatre — les balises de tête,
l’en-tête, le corps, le pied de page —, on refait les trois morceaux de
coquille dans la langue voulue, et on traduit le corps chaîne par chaîne à
partir d’un dictionnaire. Le balisage n’est jamais réécrit : on ne remplace
que le texte entre deux balises et le contenu des attributs qui portent du
texte lu. La structure, les classes, les liens et les scripts sortent
intacts.

**Une chaîne absente du dictionnaire arrête la fabrication**, et le script la
nomme. C’est le garde-fou principal : aucune phrase ne peut rester en
français par oubli, et une phrase française modifiée se signale d’elle-même
à la traduction suivante.

## Lancer

```bash
python3 outils/traduire-site.py en
python3 outils/traduire-site.py vi
```

Toujours **après** les gabarits et après `donnees-structurees.py` et
`dimensions-images.py`, jamais avant. Puis `plan-du-site.py`, puis
`verifier-site.py`.

## Les fichiers

```
langues.py          Les langues, leurs drapeaux, et les textes de la coquille
coquille.py         Tête, en-tête, pied de page, icônes, drapeaux
inventaire.py       Relève les chaînes visibles d’une page
traduire.py         Découpe, traduit, réassemble
controle_langue.py  Relit une page produite et signale ce qui semble français
dictionnaires/      Un fichier par langue et par page
```

`verifier-site.py` appelle `controle_langue.py` tout seul sur les pages des
dossiers de langue : le contrôle est donc dans la vérification habituelle,
il n’y a rien de plus à lancer.

## Les polices

Le vietnamien a besoin de deux fichiers que les autres langues n’utilisent
pas : `inter-vietnamese.woff2` et `source-serif-4-vietnamese.woff2`. Le
sous-jeu « latin étendu » s’arrête avant `U+1EA0`, et c’est là que vivent la
plupart des lettres à ton. Chaque fichier est déclaré avec sa propre plage :
le navigateur ne le charge que s’il rencontre ces caractères, et les pages
vietnamiennes le préchargent.

**Caveat n’existe pas en vietnamien.** La carte postale de « À propos »
emploie donc le serif du site sur ces pages, par la section 48 de
`styles.css`. Les deux autres emplois de Caveat sont les mots d’Amélie : ils
restent en français, donc en Caveat.

## Trois choses ne se traduisent pas

**Les pages légales.** Le droit applicable est le droit français. Les
traduire approximativement engagerait le cabinet. Les pages traduites y
renvoient en indiquant qu’elles sont en français, et le sélecteur de langue
ne s’affiche pas sur ces pages : il n’aurait nulle part où mener.

**Les citations des témoignages.** Ce sont les mots de personnes réelles.
Elles restent dans leur langue, marquées `lang="fr"` pour que les lecteurs
d’écran changent de voix ; tout ce qui les entoure — le chapeau, les
fonctions, la mention que les résultats varient — est traduit.

**Le prix.** La prestation est vendue et facturée en France, sous TVA
française : la page anglaise écrit `432 €` et traduit « TTC » par
« incl. French VAT ». Elle ne convertit rien.

À quoi s’ajoutent les noms propres : le cabinet, sa signature, les quatre
offres, les cinq verdicts, les lieux.

## Deux pièges déjà désamorcés

**Les listes déroulantes du formulaire.** Sans attribut `value`, une
`<option>` envoie au serveur le texte qu’elle affiche. Traduire l’étiquette
changerait donc la valeur postée, qu’`api/contact.js` compare à une liste
fermée : la réponse serait silencieusement remplacée par « Autre ».
`traduire.py` fige donc la valeur française avant de traduire l’étiquette.
Le visiteur lit sa langue, le serveur reçoit ce qu’il attend, et le message
qui arrive chez Amélie garde le même vocabulaire quelle que soit la langue
du visiteur.

**Le retour sans JavaScript.** Le champ caché `retour` porte le préfixe de
langue, et `api/contact.js` l’accepte après contrôle : un visiteur anglais
sans JavaScript revient sur la page anglaise. La fonction lui répond aussi
dans sa langue — elle la déduit de ce même champ, sans qu’il faille en
ajouter un.

## Ajouter une langue

1. Compléter `IDENTITE` et `TEXTES` dans `langues.py`, et dessiner le
   drapeau dans `coquille.py` s’il manque.
2. Écrire les dictionnaires dans `dictionnaires/`. Pour connaître les
   chaînes à traduire, `traduire.inventorier_corps("index.html")` les rend
   dans l’ordre de la page.
3. Ajouter la langue à `PUBLIEES` — **le jour où ses pages existent**, pas
   avant : le sélecteur et les `hreflang` ne montrent que celles-là, et
   annoncer une traduction absente donne une page introuvable au visiteur
   et une erreur aux moteurs.
4. Régénérer les pages françaises : c’est ce qui fait apparaître le nouveau
   drapeau dans leur sélecteur.
