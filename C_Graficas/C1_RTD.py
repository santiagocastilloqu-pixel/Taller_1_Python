#Para este ejercicio usaremos la ecuacion Callendar-Van Dusen R = R0 * (1 + A*T + B*T**2 + C*(T - 100)*T**3)
#Donde R0 es la resistencia a 0°C, A ,B yC son constantes de la ecuacion y T es la temperatura en grados Celsius.
import numpy as np
import matplotlib.pyplot as plt
#Constantes
R0 = 100
A = 3.9083e-3
B = -5.775e-7
C = -4.183e-12
#Temperaturas
T= np.linspace(-200,200,401)
#Condiciones
R = np.where(
    T < 0,
    R0 * (1 + A*T + B*T**2 + C*(T - 100)*T**3),
    R0 * (1 + A*T + B*T**2)
)
#Grafica
plt.plot(T,R,color="red")
plt.title("Resistencia vs Temperatura",)
plt.xlabel("Temperatura (°C)",)
plt.ylabel("Resistencia (Ω)",)
plt.grid(True,color="black")
plt.show()