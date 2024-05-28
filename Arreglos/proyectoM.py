# Definición de funciones modulares

def actualizar_inventario(materiales, cantidades, nombre_material, cantidad, tipo):
    if nombre_material in materiales:
        indice = materiales.index(nombre_material)
        if tipo == "entrada":
            cantidades[indice] += cantidad
            print(f"Entrada registrada: {cantidad} de '{nombre_material}'. Cantidad actual: {cantidades[indice]}.")
        elif tipo == "salida":
            if cantidades[indice] >= cantidad:
                cantidades[indice] -= cantidad
                print(f"Salida registrada: {cantidad} de '{nombre_material}'. Cantidad actual: {cantidades[indice]}.")
            else:
                print(f"No hay suficiente cantidad de '{nombre_material}' en el inventario.")
    else:
        if tipo == "entrada":
            materiales.append(nombre_material)
            cantidades.append(cantidad)
            print(f"Material '{nombre_material}' agregado con cantidad {cantidad}.")
        else:
            print(f"El material '{nombre_material}' no existe en el inventario y no se puede registrar una salida.")


def mostrar_inventario(materiales, cantidades):
    print("\nInventario Actual:")
    print("-------------------")
    for i in range(len(materiales)):
        print(f"{materiales[i]}: {cantidades[i]} unidades")


# Función principal
def main():
    materiales = []
    cantidades = []

    while True:
        print("\nGestión de Inventario de Materiales de Construcción")
        print("1. Agregar material o registrar entrada")
        print("2. Registrar salida de material")
        print("3. Mostrar inventario")
        print("4. Salir")
        opcion = int(input("Elige una opción: "))

        if opcion == 1:
            nombre_material = input("Introduce el nombre del material: ")
            cantidad = int(input("Introduce la cantidad de entrada: "))
            actualizar_inventario(materiales, cantidades, nombre_material, cantidad, "entrada")
        elif opcion == 2:
            nombre_material = input("Introduce el nombre del material: ")
            cantidad = int(input("Introduce la cantidad de salida: "))
            actualizar_inventario(materiales, cantidades, nombre_material, cantidad, "salida")
        elif opcion == 3:
            mostrar_inventario(materiales, cantidades)
        elif opcion == 4:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, elige una opción del 1 al 4.")


# Ejecutar el programa
if __name__ == "__main__":
    main()

