#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Fabrique les pages d'une langue à partir des pages françaises publiées.

    python3 outils/traduire-site.py en

À lancer **après** les gabarits et après les deux outils qui les retouchent,
jamais avant : une page traduite descend de la page française telle qu'elle
est publiée.

    build_a … build_g              les pages françaises
    outils/donnees-structurees.py
    outils/dimensions-images.py
    outils/traduire-site.py en     les pages anglaises
    outils/plan-du-site.py         le plan du site
    outils/verifier-site.py        le contrôle

Le script refuse d'écrire une page dont une seule chaîne visible manquerait
au dictionnaire, et il les nomme. Aucune phrase ne peut donc rester en
français par oubli, et une retouche du texte français se voit ici tout de
suite.

Les trois pages légales ne sont pas traduites : le droit applicable est le
droit français. Les pages traduites y renvoient en le disant.
"""
import os
import sys

ICI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(ICI, "traduction"))
sys.path.insert(0, os.path.join(ICI, "traduction", "dictionnaires"))

import traduire

# Un dictionnaire par langue : la page d'accueil a le sien, les autres pages
# sont regroupées. Chaque entrée dit ce qu'il faut faire de chaque chaîne —
# la traduire, la garder comme citation, ou la laisser telle quelle.
def glossaires(lang):
    if lang == "en":
        import en_accueil, en_pages, en_titres
        tables = {"index.html": (en_accueil.EN, en_accueil.CITATIONS,
                                 en_accueil.INCHANGE)}
        for page, dico in en_pages.PAGES.items():
            tables[page] = (dico,
                            en_pages.CITATIONS.get(page, set()),
                            en_pages.INCHANGE.get(page, set()))
        return tables, en_titres.TITRES
    raise SystemExit(f"aucun dictionnaire pour « {lang} ». "
                     "Voir outils/traduction/dictionnaires/.")


def main(lang):
    tables, titres = glossaires(lang)
    echecs = 0
    for page in sorted(tables):
        dico, citations, inchange = tables[page]
        titre, description = titres[page]
        oublis = traduire.fabriquer(
            page, lang, traduire.Glossaire(lang, dico, citations, inchange),
            titre, description)
        if oublis:
            echecs += 1
            print(f"{lang}/{page} : NON ÉCRITE, "
                  f"{len(oublis)} chaîne(s) sans traduction")
            for t in oublis:
                print("   ", t[:100])
        else:
            taille = os.path.getsize(os.path.join(traduire.RACINE, lang, page))
            print(f"écrit : {lang}/{page} {taille} octets")
    if echecs:
        print(f"\n{echecs} page(s) non écrite(s).")
        return 1
    print(f"\n{len(tables)} page(s) en « {lang} ».")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else "en"))
