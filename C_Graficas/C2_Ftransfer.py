import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

print("Funcion de transferencia de segundo orden")
print("G(s) = (b0*s + b1) / (a0*s^2 + a1*s + a2)")

# Numerador
b0 = float(input("Ingrese b0: "))
b1 = float(input("Ingrese b1: "))

# Denominador
a0 = float(input("Ingrese a0: "))
a1 = float(input("Ingrese a1: "))
a2 = float(input("Ingrese a2: "))

if a0 == 0:
    print("a0 no puede ser 0")
else:
    delta = a1**2 - 4*a0*a2

    print("Discriminante:", delta)

    if delta < 0:
        print("Sistema subamortiguado")
    elif delta == 0:
        print("Sistema criticamente amortiguado")
    else:
        print("Sistema sobreamortiguado")

    numerador = [b0, b1]
    denominador = [a0, a1, a2]

    sistema = signal.TransferFunction(numerador, denominador)

    tiempo, respuesta = signal.step(sistema)

    plt.plot(tiempo, respuesta)
    plt.title("Respuesta al escalon")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")
    plt.grid(True)
    plt.show()
