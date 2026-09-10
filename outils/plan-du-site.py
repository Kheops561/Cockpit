#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Réécrit `sitemap.xml` à partir des pages présentes sur le disque.

Le plan du site était tenu à la main. Avec une deuxième langue, cela faisait
deux listes à maintenir en parallèle, et une page oubliée ne se voit pas.
Ce script les relève lui-même.

Deux choses qu'il fait et qu'une liste manuelle ne faisait pas :

- il déclare les **traductions** d'une page les unes aux autres, par
  `xhtml:link`. Sans cela, les moteurs peuvent lire deux pages de contenu
  proche comme des doublons plutôt que comme deux versions ;
- il prend la **date de dernière modification** du fichier, au lieu d'une
  date recopiée.

La page introuvable n'y figure pas : on ne demande pas à un moteur
d'indexer une erreur.

    python3 outils/plan-du-site.py
"""
import os
import re
import sys
from datetime import date

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOMAINE = "https://amelie-invest.com"

# Ce qui n'est pas proposé à l'indexation.
EXCLUES = {"404.html"}

# Fréquence de révision et importance relative, par page. Une page absente
# de ce tableau reçoit la dernière ligne.
RANG = {
    "index.html": ("weekly", "1.0"),
    "diagnostic.html": ("monthly", "0.9"),
    "accompagnements.html": ("monthly", "0.9"),
    "approche.html": ("monthly", "0.8"),
    "temoignages.html": ("monthly", "0.8"),
    "ressources.html": ("monthly", "0.7"),
    "ressource-3-effets.html": ("yearly", "0.6"),
    "a-propos.html": ("yearly", "0.6"),
    "contact.html": ("yearly", "0.6"),
    "formulaire.html": ("yearly", "0.6"),
    "cgv.html": ("yearly", "0.3"),
    "mentions-legales.html": ("yearly", "0.2"),
    "confidentialite.html": ("yearly", "0.2"),
}
DEFAUT = ("yearly", "0.5")

# L'ordre d'affichage : celui du tableau ci-dessus, puis l'alphabet.
ORDRE = {nom: i for i, nom in enumerate(RANG)}


def langues():
    """Les dossiers de langue présents, le français d'abord."""
    trouvees = [""]
    for nom in sorted(os.listdir(RACINE)):
        if re.fullmatch(r"[a-z]{2}", nom) and os.path.isdir(os.path.join(RACINE, nom)):
            trouvees.append(nom)
    return trouvees


def url(lang, page):
    chemin = "" if page == "index.html" else page
    return f"{DOMAINE}/{lang + '/' if lang else ''}{chemin}"


def modifiee(lang, page):
    chemin = os.path.join(RACINE, lang, page) if lang else os.path.join(RACINE, page)
    return date.fromtimestamp(os.path.getmtime(chemin)).isoformat()


def main():
    langs = langues()
    # Quelles langues portent quelle page.
    pages = {}
    for lang in langs:
        dossier = os.path.join(RACINE, lang) if lang else RACINE
        for nom in os.listdir(dossier):
            if nom.endswith(".html") and nom not in EXCLUES:
                pages.setdefault(nom, []).append(lang)

    lignes = ['<?xml version="1.0" encoding="UTF-8"?>',
              '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
              '        xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    total = 0
    for nom in sorted(pages, key=lambda n: (ORDRE.get(n, 99), n)):
        presentes = pages[nom]
        frequence, priorite = RANG.get(nom, DEFAUT)
        for lang in presentes:
            lignes.append("  <url>")
            lignes.append(f"    <loc>{url(lang, nom)}</loc>")
            # Une page traduite se déclare aux côtés de ses sœurs, la
            # française comprise : c'est ce que demandent les moteurs.
            if len(presentes) > 1:
                for autre in presentes:
                    code = autre or "fr"
                    lignes.append(
                        f'    <xhtml:link rel="alternate" hreflang="{code}"'
                        f' href="{url(autre, nom)}"/>')
                lignes.append(
                    '    <xhtml:link rel="alternate" hreflang="x-default"'
                    f' href="{url("", nom)}"/>')
            lignes.append(f"    <lastmod>{modifiee(lang, nom)}</lastmod>")
            lignes.append(f"    <changefreq>{frequence}</changefreq>")
            lignes.append(f"    <priority>{priorite}</priority>")
            lignes.append("  </url>")
            total += 1
    lignes.append("</urlset>")

    with open(os.path.join(RACINE, "sitemap.xml"), "w", encoding="utf-8") as f:
        f.write("\n".join(lignes) + "\n")
    print(f"sitemap.xml : {total} adresse(s), {len(pages)} page(s), "
          f"{len(langs)} langue(s).")


if __name__ == "__main__":
    sys.exit(main())
