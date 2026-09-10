# -*- coding: utf-8 -*-
"""Fabrique une page traduite a partir de la page francaise publiee.

Le principe, explique dans `inventaire.py` : on ne reecrit pas les gabarits.
On prend la page francaise telle qu'elle est en ligne, on lui remet une
coquille dans la langue voulue — en-tete, pied de page, balises de tete, tous
produits par `coquille.py`, deja verifies — et on traduit le corps chaine par
chaine, a partir d'un dictionnaire.

Deux garde-fous :

1. **Rien ne peut rester en francais par oubli.** Toute chaine visible absente
   du dictionnaire est signalee, et le fichier n'est pas ecrit.
2. **Le balisage n'est jamais reecrit.** On ne remplace que le texte entre
   deux balises et le contenu des attributs qui portent du texte lu. La
   structure, les classes, les liens et les scripts sortent intacts.
"""
import os
import re
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
# `outils/traduction/` → la racine du site est deux crans au-dessus.
RACINE = os.path.dirname(os.path.dirname(ICI))
sys.path.insert(0, ICI)

import coquille
from inventaire import ZONES_MUETTES, COMMENTAIRES, TEXTE, ATTRIBUTS, _garder

# Ce que le corps ne doit pas contenir : ni le francais des coquilles, ni les
# citations, qui restent en francais par choix (voir CLAUDE.md).
MASQUES = (ZONES_MUETTES, COMMENTAIRES)


def _traduire_segment(seg, mot, manquants):
    """`mot` rend la forme a ecrire, ou leve l'oubli. Voir `Glossaire`."""

    def texte(m):
        brut = m.group(1)
        if not _garder(brut):
            return m.group(0)
        remplace = mot(brut.strip(), balise=True, manquants=manquants)
        if remplace is None:
            return m.group(0)
        avant = brut[:len(brut) - len(brut.lstrip())]
        apres = brut[len(brut.rstrip()):]
        return ">" + avant + remplace + apres + "<"

    def attribut(m):
        nom, brut = m.group(1), m.group(2)
        if not _garder(brut):
            return m.group(0)
        # Un attribut ne peut pas porter de balise : la citation gardee en
        # francais y reste telle quelle, sans son `lang`.
        remplace = mot(brut.strip(), balise=False, manquants=manquants)
        if remplace is None:
            return m.group(0)
        return f'{nom}="{remplace}"'

    return ATTRIBUTS.sub(attribut, TEXTE.sub(texte, seg))


class Glossaire:
    """Le dictionnaire d'une page, et ce qu'il faut faire de chaque chaine.

    Trois sorts possibles, et un seul par chaine :

    - **traduite** : elle figure dans `dico` ;
    - **citee** : c'est la parole de quelqu'un, elle reste en francais et on
      la signale par un `lang="fr"` pour que les lecteurs d'ecran changent
      de voix ;
    - **inchangee** : un nom propre, un montant — rien a traduire.

    Tout le reste est un oubli, et un oubli arrete la fabrication.
    """

    def __init__(self, lang, dico, citations=(), inchange=()):
        self.lang = lang
        self.dico = dico
        self.citations = frozenset(citations)
        self.inchange = frozenset(inchange)

    def __call__(self, cle, balise, manquants):
        if cle in self.dico:
            return self.dico[cle]
        if cle in self.inchange:
            return cle
        if cle in self.citations:
            if balise and self.lang != "fr":
                return f'<span lang="fr">{cle}</span>'
            return cle
        manquants.append(cle)
        return None


# Ce qui remplace une zone mise de cote, avant la traduction.
#
# Un chevron ouvre et ferme ce jeton, et c'est essentiel : le texte se releve
# entre deux balises, et un dessin pose au milieu d'une phrase — le chevron
# d'un `<summary>`, par exemple — couperait cette phrase en deux si on le
# retirait purement et simplement. Le jeton tient sa place.
JETON = "<!--\x00%d\x00-->"
RETOUR = re.compile(r"<!--\x00(\d+)\x00-->")


def traduire_corps(html, mot, manquants):
    """Traduit le texte visible, en laissant le code et les dessins de cote."""
    zones = sorted(
        [m.span() for masque in MASQUES for m in masque.finditer(html)])
    morceaux, gardes, pos = [], [], 0
    for debut, fin in zones:
        if debut < pos:
            continue
        morceaux.append(html[pos:debut])
        morceaux.append(JETON % len(gardes))
        gardes.append(html[debut:fin])
        pos = fin
    morceaux.append(html[pos:])
    traduit = _traduire_segment("".join(morceaux), mot, manquants)
    return RETOUR.sub(lambda m: gardes[int(m.group(1))], traduit)


# ---------------------------------------------------------------------------
# Deux precautions avant de traduire.
# ---------------------------------------------------------------------------

OPTION = re.compile(r"(?is)<option(?![^>]*\bvalue=)([^>]*)>(.*?)</option>")


def epingler_valeurs(html):
    """Fige la valeur envoyee par les listes deroulantes.

    Sans attribut `value`, un `<option>` envoie au serveur le texte qu'il
    affiche. Traduire ce texte changerait donc la valeur postee, que
    `api/contact.js` compare a une liste fermee : la reponse serait
    silencieusement remplacee par « Autre ». On epingle donc la valeur
    francaise avant de traduire l'etiquette. Le visiteur lit sa langue, le
    serveur recoit ce qu'il attend, et le message qui arrive chez Amelie
    garde le meme vocabulaire quelle que soit la langue du visiteur.
    """
    return OPTION.sub(
        lambda m: f'<option value="{m.group(2).strip()}"{m.group(1)}>{m.group(2)}</option>',
        html)


LIEN_LEGAL = re.compile(
    r'(href=")(?!/)((?:mentions-legales|confidentialite|cgv)\.html)')


def renvoyer_legal(html, lang):
    """Fait pointer les liens legaux du corps vers la racine.

    Les pages legales n'existent qu'en francais. Depuis `/en/contact.html`,
    un lien ecrit `cgv.html` chercherait `/en/cgv.html`, qui n'existe pas :
    on le ramene donc a `/cgv.html`. La coquille le fait deja de son cote,
    par `langues.lien()` ; ceci vaut pour les liens ecrits dans le texte.

    L'etiquette du lien, elle, dit dans quelle langue est la page visee :
    c'est le dictionnaire de la page qui s'en charge.
    """
    if lang == "fr":
        return html
    return LIEN_LEGAL.sub(lambda m: m.group(1) + "/" + m.group(2), html)


RETOUR_SANS_JS = re.compile(
    r'(<input type="hidden" name="retour" value=")([^"]*)(")')


def prefixer_retour(html, lang):
    """Renvoie le visiteur sans JavaScript sur la page de *sa* langue."""
    if lang == "fr":
        return html
    return RETOUR_SANS_JS.sub(
        lambda m: m.group(1) + lang + "/" + m.group(2) + m.group(3), html)


# ---------------------------------------------------------------------------
# Decoupe de la page francaise : coquille de tete, en-tete, corps, pied.
# ---------------------------------------------------------------------------

FIN_TETE = re.compile(r'<a class="skip" href="#contenu">[^<]*</a>\n')
DEBUT_HEADER = '<header class="header" data-header>'
FIN_HEADER = "</header>\n"
DEBUT_PIED = '<footer class="footer">'


def decouper(html):
    m = FIN_TETE.search(html)
    if not m:
        raise SystemExit("lien d'evitement introuvable : page inattendue")
    i = html.index(DEBUT_HEADER, m.end())
    j = html.index(FIN_HEADER, i) + len(FIN_HEADER)
    k = html.index(DEBUT_PIED, j)
    return html[:m.end()], html[i:j], html[j:k], html[k:]


TITRE = re.compile(r"<title>(.*?)</title>", re.S)
DESCRIPTION = re.compile(r'<meta name="description" content="([^"]*)">')
IMAGE = re.compile(r'<meta property="og:image" content="[^"]*?(/assets/[^"]*)">')


def fabriquer(page, lang, glossaire, titre, description):
    """Ecrit `<lang>/<page>` a partir de `<page>`. Rend la liste des oublis."""
    source = os.path.join(RACINE, page)
    html = open(source, encoding="utf-8").read()
    tete_fr, _header_fr, corps_fr, _pied_fr = decouper(html)

    image = IMAGE.search(tete_fr)
    manquants = []
    corps_fr = renvoyer_legal(
        prefixer_retour(epingler_valeurs(corps_fr), lang), lang)
    corps = traduire_corps(corps_fr, glossaire, manquants)
    if manquants:
        return manquants

    tete = coquille.head(titre, description, page,
                      image.group(1) if image else "/assets/images/og-image.jpg",
                      lang=lang)
    entete = coquille.header(active=page, lang=lang)
    pied = coquille.footer(lang=lang)

    dossier = os.path.join(RACINE, lang)
    os.makedirs(dossier, exist_ok=True)
    with open(os.path.join(dossier, page), "w", encoding="utf-8") as f:
        f.write(tete + entete + corps + pied)
    return []


def inventorier_corps(page):
    """Les chaines du corps seul : la coquille est traduite ailleurs."""
    from inventaire import relever
    html = open(os.path.join(RACINE, page), encoding="utf-8").read()
    _, _, corps, _ = decouper(html)
    return relever(corps)
