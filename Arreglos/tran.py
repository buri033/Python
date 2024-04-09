import random
B=[0]*20
A=[0]*20

#generamos el vector original
for i in range(20):
    B[i]=random.randint(1,500)
print(B)
#aquí reorganizamos el vector pares y luego impares
j=0
for i in range(20):
    if B[i]%2==0:
        A[j]=B[i]
        j+=1
for i in range(20):
    if B[i]%2 != 0:
        A[j] = B[i]
        j += 1

print("Vector organizado(pares y luego impares", A)

