#Hacer un algoritmo que muestre los primeros 20 números multiplos de 6
c=1
iteracion=0
for i in range(1,200, 1):
    if i%6==0 and c<=20:
        print(i)
        c=c+1
    iteracion=iteracion+1
print("elnumero de iteraciones realizadas fue", iteracion)
