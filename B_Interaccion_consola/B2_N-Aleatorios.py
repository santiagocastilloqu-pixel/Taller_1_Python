import random
numeros_a_elegir= int(input("cantidad de numeros"))
valor1= int(input("ingrese el rango inicial"))
valor2= int(input("ingrese el rango final"))
rango= range(valor1, valor2)
aleatorio= random.choices(rango, k=numeros_a_elegir)
print("respuesta:", aleatorio)