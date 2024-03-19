#Hacer un programa que lea 15 numeros enteros encuentre el promedio de los que están entre 50 y 100
import random
suma = 0
contador = 0
for i in range(0,15):
    numero = random.randint(1,100)
    print(numero)
    if numero > 50 and numero <= 100:
       suma = suma+numero
       contador += 1

if contador > 0:
    promedio=suma/contador
    print("El promedio es: ", promedio)


