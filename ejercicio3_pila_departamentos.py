"""
Ejercicio 3: Pila de departamentos de Nicaragua

Programa orientado a objetos que permite agregar, eliminar, buscar
e imprimir información de una pila de tipo string. La pila guarda los
nombres de los departamentos de Nicaragua. Cada operación está
implementada como un método de la clase PilaDepartamentos.
"""


class PilaDepartamentos:

    def __init__(self):
        self._elementos = []

    def agregar(self, departamento):
        self._elementos.append(departamento)
        print(f"'{departamento}' fue agregado a la pila.")

    def eliminar(self):
        if self.esta_vacia():
            print("La pila está vacía, no hay nada que eliminar.")
            return None
        departamento = self._elementos.pop()
        print(f"'{departamento}' fue eliminado de la pila.")
        return departamento

    def ver_cima(self):
        if self.esta_vacia():
            print("La pila está vacía.")
            return None
        print(f"El elemento en la cima es: {self._elementos[-1]}")
        return self._elementos[-1]

    def buscar(self):
        if self.esta_vacia():
            print("La pila está vacía, no se puede buscar.")
            return False
        
        departamento = input("ingrese el departamento que desea buscar")
            
        if departamento in self._elementos:
            print(f"'{departamento}' se encuentra en la pila.")
            return True
        print(f"'{departamento}' no se encuentra en la pila.")
        return False
    
    def contar(self):
        print(f"La pila tiene {len(self._elementos)} elemento(s).")
        return len(self._elementos)

    def imprimir(self):
        if self.esta_vacia():
            print("La pila está vacía.")
            return
        print("Departamentos en la pila (de la cima a la base):")
        for departamento in reversed(self._elementos):
            print(f"  -> {departamento}")

    def limpiar(self):
        if self.esta_vacia():
           print ("La pila esta vacia, no hay nada que limpiar")
           return 
        self._elementos.clear()
        print("La pila ha sido limpiada.")

    def esta_vacia(self):
        return len(self._elementos) == 0


def mostrar_menu():
    print("\n****Menú de Opciones*****")
    print("1. Agregar un departamento")
    print("2. Eliminar un departamento")
    print("3. Mostrar el último elemento en la Cima")
    print("4. Buscar un departamento")
    print("5. Contar cuantos elementos tiene la Pila")
    print("6. Mostrar todos los elementos de la pila")
    print("7. Limpiar la Pila")
    print("8. Salir")


def main():
    pila = PilaDepartamentos()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            nombre = input("Ingrese el nombre del departamento: ").strip()
            if nombre:
                pila.agregar(nombre)
            else:
                print("Error: el nombre no puede estar vacío.")
        elif opcion == "2":
            pila.eliminar()
        elif opcion == "3":
            pila.ver_cima()
        elif opcion == "4":
            pila.buscar()
        elif opcion == "5":
            pila.contar()
        elif opcion == "6":
            pila.imprimir()
        elif opcion == "7":
            pila.limpiar()
        elif opcion == "8":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida, intente de nuevo.")


if __name__ == "__main__":
    main()
