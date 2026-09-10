#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Vérification du site statique Amélie & Partners.

Contrôle, sans navigateur :
  - chaque lien interne pointe vers un fichier existant ;
  - chaque ancre interne (#…) existe dans la page visée ;
  - chaque image, feuille de styles, script et police référencés existent ;
  - chaque page a un titre, une description, une balise canonique et un <h1> ;
  - chaque <img> porte un attribut alt (vide autorisé pour les décors) ;
  - les invariants de marque sont présents (huit témoignages, mention sur la
    variabilité des résultats, lien de réservation, adresse e-mail).

Usage, depuis la racine du site :
    python3 outils/verifier-site.py
"""

import os
import re
import sys
from html.parser import HTMLParser

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CALENDLY = "https://calendly.com/amelie-partners"
EMAIL = "contact@amelie-invest.com"

erreurs = []
avertissements = []


class Analyse(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.liens = []
        self.ressources = []
        self.ids = set()
        self.images = []
        self.h1 = 0
        self.title = False
        self._in_title = False
        self.title_texte = ""
        self.description = None
        self.canonical = None

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if a.get("id"):
            self.ids.add(a["id"])
        if a.get("name") and tag == "a":
            self.ids.add(a["name"])
        if tag == "a" and a.get("href"):
            self.liens.append(a["href"])
        elif tag == "link" and a.get("href"):
            if a.get("rel") == "canonical":
                self.canonical = a["href"]
            else:
                self.ressources.append(a["href"])
        elif tag == "script" and a.get("src"):
            self.ressources.append(a["src"])
        elif tag == "img":
            self.images.append(a)
            if a.get("src"):
                self.ressources.append(a["src"])
        elif tag == "meta" and a.get("name") == "description":
            self.description = a.get("content")
        elif tag == "h1":
            self.h1 += 1
        elif tag == "title":
            self.title = True
            self._in_title = True

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False

    def handle_data(self, data):
        if self._in_title:
            self.title_texte += data


def pages():
    return sorted(f for f in os.listdir(RACINE) if f.endswith(".html"))


def main():
    docs = {}
    for nom in pages():
        p = Analyse()
        p.feed(open(os.path.join(RACINE, nom), encoding="utf-8").read())
        docs[nom] = p

    for nom, p in docs.items():
        if not p.title or not p.title_texte.strip():
            erreurs.append(f"{nom} : titre manquant")
        if not p.description:
            erreurs.append(f"{nom} : meta description manquante")
        if not p.canonical:
            avertissements.append(f"{nom} : balise canonique absente")
        if p.h1 != 1:
            erreurs.append(f"{nom} : {p.h1} balise(s) h1 (une seule attendue)")

        for img in p.images:
            if "alt" not in img:
                erreurs.append(f"{nom} : <img src=\"{img.get('src')}\"> sans attribut alt")

        for ref in p.ressources:
            if ref.startswith(("http://", "https://", "data:", "mailto:", "#")):
                continue
            chemin = os.path.join(RACINE, ref.split("?")[0])
            if not os.path.exists(chemin):
                erreurs.append(f"{nom} : ressource introuvable → {ref}")

        for lien in p.liens:
            if lien.startswith(("http://", "https://", "mailto:", "tel:")):
                continue
            cible, _, ancre = lien.partition("#")
            if cible:
                chemin = os.path.join(RACINE, cible)
                if not os.path.exists(chemin):
                    erreurs.append(f"{nom} : lien cassé → {lien}")
                    continue
                doc = docs.get(cible)
            else:
                doc = p
            if ancre and doc and ancre not in doc.ids:
                erreurs.append(f"{nom} : ancre introuvable → {lien}")

    # ------------------------------------------------ invariants de marque
    accueil = open(os.path.join(RACINE, "index.html"), encoding="utf-8").read()

    noms = ["Stéphane D.", "Jane V.", "Sébastien C.", "Bernard L.",
            "Hang N.", "Clément R.", "François D.", "Yann C."]
    manquants = [n for n in noms if n not in accueil]
    if manquants:
        erreurs.append("index.html : témoignages manquants → " + ", ".join(manquants))
    # Les huit témoignages passent en carrousel : chaque nom paraît une fois
    # par page. Le bandeau défilant, qui doublait la série pour fermer sa
    # boucle, n'existe plus.
    for n in noms:
        if accueil.count(n) != 1:
            avertissements.append(
                f"index.html : « {n} » apparaît {accueil.count(n)} fois "
                "(1 attendue : le carrousel ne double plus la série)")

    if "les résultats varient selon les situations" not in accueil:
        erreurs.append("index.html : mention sur la variabilité des résultats absente")
    if "TÉMOIGNAGES" not in accueil.upper():
        erreurs.append("index.html : section Témoignages absente")
    if "Décisions clients" in accueil:
        erreurs.append("index.html : titre interdit « Décisions clients »")

    for nom in pages():
        s = open(os.path.join(RACINE, nom), encoding="utf-8").read()
        if re.search(r"[\U0001F300-\U0001FAFF←-⇿⬀-⯿]", s):
            erreurs.append(f"{nom} : émoji ou flèche Unicode détecté (chevrons vectoriels attendus)")
        if "#/" in s:
            avertissements.append(f"{nom} : routeur « #/… » détecté")
        # Les pages sont produites par des gabarits Python. Une accolade
        # restée en clair est un marqueur non remplacé : il s'affiche tel
        # quel dans le navigateur. Les styles en ligne sont ecartes, une
        # accolade y est legitime.
        sans_style = re.sub(r'style="[^"]*"', "", s)
        for marqueur in set(re.findall(r"\{[A-Za-z_][A-Za-z0-9_]*\}", sans_style)):
            erreurs.append(f"{nom} : marqueur de gabarit non remplacé → {marqueur}")

    if CALENDLY not in accueil:
        erreurs.append("index.html : lien de réservation absent")
    if EMAIL not in accueil:
        erreurs.append("index.html : adresse e-mail absente")

    for f in ("sitemap.xml", "robots.txt", "assets/css/styles.css",
              "assets/css/fonts.css", "assets/js/site.js", "assets/fonts/OFL.txt"):
        if not os.path.exists(os.path.join(RACINE, f)):
            erreurs.append(f"fichier attendu manquant : {f}")

    # ------------------------------------------------------------- rapport
    print(f"{len(docs)} pages analysées.")
    for a in avertissements:
        print("  avertissement :", a)
    for e in erreurs:
        print("  ERREUR :", e)
    if erreurs:
        print(f"\n{len(erreurs)} erreur(s).")
        return 1
    print("\nAucune erreur." + (f" {len(avertissements)} avertissement(s)." if avertissements else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())
