# -*- coding: utf-8 -*-
"""Les langues du site, et tout ce que la coquille écrit d'elle-même.

Le français vit à la racine, les autres langues dans un dossier : `/en/`,
`/vi/`. C'est ce qui permet aux liens entre pages de rester relatifs — une
page anglaise renvoie vers une autre page anglaise sans qu'on écrive quoi
que ce soit — tandis que les fichiers du site sont appelés en absolu depuis
la racine, `/assets/…`, et sont donc partagés par toutes les langues.

Décisions prises avec Amélie, le 10 septembre 2026 :

- **Une seule version anglaise.** Entre l'anglais britannique et l'américain,
  la différence se réduit ici à quelques graphies, pour deux fois le travail
  à chaque correction de texte.
- **Les citations des témoignages restent en français**, dans la langue où
  elles ont été dites. Les traduire reviendrait à les modifier, ce que les
  instructions permanentes interdisent. Le contexte et les attributions, eux,
  sont traduits, et une mention explique pourquoi les citations ne le sont
  pas.
- **Les pages légales ne sont pas traduites.** Les autres langues y renvoient
  en indiquant que le français fait foi : une traduction approximative d'un
  texte juridique engagerait le cabinet.
"""

# L'ordre compte : c'est celui du sélecteur de langue.
LANGUES = ["fr", "en", "vi"]

# Les langues réellement en ligne. Le sélecteur et les liens `hreflang` ne
# montrent que celles-là : annoncer une traduction qui n'existe pas donne une
# page introuvable au visiteur et une erreur aux moteurs.
#
# On y ajoute une langue le jour où ses pages sont écrites, pas avant.
PUBLIEES = ["fr", "en"]

# Ce qui identifie chaque langue : le code que lisent les navigateurs et les
# moteurs, le nom que lisent les gens, et le drapeau qui les aide à repérer.
IDENTITE = {
    # `code` va dans `<html lang>` et dans `hreflang` ; `og` dans la balise
    # que lisent les réseaux sociaux, qui veut la forme longue.
    "fr": {"code": "fr", "og": "fr_FR", "nom": "Français",   "court": "FR", "drapeau": "france"},
    "en": {"code": "en", "og": "en_GB", "nom": "English",    "court": "EN", "drapeau": "royaume-uni"},
    "vi": {"code": "vi", "og": "vi_VN", "nom": "Tiếng Việt", "court": "VI", "drapeau": "vietnam"},
}

# Les pages légales n'existent qu'en français : les autres langues y renvoient.
PAGES_LEGALES = ("mentions-legales.html", "confidentialite.html", "cgv.html")


def prefixe(lang):
    """Le chemin depuis la racine du site jusqu'aux pages de cette langue."""
    return "" if lang == "fr" else f"{lang}/"


def lien(lang, page):
    """Le lien vers une page, depuis une page de la même langue.

    Les pages légales n'existent qu'en français : depuis l'anglais ou le
    vietnamien, on remonte donc à la racine.
    """
    if page in PAGES_LEGALES and lang != "fr":
        return f"/{page}"
    return page


# ---------------------------------------------------------------------------
# Les textes de la coquille : navigation, pied de page, repères d'accessibilité.
# Le corps des pages est traduit ailleurs, page par page.
#
# Le nom de la marque, sa signature et les noms des offres ne sont jamais
# traduits : « Amélie & Partners », « Investir avec méthode · Décider avec
# clarté », « Diagnostic Stratégique ». Ce sont des noms propres.
# ---------------------------------------------------------------------------

TEXTES = {
    "fr": {
        "aller-contenu": "Aller au contenu",
        "descendre": "Descendre au contenu",
        "retour-accueil": "Amélie &amp; Partners, retour à l&rsquo;accueil",
        "nav-principale": "Navigation principale",
        "nav-mobile": "Navigation mobile",
        "ouvrir-menu": "Ouvrir le menu",
        "choisir-langue": "Choisir la langue",
        "langue-actuelle": "Langue actuelle",
        "cta-tete": "Analyser ma situation",
        "cta-reserver": "Réserver un premier échange",
        "promesse": "Votre partenaire stratégique pour réussir vos projets immobiliers.",
        "pied-explorer": "Explorer",
        "pied-commencer": "Commencer",
        "pied-informations": "Informations",
        "pied-mention": "&copy; <span data-year>2026</span> Amélie &amp; Partners &middot; Paris &middot; France &middot; Conseil en stratégie d&rsquo;investissement immobilier",
        "nav": [
            ("approche.html", "Notre approche"),
            ("ressources.html", "Ressources"),
            ("accompagnements.html", "Accompagnements"),
            ("temoignages.html", "Témoignages"),
            ("a-propos.html", "À propos"),
            ("contact.html", "Contact"),
        ],
        "drawer": [
            ("index.html", "Accueil"),
            ("approche.html", "Notre approche"),
            ("accompagnements.html", "Accompagnements"),
            ("temoignages.html", "Témoignages"),
            ("ressources.html", "Ressources"),
            ("a-propos.html", "À propos"),
            ("diagnostic.html", "Diagnostic Stratégique"),
            ("contact.html", "Contact"),
        ],
        "pied-explorer-liens": [
            ("approche.html", "Notre approche", "reperes"),
            ("ressources.html", "Ressources", "livre"),
            ("accompagnements.html", "Accompagnements", "duo"),
            ("temoignages.html", "Témoignages", "guillemets"),
            ("a-propos.html", "À propos", "personne"),
        ],
        "pied-commencer-liens": [
            ("diagnostic.html", "Diagnostic Stratégique", "cible"),
        ],
        "pied-echange": "Premier échange",
        "pied-informations-liens": [
            ("contact.html", "Contact", "telephone"),
            ("formulaire.html", "Nous écrire", "mail"),
        ],
        "pied-legal": [
            ("mentions-legales.html", "Mentions légales", "document"),
            ("confidentialite.html", "Données personnelles", "bouclier"),
            ("cgv.html", "Conditions générales de vente", "document"),
        ],
    },
    "en": {
        "aller-contenu": "Skip to content",
        "descendre": "Scroll to content",
        "retour-accueil": "Amélie &amp; Partners, back to the home page",
        "nav-principale": "Main navigation",
        "nav-mobile": "Mobile navigation",
        "ouvrir-menu": "Open the menu",
        "choisir-langue": "Choose a language",
        "langue-actuelle": "Current language",
        "cta-tete": "Analyse my situation",
        "cta-reserver": "Book a first conversation",
        "promesse": "Your strategic partner for successful property investments.",
        "pied-explorer": "Explore",
        "pied-commencer": "Start here",
        "pied-informations": "Information",
        "pied-mention": "&copy; <span data-year>2026</span> Amélie &amp; Partners &middot; Paris &middot; France &middot; Property investment strategy advisory",
        "nav": [
            ("approche.html", "Our approach"),
            ("ressources.html", "Resources"),
            ("accompagnements.html", "Engagements"),
            ("temoignages.html", "Client stories"),
            ("a-propos.html", "About"),
            ("contact.html", "Contact"),
        ],
        "drawer": [
            ("index.html", "Home"),
            ("approche.html", "Our approach"),
            ("accompagnements.html", "Engagements"),
            ("temoignages.html", "Client stories"),
            ("ressources.html", "Resources"),
            ("a-propos.html", "About"),
            ("diagnostic.html", "Diagnostic Stratégique"),
            ("contact.html", "Contact"),
        ],
        "pied-explorer-liens": [
            ("approche.html", "Our approach", "reperes"),
            ("ressources.html", "Resources", "livre"),
            ("accompagnements.html", "Engagements", "duo"),
            ("temoignages.html", "Client stories", "guillemets"),
            ("a-propos.html", "About", "personne"),
        ],
        "pied-commencer-liens": [
            ("diagnostic.html", "Diagnostic Stratégique", "cible"),
        ],
        "pied-echange": "First conversation",
        "pied-informations-liens": [
            ("contact.html", "Contact", "telephone"),
            ("formulaire.html", "Write to us", "mail"),
        ],
        "pied-legal": [
            ("mentions-legales.html", "Legal notice (in French)", "document"),
            ("confidentialite.html", "Personal data (in French)", "bouclier"),
            ("cgv.html", "Terms of sale (in French)", "document"),
        ],
    },
    "vi": {
        "aller-contenu": "Đến nội dung",
        "descendre": "Xuống phần nội dung",
        "retour-accueil": "Amélie &amp; Partners, về trang chủ",
        "nav-principale": "Điều hướng chính",
        "nav-mobile": "Điều hướng trên điện thoại",
        "ouvrir-menu": "Mở menu",
        "choisir-langue": "Chọn ngôn ngữ",
        "langue-actuelle": "Ngôn ngữ hiện tại",
        "cta-tete": "Phân tích tình hình của tôi",
        "cta-reserver": "Đặt buổi trao đổi đầu tiên",
        "promesse": "Đối tác chiến lược của bạn cho các dự án bất động sản.",
        "pied-explorer": "Khám phá",
        "pied-commencer": "Bắt đầu",
        "pied-informations": "Thông tin",
        "pied-mention": "&copy; <span data-year>2026</span> Amélie &amp; Partners &middot; Paris &middot; Pháp &middot; Tư vấn chiến lược đầu tư bất động sản",
        "nav": [
            ("approche.html", "Phương pháp"),
            ("ressources.html", "Tài liệu"),
            ("accompagnements.html", "Dịch vụ"),
            ("temoignages.html", "Khách hàng nói gì"),
            ("a-propos.html", "Giới thiệu"),
            ("contact.html", "Liên hệ"),
        ],
        "drawer": [
            ("index.html", "Trang chủ"),
            ("approche.html", "Phương pháp"),
            ("accompagnements.html", "Dịch vụ"),
            ("temoignages.html", "Khách hàng nói gì"),
            ("ressources.html", "Tài liệu"),
            ("a-propos.html", "Giới thiệu"),
            ("diagnostic.html", "Diagnostic Stratégique"),
            ("contact.html", "Liên hệ"),
        ],
        "pied-explorer-liens": [
            ("approche.html", "Phương pháp", "reperes"),
            ("ressources.html", "Tài liệu", "livre"),
            ("accompagnements.html", "Dịch vụ", "duo"),
            ("temoignages.html", "Khách hàng nói gì", "guillemets"),
            ("a-propos.html", "Giới thiệu", "personne"),
        ],
        "pied-commencer-liens": [
            ("diagnostic.html", "Diagnostic Stratégique", "cible"),
        ],
        "pied-echange": "Buổi trao đổi đầu tiên",
        "pied-informations-liens": [
            ("contact.html", "Liên hệ", "telephone"),
            ("formulaire.html", "Viết cho chúng tôi", "mail"),
        ],
        "pied-legal": [
            ("mentions-legales.html", "Thông tin pháp lý (tiếng Pháp)", "document"),
            ("confidentialite.html", "Dữ liệu cá nhân (tiếng Pháp)", "bouclier"),
            ("cgv.html", "Điều khoản bán hàng (tiếng Pháp)", "document"),
        ],
    },
}
