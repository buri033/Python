# Crear un algoritmo que valide si un usuario puede entrar a una discoteca o no
# El algoritmo pedirá al usuario la edad, validará si la edad es mayor a 18
# y luego mostrará bienvenido a la discoteca si se cumple esta condición, de lo contrario mostrará no puedes ingresar


edad = int(input("Ingrese edad: "))
if edad>18:
    print("Bienvenido a la discoteca")
else:
    if edad >0:
        print("No puedes ingrsar a la discoteca, solo tienes: ", edad)
    else:
        print("Error en la edad")
