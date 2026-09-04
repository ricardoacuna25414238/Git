"""
Ejercicio 1: Pila de números enteros

Programa que permite agregar números enteros a una pila y realizar:
1. Agregar números
2. Contar elementos
3. Mostrar todos los elementos
4. Promedio de todos los números
5. Salir del sistema
"""

pila = []


def agregar_numero():
    while True:
        try:
            numero = int(input("Ingrese un número entero: "))
            pila.append(numero)
            print(f"El número {numero} fue agregado a la pila.")
            break
        except ValueError:
            print("Error: debe ingresar un número entero válido.")


def contar_elementos():
    print(f"La pila tiene {len(pila)} elemento(s).")


def mostrar_elementos():
    if not pila:
        print("La pila está vacía.")
        return
    print("Elementos de la pila (de la cima a la base):")
    for elemento in reversed(pila):
        print(f"  -> {elemento}")


def calcular_promedio():
    if not pila:
        print("La pila está vacía, no se puede calcular el promedio.")
        return
    promedio = sum(pila) / len(pila)
    print(f"El promedio de los números es: {promedio:.2f}")


def mostrar_menu():
    print("\n****Menú de Opciones*****")
    print("1. Agregar números")
    print("2. Contar elementos")
    print("3. Mostrar todos los elementos")
    print("4. Promedio de todos los números")
    print("5. Salir del sistema")


def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_numero()
        elif opcion == "2":
            contar_elementos()
        elif opcion == "3":
            mostrar_elementos()
        elif opcion == "4":
            calcular_promedio()
        elif opcion == "5":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    main()
