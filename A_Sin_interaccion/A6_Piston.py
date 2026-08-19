import math
print("CALCULO DE FUERZA DE UN CILINDRO NEUMATICO")
#Parametros del cilindro
presion = float(input("Ingrese la presion en bar: "))
diametro_piston = float(input("Ingrese el diametro del piston en mm: "))
diametro_vastago = float(input("Ingrese el diametro del vastago en mm: "))

# Conversion de unidades
presion_pa = presion * 100000
diametro_piston_m = diametro_piston / 1000
diametro_vastago_m = diametro_vastago / 1000

# Areas
area_piston = math.pi * (diametro_piston_m ** 2) / 4
area_vastago = math.pi * (diametro_vastago_m ** 2) / 4

# Fuerzas
fuerza_avance = presion_pa * area_piston
fuerza_retroceso = presion_pa * (area_piston - area_vastago)

print("Fuerza de avance:", fuerza_avance, "N")
print("Fuerza de retroceso:", fuerza_retroceso, "N")
