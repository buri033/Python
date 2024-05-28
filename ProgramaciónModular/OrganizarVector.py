
import random

def crearV(n):
    B=[0]*n
    for i in range(n):
        B[i]=random.randint(0,200)
    return B


#principal
n=int(input("Ingrese el tamaño del vector: "))
B=crearV(n)
print("El vector creado es: ", B)

sortB=sorted(B)
print("El vector ordenado es: ", sortB)