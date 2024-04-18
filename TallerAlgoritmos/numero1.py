#Hacer un algoritmo que determine el número de dígitos que posee una cifra. Ejemplo:
#345 tiene 3 cifras, 12389 tiene 5 cifras

numero = int(input("Ingresa un número: "))
contador = 0

if numero == 0:
    contador = 1

while numero != 0:
    contador += 1
    numero //= 10

print(f"El número ingresado tiene {contador} cifras.")