# -*- coding: utf-8 -*-
"""Relève tout ce qu'une page montre, tel qu'écrit dans la source.

Le principe du chantier : plutôt que de réécrire les gabarits — deux mille
sept cents lignes où le français est en dur, et où j'ai déjà cassé trois
choses en les touchant —, on lit la page française produite et on remplace
chaque chaîne visible par sa traduction, prise dans un dictionnaire.

Les chaînes sont relevées **telles qu'elles apparaissent dans la source**,
entités HTML comprises : le remplacement est alors une substitution exacte,
sans passer par une réécriture du document.

L'intérêt est le contrôle : toute chaîne absente du dictionnaire est
signalée. Aucune phrase ne peut rester en français par oubli.
"""
import html as _html
import re

# Les zones qu'on ne lit pas : du code, ou du dessin.
ZONES_MUETTES = re.compile(r"(?is)<(script|style|svg)\b.*?</\1>")
COMMENTAIRES = re.compile(r"(?s)<!--.*?-->")

# Le texte entre deux balises.
TEXTE = re.compile(r">([^<>]+)<")
# Les attributs qui portent du texte lu par quelqu'un.
ATTRIBUTS = re.compile(
    r'\b(alt|aria-label|placeholder|title|data-manque|data-court|data-format'
    r'|data-label-pause|data-label-play)="([^"]*)"')

# Ni le code, ni les noms propres.
INVARIANTS = {
    "Amélie &amp; Partners", "Amélie-Thu DUONG", "Diagnostic Stratégique",
    "LinkedIn", "Paris", "France", "Amélie", "Partners",
    "Investir avec méthode", "Décider avec clarté", "Calendly",
}


def _garder(t):
    t = t.strip()
    if not t or t in INVARIANTS:
        return None
    # Une chaîne sans lettre — un nombre, un tiret, une puce — ne se traduit
    # pas. Le test se fait sur le texte réellement lu : sans cela, les lettres
    # du nom d'une entité (`&gt;`, `&nbsp;`) feraient passer « > 35 » pour une
    # phrase à traduire.
    if not re.search(r"[A-Za-zÀ-ÿ]", _html.unescape(t)):
        return None
    return t


def relever(html):
    """Les chaînes visibles, dans l'ordre où elles apparaissent."""
    net = COMMENTAIRES.sub(" ", ZONES_MUETTES.sub(" ", html))
    vues, sortie = set(), []
    for m in TEXTE.finditer(net):
        t = _garder(m.group(1))
        if t and t not in vues:
            vues.add(t)
            sortie.append(t)
    for m in ATTRIBUTS.finditer(net):
        t = _garder(m.group(2))
        if t and t not in vues:
            vues.add(t)
            sortie.append(t)
    return sortie
