#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Recale les attributs width et height des images sur les fichiers réels.

Ces attributs servent au navigateur à réserver la place de l'image avant
qu'elle n'arrive : s'ils sont faux, la page sursaute pendant le chargement.
À relancer après tout remplacement de visuel dont les dimensions changent.

    python3 outils/dimensions-images.py
"""

import glob
import io
import os
import re
import sys

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

try:
    from PIL import Image
except ImportError:
    raise SystemExit("Pillow est nécessaire :  pip install Pillow")

BALISE = re.compile(r'<img\b[^>]*>', re.I)
SRC = re.compile(r'src="(assets/images/[^"]+)"')


def dimensions(rel, cache={}):
    if rel not in cache:
        chemin = os.path.join(RACINE, rel)
        cache[rel] = Image.open(chemin).size if os.path.exists(chemin) else None
    return cache[rel]


def corriger(balise):
    m = SRC.search(balise)
    if not m:
        return balise, False
    taille = dimensions(m.group(1))
    if not taille:
        return balise, False
    w, h = taille
    avant = balise
    if 'width="' in balise:
        balise = re.sub(r'width="\d+"', f'width="{w}"', balise)
    if 'height="' in balise:
        balise = re.sub(r'height="\d+"', f'height="{h}"', balise)
    return balise, balise != avant


def main():
    total = 0
    for page in sorted(glob.glob(os.path.join(RACINE, '*.html'))):
        s = io.open(page, encoding='utf-8').read()
        corrections = [0]

        def rempl(m):
            nouveau, change = corriger(m.group(0))
            if change:
                corrections[0] += 1
            return nouveau

        nouveau = BALISE.sub(rempl, s)
        if corrections[0]:
            io.open(page, 'w', encoding='utf-8').write(nouveau)
            print(f"{os.path.basename(page)} : {corrections[0]} image(s) recalée(s)")
            total += corrections[0]
    print(f"\n{total} correction(s)." if total else "\nRien à corriger.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
