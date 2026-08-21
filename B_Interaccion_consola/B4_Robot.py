print("Robot a escoger:\n1. Robot cartesiano\n2. Robot cilindrico\n3. Robot esférico")

elegir = input("Elija el tipo de robot: ")

if elegir == "1":
    print("El tipo de robot es cartesiano y sus articulaciones son 3 prismáticas")

elif elegir == "2":
    print("El tipo de robot es cilindrico y sus articulaciones son 1 rotacional y 2 prismáticas")

elif elegir == "3":
    print("El tipo de robot es esférico y sus articulaciones son 2 rotacionales y 1 prismática")

else:
    print("Opción no válida")