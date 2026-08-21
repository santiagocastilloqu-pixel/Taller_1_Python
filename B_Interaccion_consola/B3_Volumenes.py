#volumen de las diferentes figuras descritas por el profesor 
saludo=print("calculadora para hallar volumenes")
print("elige las siguientes opciones")
figuras="\n1 Prisma \n2 Piramide \n3 Cono Truncado \n4 Cilindro"
print(figuras)
opciones= int(input("ingrese la figura a calcular"))
if opciones== 1: 
    valor_1=float(input("ingrese el valor del area de la base"))
    valor_2=float(input("ingrese el valor de la altura del cuerpo"))
    volumen_prisma= valor_1*valor_2
    print(volumen_prisma)
elif opciones==2: 
    valor_3= float(input("ingrese el valor del area de la base"))
    valor_4=float(input("ingrese el valor de la altura de la piramide"))
    volumen_piramide= 1/3*valor_3*valor_4
    print(volumen_piramide)
elif opciones== 3: 
    valor_5=float(input("ingrese el valor de la altura del cono"))
    valor_6=float(input("ingrese el valor del radio de la base mayor"))
    valor_7=float(input("ingrese el valor del radio de la base menor"))

if valor_7 < valor_6:
    volumen_cono_trucado= 1/3*3.1416*valor_5*(valor_6**2+valor_7**2+valor_6*valor_7)
    print(volumen_cono_trucado)
elif opciones== 4:
    valor_8= float(input("ingrese el valor de la altura del cilindro"))
    valor_9= float(input("ingrese el valor del radio del cilindro"))
    volumen_cilindro= 3.1416*valor_9**2*valor_8
    print(volumen_cilindro)
