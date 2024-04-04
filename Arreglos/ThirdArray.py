#Crear un vector apartir de la suma de los dos primeros generados

import random

n = int(input("digita el rango del vector\n"))
A = [0] * n
B = [0] * n
R = [0] * n
print(A)

# Se genera vector A
for i in range(n):
    A[i] = random.randint(1, 100)
print("El primer vector creado fue: ", A)
print("*************************************")

# Se genera vector B
for i in range(n):
    B[i] = random.randint(1, 100)
print("El segundo vector creado fue: ", B)
print("*************************************")

#Aquí se genera el vector R con la suma de elementos de posiciones correspondientes

for i in range(n):
    R[i]= A[i]+B[i]
print("El tercer vector creado fue: ", R)
