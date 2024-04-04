n = int(input("digita el rango del vector\n"))
A = [0] * n
print(A)
for i in range(n):
    elemento = int(input("digite el elemento del vector\n"))
    A[i] = elemento
print("El vector creado fue: ", A)
