import numpy as np
#Matrices
A = np.array([[9, 12, 17], [8, 15, 23], [9, 17, 8]])
B = np.array([[13, 25, 12], [23, 7,14], [3, 15, 32]])
#Suma
C = (A+B)
print(C)
#Resta
D = (A-B)
print(D)
#Multiplicacion punto a punto
E =np. dot(A, B)
print(E)
#Multiplicacion punto cruz
F = np.cross(A, B)
print(F)
#Division
G = (A/B)
print(G)