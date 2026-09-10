# -*- coding: utf-8 -*-
"""Cherche ce qui serait reste en francais dans une page traduite.

Le dictionnaire garantit deja qu'aucune chaine n'a ete oubliee. Ce controle
prend le probleme par l'autre bout : il relit la page produite et signale
tout ce qui *ressemble* a du francais. C'est un filet, pas une preuve — mais
il attrape la traduction distraite qui aurait recopie sa source.

Ce qui reste en francais volontairement — citations signalees par `lang="fr"`,
noms d'offres, nom du cabinet — est ecarte.
"""
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from inventaire import relever

# Des mots que l'anglais n'ecrit pas, et qui ne sont pas des noms propres.
FRANCAIS = re.compile(
    r"(?i)\b(le|la|les|des|une|aux|nous|vous|leur|leurs|dans|pour|avec|sans|"
    r"mais|donc|plus|tout|toute|toutes|tous|cette|votre|vos|notre|nos|est|"
    r"sont|etre|être|avoir|fait|faire|peut|pouvez|chaque|entre|apres|après|"
    r"avant|selon|ainsi|alors|encore|jamais|toujours|sur|sous|vers|chez|"
    r"quand|comment|pourquoi|qui|que|quoi|dont)\b")

# Ce qui a le droit de rester francais.
TOLERE = re.compile(
    r"Diagnostic Stratégique|Stratégie de Financement|"
    r"Recherche immobilière à Paris|Trajectoire Investisseur|"
    r"Investir avec méthode|Décider avec clarté|Amélie|Partners|"
    r"AVANCER|PRÉPARER|RESTRUCTURER|APPROFONDIR|SUSPENDRE|"
    r"Saint-Maur-des-Fossés|Hanoï|Hanoi|Hoan Kiem|Pont des Arts|"
    r"Viêt Nam|Côte d’Ivoire|La Réunion|Nouvelle-Calédonie|"
    r"Fontainebleau|Rivoli|Louvre|Seine|Marais|Essilor|Veolia|CPAM")

# Une citation gardee en francais porte son `lang` : on la retire avant de lire.
CITATION = re.compile(r'(?s)<span lang="fr">.*?</span>')


def suspects(chemin):
    html = open(chemin, encoding="utf-8").read()
    html = CITATION.sub(" ", html)
    sortie = []
    for t in relever(html):
        net = TOLERE.sub(" ", t)
        trouves = set(m.group(0).lower() for m in FRANCAIS.finditer(net))
        if trouves:
            sortie.append((t, sorted(trouves)))
    return sortie


if __name__ == "__main__":
    total = 0
    for chemin in sys.argv[1:]:
        s = suspects(chemin)
        total += len(s)
        print(f"=== {chemin} : {len(s)} suspect(s)")
        for t, mots in s:
            print("   ", ",".join(mots), "|", t[:110])
    raise SystemExit(1 if total else 0)
