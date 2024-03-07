#Hacer un algoritmo que valide un usuario, el usuario será "Python", si se digita ese usuario debe mostrar
# "Bienvenido", de lo contrario volverá a pedir que ingrese un usuario

c = 0
while True:
    user = input("Digite un usuario: ")
    if user == "Python":
        print("Bienvenido")
        break
    else:
        c = c+1
    if c > 3:
        print("Se bloqueó el sistema")
        break
print("Programa ejecutado")