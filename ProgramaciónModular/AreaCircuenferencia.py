def Circunferencia(R):
    A = 3.1416 * R ** 2
    return A

Radio = float(input('Ingrese el radio de la circunferencia: '))
Area = Circunferencia(Radio)
print(f"El area de la circunferencia es: {Area}")