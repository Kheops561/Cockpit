# -*- coding: utf-8 -*-
"""Marque Amélie & Partners : un nœud à N boucles.

Le logo de la marque est un entrelacs à quatre boucles. La construction est
ici paramétrée par le nombre de boucles, ce qui permet de l'accorder au
nombre d'étapes d'un schéma : quatre boucles pour quatre étapes, cinq pour
cinq, trois pour trois.
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


def marque(n=4, classe="mark", epaisseur=6.5, titre=None, etapes=False):
    """SVG de la marque. `etapes=True` numérote chaque boucle pour qu'un
    schéma puisse en allumer une à la fois."""
    chemins = []
    for i in range(n):
        attrs = f'class="mark__lobe"' + (f' data-lobe="{i}"' if etapes else '')
        chemins.append(f'    <path {attrs} d="{lobe_path(n, i)}"/>')
    role = (f'role="img" aria-label="{titre}"' if titre
            else 'role="presentation" aria-hidden="true"')
    return (f'<svg class="{classe}" viewBox="0 0 100 100" {role} focusable="false"\n'
            f'     fill="none" stroke="currentColor" stroke-width="{epaisseur}"\n'
            f'     stroke-linecap="round" stroke-linejoin="round">\n'
            + "\n".join(chemins) + "\n</svg>")


if __name__ == "__main__":
    import sys
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    if n < 2:
        raise SystemExit("Il faut au moins deux boucles.")
    print(marque(n, titre="Amelie & Partners"))
