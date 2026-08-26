import numpy as np
import matplotlib.pyplot as plt
V = float(input("Ingrese el voltaje (V): "))
C_micro = float(input("Ingrese la capacitancia (µF): "))
R = float(input("Ingrese la resistencia (Ω): "))
C = C_micro * 1e-6
tau = R * C
t = np.linspace(0, 5 * tau, 1000)
Vc_carga = V * (1 - np.exp(-t / tau))
Vc_descarga = V * np.exp(-t / tau)
print("\nRESULTADOS")
print(f"Voltaje: {V} V")
print(f"Capacitancia: {C_micro} µF")
print(f"Resistencia: {R} Ω")
print(f"Constante de tiempo τ = {tau:.6f} segundos")
plt.figure(figsize=(10, 6))
plt.plot(t, Vc_carga, label="Carga del capacitor")
plt.plot(t, Vc_descarga, label="Descarga del capacitor")
plt.title("Carga y descarga de un circuito RC")
plt.xlabel("Tiempo (s)")
plt.ylabel("Voltaje del capacitor (V)")
plt.grid(True)
