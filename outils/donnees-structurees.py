#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Insère (ou remet à jour) les données structurées JSON-LD.

À relancer après toute modification de l'accueil ou de la page Diagnostic.
Le script est idempotent : il remplace le bloc existant au lieu d'en ajouter
un second.

    python3 outils/donnees-structurees.py
"""

import io
import json
import os
import re

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://amelie-invest.com"

ORGANISATION = {
    "@context": "https://schema.org",
    "@type": "ProfessionalService",
    "name": "Amélie & Partners",
    "url": SITE + "/",
    "email": "contact@amelie-invest.com",
    "image": SITE + "/assets/images/og-image.jpg",
    "description": "Conseil en stratégie d’investissement immobilier. Amélie & Partners "
                   "accompagne les investisseurs particuliers et professionnels pour "
                   "financer, acquérir et piloter leur patrimoine immobilier.",
    "slogan": "Investir avec méthode · Décider avec clarté",
    "areaServed": [{"@type": "City", "name": "Paris"}, {"@type": "Country", "name": "France"}],
    "founder": {"@type": "Person", "name": "Amélie-Thu DUONG", "jobTitle": "Fondatrice"},
    "knowsLanguage": "fr-FR",
    "makesOffer": [{
        "@type": "Offer",
        "name": "Diagnostic Stratégique",
        "description": "Questionnaire préparatoire, session stratégique de 75 minutes "
                       "et Note de Diagnostic & Décision.",
        "price": "450",
        "priceCurrency": "EUR",
        "valueAddedTaxIncluded": False,
        "url": SITE + "/diagnostic.html",
    }],
}

SERVICE = {
    "@context": "https://schema.org",
    "@type": "Service",
    "name": "Diagnostic Stratégique",
    "serviceType": "Conseil en stratégie d’investissement immobilier",
    "provider": {"@type": "ProfessionalService", "name": "Amélie & Partners", "url": SITE + "/"},
    "areaServed": {"@type": "Country", "name": "France"},
    "description": "Un regard stratégique pour clarifier la situation, challenger les "
                   "options et déterminer la prochaine étape : questionnaire préparatoire, "
                   "session de 75 minutes et Note de Diagnostic & Décision.",
    "offers": {
        "@type": "Offer",
        "price": "450",
        "priceCurrency": "EUR",
        "valueAddedTaxIncluded": False,
        "url": SITE + "/diagnostic.html",
    },
}

MARQUEUR = '<script src="assets/js/site.js" defer></script>'


def appliquer(fichier, donnees):
    chemin = os.path.join(RACINE, fichier)
    contenu = io.open(chemin, encoding="utf-8").read()
    contenu = re.sub(r'<script type="application/ld\+json">.*?</script>\s*', "",
                     contenu, flags=re.S)
    bloc = ('<script type="application/ld+json">\n'
            + json.dumps(donnees, ensure_ascii=False, indent=2)
            + "\n</script>\n")
    if MARQUEUR not in contenu:
        raise SystemExit(f"{fichier} : appel du script du site introuvable.")
    contenu = contenu.replace(MARQUEUR, bloc + MARQUEUR)
    io.open(chemin, "w", encoding="utf-8").write(contenu)
    print("données structurées :", fichier)


if __name__ == "__main__":
    appliquer("index.html", ORGANISATION)
    appliquer("diagnostic.html", SERVICE)
