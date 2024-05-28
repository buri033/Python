def crear_sala(filas, columnas):
    # Crear una matriz vacía de dimensiones filas x columnas
    return [["" for i in range(columnas)] for i in range(filas)]


# Esta función crea una "sala" representada por una lista de listas (una matriz),
# donde cada elemento es una cadena vacía que representa un asiento vacío.

def mostrar_sala(sala):
    # Mostrar la sala con los nombres de los alumnos
    for fila in sala:
        for nombre in fila:
            if nombre == "":
                print("[Vacío]", end="\t")
            else:
                print(nombre, end="\t")
        print()  # Nueva línea al final de cada fila


# Esta función recorre la matriz y muestra cada asiento.
# Si el asiento está vacío, imprime "[Vacío]".
# Si hay un nombre en el asiento, imprime el nombre.

def agregar_alumno(sala, fila, columna, nombre):
    # Agregar el nombre del alumno en la posición especificada
    if sala[fila][columna] == "":
        sala[fila][columna] = nombre
    else:
        print("La posición ya está ocupada. Inténtalo de nuevo.")


# Esta función agrega el nombre de un alumno en una posición específica de la matriz.
# Si el asiento ya está ocupado, muestra un mensaje de error.

def eliminar_alumno(sala, fila, columna):
    # Eliminar el nombre del alumno en la posición especificada
    if sala[fila][columna] != "":
        sala[fila][columna] = ""
    else:
        print("La posición ya está vacía.")


# Esta función elimina el nombre de un alumno de una posición específica de la matriz.
# Si el asiento ya está vacío, muestra un mensaje indicando que no hay nadie que eliminar.

def main():
    filas = 5
    columnas = 3
    sala = crear_sala(filas, columnas)

    # Inicializa una sala con 5 filas y 3 columnas.

    while True:
        print("\nSala de Cómputo:")
        mostrar_sala(sala)

        # Muestra la sala actual en cada iteración del bucle.

        accion = input("\nElige una acción: 'agregar', 'eliminar' o 'salir': ").lower()
        if accion == 'salir':
            break
        elif accion == 'agregar' or accion == 'eliminar':
            try:
                fila = int(input("Introduce el número de fila (0-4): "))
                columna = int(input("Introduce el número de columna (0-2): "))
            except ValueError:
                print("Por favor, introduce números válidos.")
                continue

            # Solicita al usuario las coordenadas de la fila y la columna.
            # Si el usuario introduce un valor no numérico, muestra un error y vuelve a pedir los datos.

            if fila < 0 or fila >= filas or columna < 0 or columna >= columnas:
                print("Posición inválida. Inténtalo de nuevo.")
                continue

            # Verifica que las coordenadas estén dentro de los límites de la matriz.

            if accion == 'agregar':
                nombre = input("Introduce el nombre del alumno: ")
                agregar_alumno(sala, fila, columna, nombre)
            elif accion == 'eliminar':
                eliminar_alumno(sala, fila, columna)
        else:
            print("Acción inválida. Por favor, elige 'agregar', 'eliminar' o 'salir'.")

        # Según la acción del usuario, llama a la función correspondiente para agregar o eliminar un alumno.
        # Si la acción es inválida, muestra un mensaje de error.


if __name__ == "__main__":
    main()

# Llama a la función main para iniciar el programa.
# El programa seguirá ejecutándose en un bucle hasta que el usuario elija 'salir'.
