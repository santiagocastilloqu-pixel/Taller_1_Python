import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

print("Funcion de transferencia de segundo orden")
print("G(s) = K * wn^2 / (s^2 + 2*zeta*wn*s + wn^2)")

K = float(input("Ingrese la ganancia K: "))
wn = float(input("Ingrese la frecuencia natural wn: "))
zeta = float(input("Ingrese el factor de amortiguamiento zeta: "))

if wn <= 0:

    print("La frecuencia natural debe ser mayor que 0")

else:


    delta = (2 * zeta * wn)**2 - 4 * wn**2

    print("\nDiscriminante:", delta)

    # Determinar el tipo de sistema
    if zeta < 1 and zeta > 0:
        print("Sistema subamortiguado")

    elif zeta == 1:
        print("Sistema criticamente amortiguado")

    elif zeta > 1:
        print("Sistema sobreamortiguado")

    elif zeta == 0:
        print("Sistema sin amortiguamiento")

    else:
        print("Sistema inestable")


   
    numerador = [K * wn**2]

    
    denominador = [1, 2 * zeta * wn, wn**2]


    sistema = signal.TransferFunction(
        numerador,
        denominador
    )
    print("\nNumerador:", numerador)
    print("Denominador:", denominador)

    print("\nFuncion de transferencia:")
    print(sistema)

    tiempo, respuesta = signal.step(sistema)

    plt.plot(tiempo, respuesta)

    plt.title("Respuesta al escalon - Sistema de segundo orden")

    plt.xlabel("Tiempo (s)")
    plt.ylabel("Amplitud")

    plt.grid(True)

    plt.show()
