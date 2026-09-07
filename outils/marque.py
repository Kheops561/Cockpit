# -*- coding: utf-8 -*-
"""Marque Amélie & Partners : le tracé du logo.

Le logo est un entrelacs de quatre boucles. Chaque boucle part du centre, se
déploie vers l'exterieur et revient en se croisant elle-meme ; les brins des
boucles voisines se chevauchent et forment le noeud.

Le logo du site compte toujours quatre boucles et reste identique partout.
Le parametre `n` n'existe que pour reconstruire ce trace ; il n'a pas
vocation a produire des variantes publiees.

    python3 outils/marque.py     # affiche le SVG du logo
"""
import math


def lobe_path(n, i, cx=50.0, cy=50.0, rayon=38.0, ecart=11.0, largeur=20.0):
    """Chemin d'une boucle. Les deux brins partent de part et d'autre du
    centre : c'est leur chevauchement avec les boucles voisines qui produit
    l'entrelacs."""
    pas = 360.0 / n
    base = -90.0 + i * pas

    def pt(angle_deg, r):
        a = math.radians(angle_deg)
        return (cx + r * math.cos(a), cy + r * math.sin(a))

    # Les brins partent du côté opposé à celui vers lequel ils s'écartent :
    # la boucle se croise donc elle-même au niveau du col, comme le logo.
    depart = pt(base - 90, ecart)
    arrivee = pt(base + 90, ecart)
    pointe = pt(base, rayon)
    c1 = pt(base + largeur * 1.35, rayon * 0.78)
    c2 = pt(base + largeur * 0.72, rayon * 1.02)
    c3 = pt(base - largeur * 0.72, rayon * 1.02)
    c4 = pt(base - largeur * 1.35, rayon * 0.78)

    f = lambda p: f"{p[0]:.2f} {p[1]:.2f}"
    return (f"M{f(depart)} C{f(c1)} {f(c2)} {f(pointe)} "
            f"C{f(c3)} {f(c4)} {f(arrivee)}")


def marque(n=4, classe="mark", epaisseur=6.5, titre=None):
    """SVG de la marque."""
    chemins = []
    for i in range(n):
        chemins.append(f'    <path class="mark__lobe" d="{lobe_path(n, i)}"/>')
    role = (f'role="img" aria-label="{titre}"' if titre
            else 'role="presentation" aria-hidden="true"')
    return (f'<svg class="{classe}" viewBox="0 0 100 100" {role} focusable="false"\n'
            f'     fill="none" stroke="currentColor" stroke-width="{epaisseur}"\n'
            f'     stroke-linecap="round" stroke-linejoin="round">\n'
            + "\n".join(chemins) + "\n</svg>")


if __name__ == "__main__":
    import sys
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    if n != 4:
        print("Note : le logo du site compte quatre boucles.", file=sys.stderr)
    print(marque(n, titre="Amelie & Partners"))
