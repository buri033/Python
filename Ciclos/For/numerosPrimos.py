#Hacer un algoritmo que muestre los números primos desde 1 a 200
for i in range(1,201):
    c=0
    for j in range(1,i+1):
        if i%j==0:
            c=c+1
    if c==2:
         print(i)