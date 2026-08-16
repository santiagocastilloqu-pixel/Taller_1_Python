import numpy as np
# Coordenadas rectangulares
x = 7
y = 4
z = 5
#Coordenadas cilindricas
r = np.sqrt(x**2 + y**2)
theta = np.arctan2(y, x)
#Comversion a grados
theta_grados = np.degrees(theta)
print("Coordenadas cilindricas: r =", r, ", theta =", theta_grados, "grados, z =", z)
#Coordendas esfericas
rho = np.sqrt(x**2 + y**2 + z**2)
phi = np.arccos(z/rho)
#Conversion a grados
phi_grados = np.degrees(phi)
print("Coordenadas esfericas: rho =", rho, ", phi =", phi_grados, "grados, theta =", theta_grados, "grados")