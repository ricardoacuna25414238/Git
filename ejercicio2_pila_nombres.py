"""
Ejercicio 2: Pila de nombres

Programa que permite guardar el primer nombre de las personas con:
1. Agregar un nombre a la Pila
2. Eliminar un nombre a la Pila
3. Mostrar el último elemento en la Cima
4. Buscar un elemento en la Pila
5. Contar cuantos elementos tiene la Pila
6. Mostrar todos los elementos de la pila
7. Limpiar la Pila
8. Salir
"""

pila = []


def agregar_nombre():
    nombre = input("Ingrese el primer nombre a agregar: ").strip()
    if nombre == "":
        print("Error: el nombre no puede estar vacío.")
        return
    pila.append(nombre)
    print(f"'{nombre}' fue agregado a la pila.")


def eliminar_nombre():
    if not pila:
        print("La pila está vacía, no hay nada que eliminar.")
        return
    nombre = pila.pop()
    print(f"'{nombre}' fue eliminado de la pila.")


def mostrar_cima():
    if not pila:
        print("La pila está vacía.")
        return
    print(f"El elemento en la cima es: {pila[-1]}")


def buscar_elemento():
    if not pila:
        print("La pila está vacía, no se puede buscar.")
        return
        
    nombre = input("Ingrese el nombre a buscar: ").strip()
    if nombre in pila:
        posicion = len(pila) - pila[::-1].index(nombre) - 1
        print(f"'{nombre}' se encontró en la pila (posición {posicion} desde la base).")
    else:
        print(f"'{nombre}' no se encontró en la pila.")


def contar_elementos():
    print(f"La pila tiene {len(pila)} elemento(s).")


def mostrar_elementos():
    if not pila:
        print("La pila está vacía.")
        return
    print("Elementos de la pila (de la cima a la base):")
    for nombre in reversed(pila):
        print(f"  -> {nombre}")


def limpiar_pila():
    if not pila:
        print("La pila ya está vacía, no hay nada que limpiar.")
        return
    pila.clear()
    print("La pila ha sido limpiada.")


def mostrar_menu():
    print("\n****Menú de Opciones*****")
    print("1. Agregar un nombre a la Pila")
    print("2. Eliminar un nombre a la Pila")
    print("3. Mostrar el último elemento en la Cima")
    print("4. Buscar un elemento en la Pila")
    print("5. Contar cuantos elementos tiene la Pila")
    print("6. Mostrar todos los elementos de la pila")
    print("7. Limpiar la Pila")
    print("8. Salir")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_nombre()
        elif opcion == "2":
            eliminar_nombre()
        elif opcion == "3":
            mostrar_cima()
        elif opcion == "4":
            buscar_elemento()
        elif opcion == "5":
            contar_elementos()
        elif opcion == "6":
            mostrar_elementos()
        elif opcion == "7":
            limpiar_pila()
        elif opcion == "8":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    main()
