import matplotlib

matplotlib.use("TkAgg")

import matplotlib.pyplot as plt
import numpy as np

valores = input("Escriba los valores del vector por separado: ")

numeros = [int(x) for x in valores.split()]

vector = np.array(numeros)

x = vector[0]
y = vector[1]
z = vector[2]

mayor = max(abs(x), abs(y), abs(z))

limite = mayor + 2

figura = plt.figure()

eje = figura.add_subplot(111, projection="3d")

eje.quiver(
    0, 0, 0,
    x, y, z,
    color="blue",
    arrow_length_ratio=0.1
)

eje.set_xlabel("Eje X")
eje.set_ylabel("Eje Y")
eje.set_zlabel("Eje Z")

eje.set_title("Ejercicio Vector")


# Límites dinámicos
eje.set_xlim(-limite, limite)
eje.set_ylim(-limite, limite)
eje.set_zlim(-limite, limite)


plt.show()
