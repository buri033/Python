# Progama para crear un vector con el rango ingresado por el usuario
import random

List = []
rango = int(input("Enter a range for your list"))
for i in range(rango):
    List.append(random.randint(1, 100))
    # List.append(random.random())
print(List)
suma = 0
for i in range(rango):
    suma = suma + List[i]
    prom = suma / rango
print("El promedio es", prom)
