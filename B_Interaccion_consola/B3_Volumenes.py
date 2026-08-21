import math

print("--- Calculadora para hallar volúmenes ---")
print("Elige una de las siguientes opciones:")
print("1. Prisma\n2. Pirámide\n3. Cono Truncado\n4. Cilindro")

opcion = int(input("Ingrese el número de la figura a calcular: "))
if opcion == 1: 
    area_base = float(input("Ingrese el valor del área de la base: "))
    altura = float(input("Ingrese el valor de la altura del cuerpo: "))
    
    volumen_prisma = area_base * altura
    print(f"El volumen del prisma es: {volumen_prisma:.2f}")

elif opcion == 2: 
    area_base = float(input("Ingrese el valor del área de la base: "))
    altura = float(input("Ingrese el valor de la altura de la pirámide: "))
    volumen_piramide = (1/3) * area_base * altura
    print(f"El volumen de la pirámide es: {volumen_piramide:.2f}")

elif opcion == 3: 
    altura = float(input("Ingrese el valor de la altura del cono: "))
    radio_mayor = float(input("Ingrese el valor del radio de la base mayor: "))
    radio_menor = float(input("Ingrese el valor del radio de la base menor: "))
    if radio_menor < radio_mayor:
        volumen_cono_truncado = (1/3) * math.pi * altura * (radio_mayor**2 + radio_menor**2 + (radio_mayor * radio_menor))
        print(f"El volumen del cono truncado es: {volumen_cono_truncado:.2f}")
    else:
        print("Error: El radio menor debe ser estrictamente más pequeño que el radio mayor.")

elif opcion == 4:
    altura = float(input("Ingrese el valor de la altura del cilindro: "))
    radio = float(input("Ingrese el valor del radio del cilindro: "))
    volumen_cilindro = math.pi * (radio**2) * altura
    print(f"El volumen del cilindro es: {volumen_cilindro:.2f}")
else:
    print("Opción no válida. Por favor, reinicie el programa y elija un número del 1 al 4.")