import numpy as np

# Rotación en X
def rotacion_x(angulo):
    angulo_rad = np.radians(angulo)
    matriz = np.array([
        [1, 0, 0],
        [0, np.cos(angulo_rad), -np.sin(angulo_rad)],
        [0, np.sin(angulo_rad), np.cos(angulo_rad)]
    ])
    return matriz

# Rotación en Y
def rotacion_y(angulo):
    angulo_rad = np.radians(angulo)
    matriz = np.array([
        [np.cos(angulo_rad), 0, np.sin(angulo_rad)],
        [0, 1, 0],
        [-np.sin(angulo_rad), 0, np.cos(angulo_rad)]
    ])
    
    return matriz

# Rotación en Z
def rotacion_z(angulo):
    angulo_rad = np.radians(angulo)
    matriz = np.array([
        [np.cos(angulo_rad), -np.sin(angulo_rad), 0],
        [np.sin(angulo_rad), np.cos(angulo_rad), 0],
        [0, 0, 1]
    ])
    return matriz

#   Insertar el angulo de rotacion
Rx = rotacion_x(30)
Ry = rotacion_y(30)
Rz = rotacion_z(30)

print("Matriz de rotación en X:")
print(Rx)

print("\nMatriz de rotación en Y:")
print(Ry)

print("\nMatriz de rotación en Z:")
print(Rz)
