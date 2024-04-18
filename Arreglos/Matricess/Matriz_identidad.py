n = int(input("Ingrese orden de la mtriz identidad\n"))
I = []
for i in range(n):
    I.append([0]*n)

for i in range(n):
    for j in range(n):
        if i==j:
            I[i][j]=1
        else:
            I[i][j]=0

print(f"Matriz identidad:\n{I}")
for i in I:
    print(i)