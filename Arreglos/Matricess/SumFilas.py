
import random
M=[]
for i in range(3):
    M.append([0]*3)
for i in range(3):
    sf=0
    for j in range(3):
        M[i][j]=random.random()*10  
        sf+=M[i][j]
    print("La suma de la fila",i,"es: ",sf)
for i in M:
    print(i)
