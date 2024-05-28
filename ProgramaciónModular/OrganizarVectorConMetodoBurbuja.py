import random


def crearV(n):
    B = [0] * n
    for i in range(n):
        B[i] = random.randint(0, 200)
    return B


def burbuja(B, n):
    for i in range(n - 1):
        for j in range(n - 1):
            if B[j] > B[j + 1]:
                aux = B[j]
                B[j] = B[j + 1]
                B[j + 1] = aux
    print("El vector ordenado ascendiente es: ", B)
    return B


def burbujaDes(B, n):
    for i in range(n - 1):
        for j in range(n - 1):
            if B[j] < B[j + 1]:
                aux = B[j]
                B[j] = B[j + 1]
                B[j + 1] = aux
    print("El vector ordenado descendiente es es: ", B)
    return B


# principal
n = int(input("Ingrese el tamaño del vector: "))
B = crearV(n)
print("El vector creado es: ", B)
sortB = burbuja(B, n)
sortBdescenciente = burbujaDes(B, n)
