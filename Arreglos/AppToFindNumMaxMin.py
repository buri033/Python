import random

n = int(input("digita el rango del vector\n"))
A = [0] * n
print(A)
for i in range(n):
    A[i] = random.randint(1, 100)
print("El vector creado fue: ", A)
print("*************************************")
# Aquí encontramos el máximo
maximo = A[1]
for i in range(n):
    if A[i] > maximo:
        maximo = A[i]
print(f"el maximo valor es: {maximo}")
print('********************************************************')
# Aquí encontramos el minimo
minimo = A[1]
for i in range(n):
    if A[i] < minimo:
        maximo = A[i]
print(f"el minimo valor es: {maximo}")
