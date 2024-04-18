import random

A = []

for i in range(3):
    A.append([0] * 3)
print(A)
for i in range(3):
    for j in range(3):
        A[i][j] = random.randint(0, 15)
print("La matriz aleatoria creada es:")
for i in A:
    print(i)
