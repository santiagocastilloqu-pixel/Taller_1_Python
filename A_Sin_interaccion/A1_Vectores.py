import numpy as np
#Vectores
A = np.array([8, 15, 23])
B = np.array([9, 17, 8])
#Suma
C = A+B
print(C)
#Resta
D = A-B
print(D)
#Multiplicaion punto a punto
E = np.dot(A, B)
print(E)
#Multiplicacion punto cruz
F = np.cross(A, B)
print(F)
#Division
G = (A/B)
print(G)