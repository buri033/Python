#Suponga que la universidad x requiere un algoritmo que le permita generar la liquidacion de matricula para un estudiantes
# de acuerdo con las isguientes condiciones: 1. Si los ingresos familiares en el último año fueron superiores a
# $100.000.000 el valor a pagar por matricula es de $12.000.000, 2. Si los ingresos son menores o iguales a $100.000.000 se
# liquidirá de acuerdo con el estrato de la vivienda así:
# a. Si el estrato es 2 o 3 se realizará un descuento del 80%
# b. Si el estrato es  4 se realizará un descuento del 30%
# c. Si el estrato es 5 se realizará un descuento del 5%
# d. Si el estrato es 6, no tendrá descuento
# e. Si el estrato es 1 tendrá derecho a una beca del 100%

liquidacion = 12000000
ingresos = float(input("Digite sus ingresos familiares: "))

if ingresos > 100000000:
    liquidacion= 12000000
else:
    estrato = int(input("Digite su estrato, mayor o igual a 1, o menor e igual que 6:"))
    if estrato == 2 or estrato == 3:
        liquidacion = liquidacion - liquidacion*0.8
    else:
        if estrato == 4:
            liquidacion = liquidacion - liquidacion*0.3
        else:
            if estrato == 5:
                liquidacion = liquidacion - liquidacion*0.05
            else:
                if estrato == 6:
                    liquidacion = liquidacion
                else:
                    liquidacion = 0
print("El valor a pagar por matricula es: ", liquidacion)