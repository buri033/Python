import random
lista=[]
suma= 0
rango= int(input("How many numbers do you want?"))
for i in range(rango):
    lista.append(random.randint(1, 100))
    suma+=lista[i]
print(lista)
promedio= suma/10
print('La suma es: ', suma)
print('El promedio  es: ',promedio)

