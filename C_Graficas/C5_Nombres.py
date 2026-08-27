import os
import matplotlib.pyplot as plt
from matplotlib.textpath import TextPath
from matplotlib.font_manager import FontProperties
from matplotlib.patches import PathPatch

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RESULTADOS_DIR = os.path.join(BASE_DIR, "resultados")
os.makedirs(RESULTADOS_DIR, exist_ok=True)

INTEGRANTES = [
    "Juan Felipe Robles Herrera",
    "Felipe Ramirez Rojas",
    "Santiago Castillo Quiroga",
]


def dibujar_nombre(nombre, ax, y_pos, tamano=1, color="black"):
    fp = FontProperties(family="DejaVu Sans", style="normal", weight="bold")
    path = TextPath((0, y_pos), nombre, size=tamano, prop=fp)
    patch = PathPatch(path, facecolor=color, edgecolor=color, lw=0.5)
    ax.add_patch(patch)


def main():
    fig, ax = plt.subplots(figsize=(10, 6))

    fig.patch.set_facecolor("#1e1e2f")
    ax.set_facecolor("#1e1e2f")

    y = 0
    colores = ["#ffd166", "#06d6a0", "#ef476f"]
    for nombre, color in zip(INTEGRANTES, colores):
        dibujar_nombre(nombre, ax, y_pos=y, tamano=1.2, color=color)
        y -= 2

    ax.set_xlim(-1, 20)
    ax.set_ylim(y - 1, 3)
    ax.set_aspect("equal")
    ax.axis("off")
    ax.set_title("Integrantes del grupo - Taller 1 Python", fontsize=14, color="white")

    plt.tight_layout()
    plt.savefig(os.path.join(RESULTADOS_DIR, "nombres_grupo.png"), dpi=150,
                facecolor=fig.get_facecolor())
    plt.show()


if __name__ == "__main__":
    main()
