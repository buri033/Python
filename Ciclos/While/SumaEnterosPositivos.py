sumap=0
num=int(input("Ingresa un numero entero positivos: ")) #variable sentinela
while num>=0:
    sumap=sumap+num
    num=int(input("Ingresa un entero positivo o, un negativo para salir: "))
print("La suma es: "+str(sumap))
print("Programa terminado")