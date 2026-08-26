import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

Coeficientes de la funcion de transferencia
print("Funcion de transferencia de segundo orden")
print("Forma: G(s) = (b0s + b1) / (a0s^2 + a1*s + a2)")

b0 = float(input("Ingrese b0: "))
b1 = float(input("Ingrese b1: "))

a0 = float(input("Ingrese a0: "))
a1 = float(input("Ingrese a1: "))
a2 = float(input("Ingrese a2: "))

Verificar que sea de segundo orden
if a0 == 0:
print("Error: a0 no puede ser 0.")
else:
# Calculo del discriminante
delta = a1**2 - 4a0a2

print("\nDiscriminante:", delta)

# Clasificacion del sistema
if delta < 0:
print("Sistema subamortiguado")
elif delta == 0:
print("Sistema criticamente amortiguado")
else:
print("Sistema sobreamortiguado")

# Funcion de transferencia
numerador = [b0, b1]
denominador = [a0, a1, a2]

sistema = signal.TransferFunction(numerador, denominador)

# Respuesta al escalon
tiempo, respuesta = signal.step(sistema)

# Grafica
plt.plot(tiempo, respuesta)

plt.title("Respuesta al escalon de un sistema de segundo orden")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.grid(True)

plt.show()
