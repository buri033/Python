numero = int(input("Ingresa un número entero para calcular su factorial: "))
resultado = 1
proceso = ""

if numero < 0:
    print("No se puede calcular el factorial de un número negativo.")
elif numero == 0:
    print("El factorial de 0 es 1.")
else:
    for i in range(1, numero + 1):
        resultado *= i
        proceso += str(i)
        if i < numero:
            proceso += "x"

    print("El factorial de", numero, "es", resultado, "y el proceso es:", proceso)
