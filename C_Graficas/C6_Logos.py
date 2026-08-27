import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

# ------------------- CONFIGURACION -------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RUTA_LOGO_1 = os.path.join(BASE_DIR, "imagenes", "hyunday.png")
RUTA_LOGO_2 = os.path.join(BASE_DIR, "imagenes", "logow.jpg")

RESULTADOS_DIR = os.path.join(BASE_DIR, "resultados")
os.makedirs(RESULTADOS_DIR, exist_ok=True)

UMBRAL = 127
# -------------------------------------------------------


def obtener_contornos(ruta_imagen, umbral=127):
    imagen = cv2.imread(ruta_imagen, cv2.IMREAD_UNCHANGED)
    if imagen is None:
        raise FileNotFoundError(f"No se pudo abrir la imagen: {ruta_imagen}")

    if imagen.shape[2] == 4:
        alfa = imagen[:, :, 3]
        _, binaria = cv2.threshold(alfa, umbral, 255, cv2.THRESH_BINARY)
        bgr = imagen[:, :, :3]
        fondo_blanco = np.full_like(bgr, 255)
        mascara_3c = cv2.merge([alfa, alfa, alfa])
        imagen_mostrar = np.where(mascara_3c > 0, bgr, fondo_blanco)
    else:
        gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
        _, binaria = cv2.threshold(gris, umbral, 255, cv2.THRESH_BINARY_INV)
        imagen_mostrar = imagen

    contornos, _ = cv2.findContours(
        binaria, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE
    )

    puntos_x = []
    puntos_y = []
    for contorno in contornos:
        for punto in contorno:
            x, y = punto[0]
            puntos_x.append(x)
            puntos_y.append(y)

    return np.array(puntos_x), np.array(puntos_y), imagen_mostrar


def graficar_contorno(x, y, titulo, ax):
    ax.scatter(x, -y, s=1, c="blue")
    ax.set_title(titulo)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.axis("equal")
    ax.grid(True)


def main():
    x1, y1, img1 = obtener_contornos(RUTA_LOGO_1, UMBRAL)
    print(f"Logo 1 (hyunday.png): se encontraron {len(x1)} puntos de contorno")
    np.savetxt(os.path.join(RESULTADOS_DIR, "coordenadas_logo1.csv"),
               np.column_stack((x1, y1)), delimiter=",", header="X,Y", comments="")

    x2, y2, img2 = obtener_contornos(RUTA_LOGO_2, UMBRAL)
    print(f"Logo 2 (logow.jpg): se encontraron {len(x2)} puntos de contorno")
    np.savetxt(os.path.join(RESULTADOS_DIR, "coordenadas_logo2.csv"),
               np.column_stack((x2, y2)), delimiter=",", header="X,Y", comments="")

    fig, axs = plt.subplots(2, 2, figsize=(10, 10))

    axs[0, 0].imshow(cv2.cvtColor(img1.astype(np.uint8), cv2.COLOR_BGR2RGB))
    axs[0, 0].set_title("Logo 1 - Original")
    axs[0, 0].axis("off")

    graficar_contorno(x1, y1, "Logo 1 - Contorno (X, Y)", axs[0, 1])

    axs[1, 0].imshow(cv2.cvtColor(img2.astype(np.uint8), cv2.COLOR_BGR2RGB))
    axs[1, 0].set_title("Logo 2 - Original")
    axs[1, 0].axis("off")

    graficar_contorno(x2, y2, "Logo 2 - Contorno (X, Y)", axs[1, 1])

    plt.tight_layout()
    plt.savefig(os.path.join(RESULTADOS_DIR, "contornos_logos.png"), dpi=150)
    plt.show()


if __name__ == "__main__":
    main()