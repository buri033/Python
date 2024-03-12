#Restas sucesivas para hacer una división

cont=0

D= int(input("Escriba el dividendo"))
d= int(input("Escriba el divisor"))
R=D
while R>=d:
    R=R-d
    cont+=1 # es lo mismo que decir cont= cont+1
print(f"El cociente es:{cont} ")
print(f"El residuo es: {R} ")
print(f"El cociente es:{cont} y el residuo {R}")