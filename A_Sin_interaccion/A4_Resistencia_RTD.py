# Para este ejercicio usaremos la ecuacion Callendar-Van Dusen
# R = R0 * (1 + A*T + B*T**2 + C*(T - 100)*T**3)
import numpy as np

R0 = 100
A = 3.9083e-3
B = -5.775e-7
C = -4.183e-12

T = float(input("Ingresar temperatura en °C: "))

# Calculo de la resistencia
if T < 0:
    R = R0 * (1 + A*T + B*T**2 + C*(T - 100)*T**3)
else:
    R = R0 * (1 + A*T + B*T**2)

print("La resistencia es:", R, "Ω")
