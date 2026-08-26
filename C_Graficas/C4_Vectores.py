import matplotlib
matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
import numpy as np
valores= input("Escriba los valores del vector por separado:")
numeros=[int(x) for x in valores.split()]
vector= np.array(numeros)
x= vector[0]
y= vector[1]
z= vector[2]
figura= plt.figure()
eje= figura.add_subplot(111, projection="3d")
eje.quiver(0,0,0,x,y,z)
eje.set_xlabel("Eje X")
eje.set_ylabel("Eje Y")
eje.set_zlabel("Eje Z")
eje.set_title("Ejercicio Vector")
eje.set_xticks(np.arange(-6, 7, 1))
eje.set_yticks(np.arange(-6, 7, 1))
eje.set_zticks(np.arange(-6, 7, 1))
plt.show()
