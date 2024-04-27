#promedio de una matriz
import random
M=[]
for i in range(5):
    M.append([0]*3)

#ahora genero la matriz aleatoria
for i in range(5):
    for j in range(3):
        M[i][j]=random.randint(1,50)
for i in M:
    print(i)

#ahora calculo el promedio

suma=0
for i in range(5):
    for j in range(3):
        suma+=M[i][j]
promedio=suma/(5*3)
print("El promedio de la matriz es: ",promedio)