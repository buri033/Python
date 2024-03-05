a = float(input("Ingrese el tamaño del lado a \n"))
b = float(input("Ingrese el tamano del lado b \n"))
c = float(input("Ingrese el tamano del lado c \n"))

p = (a+b+c)/2

if(p-a) > 0 and (p-b) > 0 and (p-c) > 0:
    A = (p* (p-a) * (p-b) * (p-c))**(1/2)
    print("El area del triangulo es: ", A,"unidades cuadradas")
else:
    print("Medidas ingresadas no forman un triangulo")