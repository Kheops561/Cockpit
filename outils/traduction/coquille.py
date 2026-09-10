# -*- coding: utf-8 -*-
"""La coquille du site : tete, en-tete, pied de page, icones, drapeaux.

Ce fichier est **dans le depot**, et non dans les brouillons, pour une
raison precise : les pages traduites en descendent. Une page anglaise n'est
pas ecrite a la main — elle est fabriquee a partir de la page francaise
publiee, a qui l'on remet cette coquille dans la langue voulue. Sans ce
fichier, le dossier `en/` ne pourrait plus etre regenere.

Les fonctions prennent toutes une langue. Elle vaut « fr » par defaut : les
gabarits francais continuent donc de fonctionner sans etre touches.

Les textes de la coquille — navigation, pied de page, reperes
d'accessibilite — vivent dans `langues.py`, une entree par langue.
"""

from langues import LANGUES, PUBLIEES, IDENTITE, TEXTES, prefixe, lien

# Les quatre adresses que le site ecrit. Les trois premieres sont les seuls
# liens sortants autorises ; la derniere est le site lui-meme.
LINKEDIN = "https://www.linkedin.com/company/amelie-partners"
CALENDLY = "https://calendly.com/amelie-partners"
EMAIL = "contact@amelie-invest.com"
DOMAIN = "https://amelie-invest.com"

# --------------------------------------------------------------- icones SVG
# Chevrons et pictogrammes vectoriels monochromes. Aucun emoji, aucune fleche
# Unicode : les icones sont dessinees et portent aria-hidden.

ICON = {
    "arrow": '<svg class="icon" width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true" focusable="false"><path d="M2 8h11M9 4l4 4-4 4" stroke="currentColor" stroke-width="1.3" stroke-linecap="square"/></svg>',
    "arrow-ne": '<svg class="icon" width="24" height="24" viewBox="0 0 24 24" fill="none" aria-hidden="true" focusable="false"><path d="M7 17 17 7M9 7h8v8" stroke="currentColor" stroke-width="1.3" stroke-linecap="square"/></svg>',
    "chevron": '<svg class="icon" width="14" height="14" viewBox="0 0 14 14" fill="none" aria-hidden="true" focusable="false"><path d="M3 5.5 7 9.5l4-4" stroke="currentColor" stroke-width="1.3" stroke-linecap="square"/></svg>',
    "calendar": '<svg class="icon" width="18" height="18" viewBox="0 0 18 18" fill="none" aria-hidden="true" focusable="false"><rect x="2.25" y="3.75" width="13.5" height="12" stroke="currentColor" stroke-width="1.2"/><path d="M2.25 7.5h13.5M6 2.25v3M12 2.25v3" stroke="currentColor" stroke-width="1.2" stroke-linecap="square"/></svg>',
    "check": '<svg class="icon" width="14" height="14" viewBox="0 0 14 14" fill="none" aria-hidden="true" focusable="false"><path d="M2.5 7.5 5.75 10.75 11.5 3.75" stroke="currentColor" stroke-width="1.4" stroke-linecap="square"/></svg>',
    "lecture": '<svg class="icon" width="12" height="12" viewBox="0 0 12 12" aria-hidden="true" focusable="false"><path d="M3.5 2 10 6l-6.5 4Z" fill="currentColor"/></svg>',
    "pause": '<svg class="icon" width="12" height="12" viewBox="0 0 12 12" fill="none" aria-hidden="true" focusable="false"><path d="M4 2v8M8 2v8" stroke="currentColor" stroke-width="1.4" stroke-linecap="square"/></svg>',
    "personne": '<svg class="icon" width="18" height="18" viewBox="0 0 18 18" fill="none" aria-hidden="true" focusable="false"><circle cx="9" cy="6.25" r="3.1" stroke="currentColor" stroke-width="1.2"/><path d="M3.2 15.4c.6-2.9 3-4.6 5.8-4.6s5.2 1.7 5.8 4.6" stroke="currentColor" stroke-width="1.2" stroke-linecap="square"/></svg>',
    "telephone": '<svg class="icon" width="18" height="18" viewBox="0 0 18 18" fill="none" aria-hidden="true" focusable="false"><rect x="5" y="1.9" width="8" height="14.2" stroke="currentColor" stroke-width="1.2"/><path d="M7.7 14.1h2.6" stroke="currentColor" stroke-width="1.2" stroke-linecap="square"/></svg>',
    "reperes": '<svg class="icon" width="18" height="18" viewBox="0 0 18 18" fill="none" aria-hidden="true" focusable="false"><path d="M3 4.5h12M3 9h12M3 13.5h7" stroke="currentColor" stroke-width="1.2" stroke-linecap="square"/></svg>',
    "plume": '<svg class="icon" width="18" height="18" viewBox="0 0 18 18" fill="none" aria-hidden="true" focusable="false"><path d="M11.6 2.6 15.4 6.4 6.6 15.2H2.8v-3.8Z" stroke="currentColor" stroke-width="1.2" stroke-linejoin="round"/><path d="M9.8 4.4l3.8 3.8" stroke="currentColor" stroke-width="1.2"/></svg>',
    "telecharger": '<svg class="icon" width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true" focusable="false"><path d="M8 1.8v8.4M4.6 7.2 8 10.6l3.4-3.4" stroke="currentColor" stroke-width="1.3" stroke-linecap="square"/><path d="M2.4 12.6v1.6h11.2v-1.6" stroke="currentColor" stroke-width="1.3" stroke-linecap="square"/></svg>',
    "alerte": '<svg class="icon" width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true" focusable="false"><circle cx="8" cy="8" r="6.4" stroke="currentColor" stroke-width="1.2"/><path d="M8 4.6v4.2M8 11.1v.9" stroke="currentColor" stroke-width="1.4" stroke-linecap="square"/></svg>',
    "mail": '<svg class="icon" width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true" focusable="false"><rect x="1.75" y="3.25" width="12.5" height="9.5" stroke="currentColor" stroke-width="1.2"/><path d="m2 4 6 4.5L14 4" stroke="currentColor" stroke-width="1.2"/></svg>',
    "livre": '<svg class="icon" width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true" focusable="false"><path d="M8 4.2C6.6 3.1 4.9 2.7 2.4 2.7v9.4c2.5 0 4.2.4 5.6 1.5 1.4-1.1 3.1-1.5 5.6-1.5V2.7c-2.5 0-4.2.4-5.6 1.5Z" stroke="currentColor" stroke-width="1.2" stroke-linecap="square" stroke-linejoin="round"/><path d="M8 4.2v9.4" stroke="currentColor" stroke-width="1.2" stroke-linecap="square"/></svg>',
    "linkedin": '<svg class="icon" width="16" height="16" viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path fill="currentColor" d="M22.22 0H1.77C.79 0 0 .77 0 1.72v20.56C0 23.23.79 24 1.77 24h20.45c.98 0 1.78-.77 1.78-1.72V1.72C24 .77 23.2 0 22.22 0zM7.12 20.45H3.55V9h3.57v11.45zM5.34 7.43a2.06 2.06 0 1 1 0-4.12 2.06 2.06 0 0 1 0 4.12zm15.11 13.02h-3.56v-5.57c0-1.33-.02-3.04-1.85-3.04-1.85 0-2.13 1.45-2.13 2.94v5.67H9.35V9h3.41v1.56h.05c.48-.9 1.64-1.85 3.37-1.85 3.6 0 4.27 2.37 4.27 5.45v6.29z"/></svg>',
    "duo": '<svg class="icon" width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true" focusable="false"><circle cx="6" cy="5.6" r="2.4" stroke="currentColor" stroke-width="1.2" stroke-linecap="square"/><path d="M1.8 13.4c0-2.3 1.9-4.2 4.2-4.2s4.2 1.9 4.2 4.2" stroke="currentColor" stroke-width="1.2" stroke-linecap="square"/><path d="M11 3.6a2.4 2.4 0 0 1 0 4.4M12.2 9.6c1.2.6 2 1.9 2 3.3" stroke="currentColor" stroke-width="1.2" stroke-linecap="square"/></svg>',
    "guillemets": '<svg class="icon" width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true" focusable="false"><path d="M6.4 4.5C4.3 5.3 3 7 3 9.1c0 1.5 1 2.4 2.2 2.4 1.1 0 2-.8 2-1.9 0-1-.7-1.8-1.7-1.8-.2 0-.4 0-.5.1.2-1 1-1.9 2.2-2.4zM13.4 4.5C11.3 5.3 10 7 10 9.1c0 1.5 1 2.4 2.2 2.4 1.1 0 2-.8 2-1.9 0-1-.7-1.8-1.7-1.8-.2 0-.4 0-.5.1.2-1 1-1.9 2.2-2.4z" stroke="currentColor" stroke-width="1.2" stroke-linecap="square" stroke-linejoin="round"/></svg>',
    "document": '<svg class="icon" width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true" focusable="false"><path d="M3.5 1.8h5.2L12.5 5.6v8.6h-9z" stroke="currentColor" stroke-width="1.2" stroke-linecap="square" stroke-linejoin="miter"/><path d="M8.7 1.8v3.8h3.8M5.8 8.6h4.4M5.8 11h4.4" stroke="currentColor" stroke-width="1.2" stroke-linecap="square"/></svg>',
    "bouclier": '<svg class="icon" width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true" focusable="false"><path d="M8 1.6 13.4 3.6v4.1c0 3.1-2.2 5.4-5.4 6.7-3.2-1.3-5.4-3.6-5.4-6.7V3.6z" stroke="currentColor" stroke-width="1.2" stroke-linecap="square" stroke-linejoin="round"/><path d="M5.7 7.9 7.4 9.6l3-3.2" stroke="currentColor" stroke-width="1.2" stroke-linecap="square"/></svg>',
    "cible": '<svg class="icon" width="16" height="16" viewBox="0 0 16 16" fill="none" aria-hidden="true" focusable="false"><circle cx="8" cy="8" r="6.2" stroke="currentColor" stroke-width="1.2" stroke-linecap="square"/><circle cx="8" cy="8" r="3" stroke="currentColor" stroke-width="1.2" stroke-linecap="square"/><circle cx="8" cy="8" r=".6" fill="currentColor" stroke="none"/></svg>',
}

# ------------------------------------------------------------------- navigation



def alternats(path):
    """Les liens `hreflang` : la meme page dans chacune des langues.

    Ils disent aux moteurs que ces pages sont des traductions l'une de
    l'autre, et non des doublons. `x-default` designe le francais : c'est la
    version servie a qui ne demande aucune des trois langues.
    """
    from langues import PAGES_LEGALES
    lignes = []
    for autre in PUBLIEES:
        # Une page legale n'existe qu'en francais : elle n'a pas d'alternat.
        if path in PAGES_LEGALES and autre != "fr":
            continue
        url = DOMAIN + "/" + prefixe(autre) + ("" if path == "index.html" else path)
        lignes.append(f'<link rel="alternate" hreflang="{IDENTITE[autre]["code"]}" href="{url}">')
    if path not in PAGES_LEGALES:
        racine = DOMAIN + "/" + ("" if path == "index.html" else path)
        lignes.append(f'<link rel="alternate" hreflang="x-default" href="{racine}">')
    return "\n".join(lignes)


def head(title, description, path, image="/assets/images/og-image.jpg", lang="fr"):
    canonical = DOMAIN + "/" + prefixe(lang) + ("" if path == "index.html" else path)
    # Une classe par page : elle permet de régler une seule page,
    # par exemple la largeur de sa colonne, sans toucher aux autres.
    slug = path[:-5] if path.endswith(".html") else path
    return f"""<!DOCTYPE html>
<html lang="{IDENTITE[lang]['code']}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<meta name="theme-color" content="#12283c">
<meta property="og:type" content="website">
<meta property="og:locale" content="{IDENTITE[lang]['og']}">
{alternats(path)}
<meta property="og:site_name" content="Amélie &amp; Partners">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="{DOMAIN}{image}">
<meta name="twitter:card" content="summary_large_image">
<link rel="preload" as="font" type="font/woff2" href="/assets/fonts/inter-latin.woff2" crossorigin>
<link rel="preload" as="font" type="font/woff2" href="/assets/fonts/source-serif-4-latin.woff2" crossorigin>
<script>document.documentElement.classList.add('js');try{{if(!sessionStorage.getItem('ap-arrivee')){{document.documentElement.classList.add('premiere-visite');sessionStorage.setItem('ap-arrivee','1');}}}}catch(e){{}}</script>
<link rel="stylesheet" href="/assets/css/fonts.css">
<link rel="stylesheet" href="/assets/css/styles.css">
<link rel="icon" href="/assets/images/favicon.png" type="image/png">
<link rel="apple-touch-icon" href="/assets/images/favicon.png">
<!-- Mesure d'audience Vercel. Le chemin est celui du site lui-meme : le
     navigateur ne s'adresse a aucun domaine tiers, ni pour charger ce
     script, ni pour lui envoyer une visite. La regle du cahier des charges
     tient donc toujours. Aucun cookie n'est depose. Hors Vercel — en local
     par exemple — le fichier n'existe pas et la page s'en passe. -->
<script defer src="/_vercel/insights/script.js"></script>
</head>
<body class="page-{slug} langue-{lang}">
<div class="voile" data-voile aria-hidden="true">
  <img class="voile__marque" src="/assets/images/logo.png" alt="" width="400" height="400" decoding="async">
</div>
<a class="skip" href="#contenu">{TEXTES[lang]['aller-contenu']}</a>
"""


def selecteur_langue(lang, path):
    """Le choix de la langue, en drapeaux.

    C'est une liste de liens, rien d'autre : elle fonctionne sans JavaScript,
    et chaque lien mene a la meme page dans l'autre langue. La langue en
    cours porte `aria-current`, comme la page ouverte dans la navigation.

    Les pages legales n'existent qu'en francais : sur celles-la, le selecteur
    ne s'affiche pas — il n'aurait nulle part ou mener.
    """
    from langues import PAGES_LEGALES
    if path in PAGES_LEGALES:
        return ""
    # Une seule langue en ligne : le selecteur n'a rien a proposer.
    if len(PUBLIEES) < 2:
        return ""
    items = []
    for autre in PUBLIEES:
        ident = IDENTITE[autre]
        cible = "/" + prefixe(autre) + ("" if path == "index.html" else path)
        courant = ' aria-current="true"' if autre == lang else ""
        items.append(
            f'<li><a class="langues-choix__lien" href="{cible}" hreflang="{ident["code"]}"'
            f' lang="{ident["code"]}"{courant}>'
            f'{DRAPEAUX[ident["drapeau"]]}<span>{ident["court"]}</span>'
            f'<span class="sr-only"> — {ident["nom"]}</span></a></li>')
    return (f'    <nav class="langues-choix" aria-label="{TEXTES[lang]["choisir-langue"]}">\n'
            f'      <ul>{"".join(items)}</ul>\n'
            f'    </nav>\n')


def header(active="", lang="fr", path=None):
    """`active` marque la page ouverte dans la navigation ; `path` dit
    laquelle c'est.

    Les deux se confondent presque toujours. Ils se separent sur les pages
    qui ne figurent pas dans la navigation — les pages legales, la page
    introuvable : rien n'y est a souligner, mais le selecteur de langue doit
    quand meme savoir sur quelle page il se trouve. Sans cela il renverrait
    vers l'accueil, en faisant croire a une traduction de la page ouverte.
    """
    T = TEXTES[lang]

    def links(items, cls, extra=""):
        # Le libelle du tiroir vit dans un `span` : c'est lui qui porte le
        # filet de la page ouverte, sous le texte et non sous la rangee
        # entiere. La barre du haut marque sa page de la meme facon.
        out = []
        for href, label in items:
            cur = ' aria-current="page"' if href == active else ""
            dedans = f'<span>{label}</span>' if cls == "drawer__link" else label
            out.append(f'<li><a class="{cls}" href="{lien(lang, href)}"{cur}>{dedans}</a></li>')
        return "\n".join(out)

    return f"""<header class="header" data-header>
  <div class="wrap header__inner">
    <a class="logo" href="index.html" aria-label="{T['retour-accueil']}">
      <img class="logo__mark" src="/assets/images/logo.png" alt="" width="400" height="400" decoding="async">
      <span class="logo__text">
        <span class="logo__name">Amélie &amp; Partners</span>
        <span class="logo__tag">Investir avec méthode <span>&middot;</span> Décider avec clarté</span>
      </span>
    </a>
    <nav class="nav" aria-label="{T['nav-principale']}">
      <ul style="display:contents">
{links(T['nav'], "nav__link")}
      </ul>
    </nav>
{selecteur_langue(lang, path or active or 'index.html')}    <a class="btn header__cta" href="diagnostic.html"><span>{T['cta-tete']}</span>{ICON['arrow']}</a>
    <button class="burger" type="button" data-burger aria-expanded="false" aria-controls="menu-mobile" hidden>
      <span></span><span></span><span></span>
      <span class="sr-only">{T['ouvrir-menu']}</span>
    </button>
  </div>
  <div class="drawer" id="menu-mobile">
    <div class="wrap">
      <nav aria-label="{T['nav-mobile']}">
        <ul class="drawer__list">
{links(T['drawer'], "drawer__link")}
        </ul>
      </nav>
      <a class="btn" href="{CALENDLY}" target="_blank" rel="noopener"><span>{T['cta-reserver']}</span>{ICON['arrow']}</a>
    </div>
  </div>
</header>
"""


def footer(lang="fr"):
    T = TEXTES[lang]

    def rangee(entrees):
        return "\n".join(
            f'          <li><a href="{lien(lang, href)}">{ICON[picto]}<span>{label}</span></a></li>'
            for href, label, picto in entrees)

    return f"""<footer class="footer">
  <div class="wrap">
    <div class="footer__top">
      <div>
        <span class="logo">
          <img class="logo__mark" src="/assets/images/logo.png" alt="" width="400" height="400" loading="lazy" decoding="async">
          <span class="logo__text">
            <span class="logo__name">Amélie &amp; Partners</span>
            <span class="logo__tag">Investir avec méthode <span>&middot;</span> Décider avec clarté</span>
          </span>
        </span>
        <p class="footer__baseline">{T['promesse']}</p>
      </div>
      <div>
        <h2 class="footer__title">{T['pied-explorer']}</h2>
        <ul class="footer__list">
{rangee(T['pied-explorer-liens'])}
        </ul>
      </div>
      <div>
        <h2 class="footer__title">{T['pied-commencer']}</h2>
        <ul class="footer__list">
{rangee(T['pied-commencer-liens'])}
          <li><a href="{CALENDLY}" target="_blank" rel="noopener">{ICON['calendar']}<span>{T['pied-echange']}</span></a></li>
        </ul>
      </div>
      <div>
        <h2 class="footer__title">{T['pied-informations']}</h2>
        <ul class="footer__list">
{rangee(T['pied-informations-liens'])}
          <li><a href="{LINKEDIN}" target="_blank" rel="noopener">{ICON['linkedin']}<span>LinkedIn</span></a></li>
{rangee(T['pied-legal'])}
        </ul>
      </div>
    </div>
    <div class="footer__bottom">
      <p>{T['pied-mention']}</p>
    </div>
  </div>
</footer>
<script src="/assets/js/site.js" defer></script>
</body>
</html>
"""



DRAPEAUX = {
    # Deux drapeaux dessinés en vectoriel, aux couleurs officielles. Ils sont
    # décoratifs : le nom du lieu est écrit juste à côté, aucune information
    # ne repose sur eux seuls.
    "france": (
        '<svg class="drapeau" viewBox="0 0 30 20" role="presentation" focusable="false" aria-hidden="true">'
        '<rect width="10" height="20" fill="#002395"/>'
        '<rect x="10" width="10" height="20" fill="#fff"/>'
        '<rect x="20" width="10" height="20" fill="#ed2939"/>'
        '</svg>'),
    # Le drapeau britannique. La contre-passe des diagonales — le decalage
    # du rouge de part et d'autre du blanc — n'est pas rendue : a la taille
    # ou ce drapeau est pose, quinze pixels de large, elle serait invisible,
    # et la dessiner demanderait des decoupes qui ne survivent pas a la
    # reduction. Les proportions et les couleurs, elles, sont justes.
    "royaume-uni": (
        '<svg class="drapeau" viewBox="0 0 30 20" role="presentation" focusable="false" aria-hidden="true">'
        '<rect width="30" height="20" fill="#012169"/>'
        '<path d="M0 0 30 20M30 0 0 20" stroke="#fff" stroke-width="4.4"/>'
        '<path d="M0 0 30 20M30 0 0 20" stroke="#c8102e" stroke-width="1.8"/>'
        '<path d="M15 0v20M0 10h30" stroke="#fff" stroke-width="6.6"/>'
        '<path d="M15 0v20M0 10h30" stroke="#c8102e" stroke-width="4"/>'
        '</svg>'),
    "vietnam": (
        '<svg class="drapeau" viewBox="0 0 30 20" role="presentation" focusable="false" aria-hidden="true">'
        '<rect width="30" height="20" fill="#da251d"/>'
        '<path fill="#ff0" d="M15 4.6 16.6 9.4 21.7 9.4 17.6 12.4 19.2 17.2 15 14.2 10.8 17.2 12.4 12.4 8.3 9.4 13.4 9.4Z"/>'
        '</svg>'),
}


def drapeau(pays):
    """Le drapeau demandé, en vectoriel, sans appel extérieur."""
    return DRAPEAUX[pays]
