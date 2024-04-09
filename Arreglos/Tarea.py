#Generar un vector y hacer otro en el cual aparezcan los números del primero, pero al revés

import random

B = [0]*5
A = [0]*5

for i in range(5):
    B[i] = random.randint(0, 50)

print('El vector original es:', B)

# Invertir B en A
for i in range(5):
    A[i] = B[4 - i]

print('Vector invertido:',A)