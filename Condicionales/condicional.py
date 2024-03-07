nota1= float(input("Ingrese la nota 1"))
nota2= float(input("Ingrese la nota 2"))
nota3= float(input("Ingrese la nota 3"))

n_final = (nota1+nota2+nota3)/3

print(n_final)

if n_final>= 4.6 and n_final<=5.0:
    print("Felicidades, ganaste en superior")
elif n_final>=3.9 and n_final<=4.5:
    print("Ganaste, felicitaciones")
elif n_final>=3.0 and n_final<=4.4:
    print("Ganaste, pero cuiado")
else:
    print("Perdiste:(")