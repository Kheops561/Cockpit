# -*- coding: utf-8 -*-
"""Fabrique le PDF de la fiche pédagogique « Les 3 effets ».

Le site est statique : il ne peut pas fabriquer un PDF au moment du clic,
et aucun service extérieur n'est appelé depuis les pages. Le PDF est donc
un fichier posé dans le dépôt, comme une image, et le bouton de la page
pointe simplement dessus.

Il est imprimé par le navigateur déjà présent dans cet environnement, en
appliquant la feuille de style d'impression du site : mêmes polices, même
typographie, sans en-tête ni pied de site.

Relancer après toute modification de `ressource-3-effets.html` ou des
règles `@media print` de `assets/css/styles.css` :

    python3 outils/fiche-pdf.py
"""
import http.server
import os
import socketserver
import sys
import threading

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGE = "ressource-3-effets.html"
SORTIE = "assets/documents/amelie-partners-les-3-effets.pdf"
PORT = 8123

CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"


def servir():
    """Un serveur local le temps de l'impression.

    Le navigateur refuse les polices locales sur `file://` : la page doit
    être servie en HTTP pour que le PDF sorte avec les bonnes fontes.
    """
    os.chdir(RACINE)
    handler = http.server.SimpleHTTPRequestHandler
    socketserver.TCPServer.allow_reuse_address = True
    httpd = socketserver.TCPServer(("127.0.0.1", PORT), handler)
    fil = threading.Thread(target=httpd.serve_forever, daemon=True)
    fil.start()
    return httpd


def main():
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("Playwright est nécessaire pour fabriquer le PDF.", file=sys.stderr)
        return 1

    httpd = servir()
    try:
        with sync_playwright() as p:
            navigateur = p.chromium.launch(executable_path=CHROME)
            page = navigateur.new_page()
            page.goto(f"http://127.0.0.1:{PORT}/{PAGE}", wait_until="networkidle")
            # Les apparitions sont armées au défilement : à l'impression,
            # tout doit déjà être visible.
            page.evaluate(
                "() => document.querySelectorAll('.reveal')"
                ".forEach(e => e.classList.add('is-visible'))")
            # La classe `pdf` ouvre les regles reservees au fichier
            # fabrique : couleurs de la maison et mise en page resserree.
            # Le visiteur qui imprime la page depuis son navigateur garde,
            # lui, la version sobre en noir sur blanc.
            page.evaluate("() => document.documentElement.classList.add('pdf')")
            page.emulate_media(media="print")
            if page.evaluate("() => document.fonts && document.fonts.ready ? 1 : 0"):
                page.evaluate("() => document.fonts.ready")
            page.wait_for_timeout(600)
            page.pdf(
                path=os.path.join(RACINE, SORTIE),
                format="A4",
                print_background=True,
                margin={"top": "13mm", "bottom": "14mm",
                        "left": "13mm", "right": "13mm"},
                display_header_footer=True,
                header_template=(
                    '<div style="font:8px \'Helvetica\',sans-serif;color:#52616c;'
                    'width:100%;padding:0 16mm;">AMÉLIE &amp; PARTNERS'
                    ' &middot; Investir avec méthode, décider avec clarté</div>'),
                footer_template=(
                    '<div style="font:8px \'Helvetica\',sans-serif;color:#52616c;'
                    'width:100%;padding:0 16mm;display:flex;'
                    'justify-content:space-between;">'
                    '<span>amelie-invest.com</span>'
                    '<span class="pageNumber"></span></div>'),
            )
            navigateur.close()
    finally:
        httpd.shutdown()

    poids = os.path.getsize(os.path.join(RACINE, SORTIE))
    print(f"écrit : {SORTIE}  {poids / 1024:.0f} Ko")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
