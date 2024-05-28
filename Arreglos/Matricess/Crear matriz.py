M=[]
for i in range(3):
    M.append([0]*3)
print(M)
#recorremos por filas
for i in range(3):
    for j in range(3):
        e=int(input("Ingrese un valor entero"))
        M[i][j]=e
print("La matriz creada es: ", M)
for i in M:
    print(i)

#recorremos por columnas
for j in range(3):
    for i in range(3):
        e=int(input("Ingrese un valor entero"))
        M[i][j]=e
print("La matriz creada es: ", M)
for i in M:
    print(i)