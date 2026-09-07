"""Genere des visuels provisoires abstraits aux couleurs de la marque.

ATTENTION : ce script ecrase les fichiers de assets/images/ portant les memes
noms. Il n'est utile que tant que les vraies photographies ne sont pas
arrivees. Ne pas le lancer ensuite.

    python3 outils/visuels-provisoires.py

Necessite Pillow :  pip install Pillow
"""
import math, random, os
from PIL import Image, ImageDraw, ImageFilter, ImageChops

RACINE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(RACINE, "assets", "images")
os.makedirs(OUT, exist_ok=True)

INK      = (18, 40, 60)
INK_SOFT = (29, 53, 73)
PAPER    = (248, 245, 239)
PAPER_S  = (239, 235, 228)
LAV      = (203, 181, 223)
LAV_D    = (117, 80, 143)
RUST     = (160, 82, 52)
WHITE    = (255, 255, 255)

def lerp(a, b, t):
    return tuple(int(round(a[i] + (b[i] - a[i]) * t)) for i in range(3))

def gradient(size, c1, c2, angle=35):
    w, h = size
    base = Image.new("RGB", (w, h))
    px = base.load()
    rad = math.radians(angle)
    dx, dy = math.cos(rad), math.sin(rad)
    # projection normalisee
    corners = [0 * dx + 0 * dy, w * dx + 0 * dy, 0 * dx + h * dy, w * dx + h * dy]
    lo, hi = min(corners), max(corners)
    step = 4
    for y in range(0, h, step):
        for x in range(0, w, step):
            t = ((x * dx + y * dy) - lo) / (hi - lo)
            c = lerp(c1, c2, t)
            for yy in range(y, min(y + step, h)):
                for xx in range(x, min(x + step, w)):
                    px[xx, yy] = c
    return base

def grain(size, strength=6, seed=0):
    """Grain fin et discret, applique ensuite a faible opacite."""
    rnd = random.Random(seed)
    w, h = size
    small = Image.new("L", (max(2, w // 2), max(2, h // 2)))
    small.putdata([rnd.randint(128 - strength, 128 + strength) for _ in range(small.width * small.height)])
    return small.resize(size, Image.BICUBIC)

def compose(name, size, palette, seed, style="facade"):
    rnd = random.Random(seed)
    c1, c2 = palette
    img = gradient(size, c1, c2, angle=rnd.choice([25, 35, 50, 120, 145]))
    w, h = size
    layer = Image.new("RGBA", size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer, "RGBA")

    accent = rnd.choice([LAV, LAV_D, RUST, WHITE])
    light = WHITE if sum(c1) < 330 else INK

    if style == "facade":
        # trames verticales facon facade haussmannienne
        cols = rnd.randint(5, 8)
        cw = w / cols
        for i in range(cols):
            if rnd.random() < 0.55:
                x0 = i * cw
                a = rnd.randint(8, 26)
                d.rectangle([x0, 0, x0 + cw * rnd.uniform(.5, 1.0), h], fill=light + (a,))
        rows = rnd.randint(4, 7)
        rh = h / rows
        for j in range(1, rows):
            d.line([(0, j * rh), (w, j * rh)], fill=light + (26,), width=max(1, w // 900))
    elif style == "arcs":
        for i in range(rnd.randint(3, 5)):
            r = rnd.uniform(.35, 1.1) * min(w, h)
            cx = rnd.uniform(-.1, 1.1) * w
            cy = rnd.uniform(-.1, 1.1) * h
            d.ellipse([cx - r, cy - r, cx + r, cy + r], outline=light + (rnd.randint(18, 40),), width=max(2, w // 420))
    elif style == "planes":
        for i in range(rnd.randint(3, 5)):
            x0 = rnd.uniform(-.2, .8) * w
            y0 = rnd.uniform(-.2, .8) * h
            d.polygon([
                (x0, y0),
                (x0 + rnd.uniform(.25, .7) * w, y0 - rnd.uniform(.05, .25) * h),
                (x0 + rnd.uniform(.25, .7) * w, y0 + rnd.uniform(.3, .8) * h),
                (x0, y0 + rnd.uniform(.35, .9) * h),
            ], fill=light + (rnd.randint(8, 20),))

    # Les masses sont floutees : on cherche une abstraction photographique,
    # pas un aplat graphique.
    soft = layer.filter(ImageFilter.GaussianBlur(max(w, h) / 90))
    img = Image.alpha_composite(img.convert("RGBA"), soft).convert("RGB")

    # Deux filets nets par-dessus, pour tenir la composition
    lines = Image.new("RGBA", size, (0, 0, 0, 0))
    ld = ImageDraw.Draw(lines, "RGBA")
    lx = rnd.uniform(.18, .78) * w
    ld.line([(lx, 0), (lx + rnd.uniform(-.06, .06) * w, h)], fill=accent + (rnd.randint(28, 55),), width=max(1, w // 900))
    ly = rnd.uniform(.28, .8) * h
    ld.line([(0, ly), (w, ly + rnd.uniform(-.04, .04) * h)], fill=light + (rnd.randint(16, 34),), width=max(1, w // 1100))
    img = Image.alpha_composite(img.convert("RGBA"), lines).convert("RGB")

    # lumiere radiale douce
    glow = Image.new("L", size, 0)
    gd = ImageDraw.Draw(glow)
    gx, gy = rnd.uniform(.15, .85) * w, rnd.uniform(.1, .6) * h
    gr = rnd.uniform(.45, .8) * max(w, h)
    gd.ellipse([gx - gr, gy - gr, gx + gr, gy + gr], fill=60)
    glow = glow.filter(ImageFilter.GaussianBlur(max(w, h) // 8))
    img = Image.composite(Image.new("RGB", size, light), img, glow.point(lambda v: int(v * .55)))

    # vignettage
    vig = Image.new("L", size, 0)
    vd = ImageDraw.Draw(vig)
    vd.ellipse([-w * .25, -h * .25, w * 1.25, h * 1.25], fill=255)
    vig = vig.filter(ImageFilter.GaussianBlur(max(w, h) // 10))
    img = Image.composite(img, Image.new("RGB", size, lerp(c1, INK, .45)), vig)

    # grain, applique a faible opacite
    noisy = ImageChops.overlay(img, Image.merge("RGB", [grain(size, 26, seed)] * 3))
    img = Image.blend(img, noisy, 0.16)

    path = os.path.join(OUT, name)
    img.save(path, "JPEG", quality=76, optimize=True, progressive=True)
    return path

NAVY   = (INK, INK_SOFT)
NAVY_L = (INK, LAV_D)
NAVY_R = (INK, RUST)
IVORY  = (PAPER, PAPER_S)
IVORY_L= (PAPER, LAV)
IVORY_R= (PAPER_S, RUST)
MIX    = (LAV_D, INK)

SPECS = [
    # heros — larges, bleu nuit (le texte blanc passe dessus)
    ("hero-accueil.jpg",          (1800, 1013), NAVY,   11, "facade"),
    ("hero-particuliers.jpg",     (1800, 1013), NAVY_L, 12, "planes"),
    ("hero-professionnels.jpg",   (1800, 1013), NAVY,   13, "planes"),
    ("hero-approche.jpg",         (1800, 1013), MIX,    14, "arcs"),
    ("hero-accompagnements.jpg",  (1800, 1013), NAVY,   15, "facade"),
    ("hero-diagnostic.jpg",       (1800, 1013), NAVY_R, 16, "planes"),
    ("hero-ressources.jpg",       (1800, 1013), NAVY_L, 17, "arcs"),
    ("hero-a-propos.jpg",         (1800, 1013), NAVY,   18, "facade"),
    ("hero-contact.jpg",          (1800, 1013), MIX,    19, "planes"),
    ("hero-mentions.jpg",         (1800,  810), NAVY,   20, "facade"),
    # cartes de public
    ("public-particuliers.jpg",   (1080, 1350), IVORY_L, 21, "facade"),
    ("public-professionnels.jpg", (1080, 1350), IVORY_R, 22, "planes"),
    # portraits
    ("portrait-amelie.jpg",       (1080, 1350), IVORY,   31, "arcs"),
    ("portrait-amelie-large.jpg", (1200, 1500), IVORY_L, 32, "arcs"),
    # accompagnements
    ("accompagnement-diagnostic.jpg",   (1320, 880), IVORY_L, 41, "planes"),
    ("accompagnement-financement.jpg",  (1320, 880), IVORY,   42, "facade"),
    ("accompagnement-recherche.jpg",    (1320, 880), IVORY_R, 43, "facade"),
    ("accompagnement-trajectoire.jpg",  (1320, 880), IVORY_L, 44, "arcs"),
    # approche
    ("approche-methode.jpg",  (1280, 960), IVORY,   51, "facade"),
    ("approche-capital.jpg",  (1280, 960), IVORY_L, 52, "arcs"),
    ("approche-principes.jpg",(1280, 960), IVORY_R, 53, "planes"),
    # particuliers
    ("particuliers-premier-achat.jpg", (1280, 960), IVORY_L, 61, "facade"),
    ("particuliers-locatif.jpg",       (1280, 960), IVORY,   62, "planes"),
    ("particuliers-arbitrage.jpg",     (1280, 960), IVORY_R, 63, "arcs"),
    # professionnels
    ("professionnels-dirigeant.jpg",   (1280, 960), IVORY,   71, "planes"),
    ("professionnels-murs.jpg",        (1280, 960), IVORY_L, 72, "facade"),
    ("professionnels-structuration.jpg",(1280, 960), IVORY_R, 73, "arcs"),
    # galerie Paris
    ("paris-01.jpg", (840, 1120), IVORY_L, 81, "facade"),
    ("paris-02.jpg", (840, 1120), IVORY,   82, "arcs"),
    ("paris-03.jpg", (840, 1120), IVORY_R, 83, "facade"),
    ("paris-04.jpg", (840, 1120), IVORY_L, 84, "planes"),
    # ressources
    ("ressource-3-effets.jpg",  (1500, 844), IVORY_L, 91, "arcs"),
    ("ressource-couverture.jpg",(1500, 844), IVORY_R, 92, "planes"),
    # bandeaux et partage
    ("cta-fond.jpg",  (1800, 810), NAVY,   95, "facade"),
    ("contact-echange.jpg", (1280, 960), IVORY_L, 96, "arcs"),
    ("og-image.jpg",  (1200, 630), NAVY_L, 99, "planes"),
]

total = 0
for name, size, pal, seed, style in SPECS:
    p = compose(name, size, pal, seed, style)
    total += os.path.getsize(p)
print(len(SPECS), "visuels,", round(total / 1024), "Ko au total")
