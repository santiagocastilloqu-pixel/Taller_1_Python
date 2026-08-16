#Para este ejercicio usaremos la ecuacion Callendar-Van Dusen (R = R0 * (1 + A*T + B*T**2))
#Donde R0 es la resistencia a 0°C, A y B son constantes de la ecuacion y T es la temperatura en grados Celsius.
import numpy as np
R0 = 100 #Resistencia a 0°C
A = 3.9083e-3 #Constante A
B = -5.775e-7 #Constante B
T = float(input("Ingresar temperatura en °C: ")) #Temperatura en 
#Calculo de la resistencia usando la ecuacion Callendar-Van Dusen
R = R0 * (1 + A*T + B*T**2)
print("La resistencia es:", R, "Ω")