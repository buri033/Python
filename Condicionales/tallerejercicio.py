#Escribir un programa que pida al usuario dos números y muestre por pantalla su división.
# Si el divisor es cero el programa debe mostrar un error.

n1 = int(input("Ingrese un numero: "))
n2 = int(input("Ingrese un numero: "))
if n2 == 0:
    print("error parcero")
else:
    div = n1 / n2
    print(f"la division da: {div}")