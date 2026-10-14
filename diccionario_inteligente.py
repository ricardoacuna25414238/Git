"""
Mini-Proyecto: Diccionario Inteligente
Diccionario con autocompletado usando un Árbol Binario de Búsqueda.
El BST guarda objetos Palabra ordenados alfabéticamente.
"""


class Palabra:
    """Guarda una palabra y su definición."""

    def __init__(self, texto, definicion):
        self.texto = texto
        self.definicion = definicion

    def clave(self):
        """Clave de comparación: minúsculas para ignorar mayúsculas."""
        return self.texto.lower()

    def __str__(self):
        return f"{self.texto}: {self.definicion}"


class Nodo:
    def __init__(self, palabra):
        self.palabra = palabra
        self.izquierdo = None
        self.derecho = None


class Diccionario:
    """BST de objetos Palabra, ordenado alfabéticamente."""

    def __init__(self):
        self.raiz = None
        self.cantidad = 0

    # ---------- Insertar ----------
    def insertar(self, palabra):
        self.raiz = self._insertar_rec(self.raiz, palabra)

    def _insertar_rec(self, nodo, palabra):
        if nodo is None:
            self.cantidad += 1
            return Nodo(palabra)
        if palabra.clave() < nodo.palabra.clave():
            nodo.izquierdo = self._insertar_rec(nodo.izquierdo, palabra)
        elif palabra.clave() > nodo.palabra.clave():
            nodo.derecho = self._insertar_rec(nodo.derecho, palabra)
        # Si ya existe, se ignora
        return nodo

    # ---------- Búsqueda exacta ----------
    def buscar(self, texto):
        """Retorna el objeto Palabra o None si no existe."""
        clave = texto.lower().strip()
        actual = self.raiz
        while actual is not None:
            if clave == actual.palabra.clave():
                return actual.palabra
            if clave < actual.palabra.clave():
                actual = actual.izquierdo
            else:
                actual = actual.derecho
        return None

    # ---------- Búsqueda por prefijo ----------
    def buscar_por_prefijo(self, prefijo):
        """Retorna la lista de Palabras que empiezan con el prefijo."""
        resultado = []
        self._prefijo_rec(self.raiz, prefijo.lower().strip(), resultado)
        return resultado

    def _prefijo_rec(self, nodo, prefijo, resultado):
        if nodo is None or prefijo == "":
            return
        clave = nodo.palabra.clave()
        inicio = clave[:len(prefijo)]  # lo que se compara con el prefijo

        # Si el prefijo es menor, nada a la derecha puede coincidir
        if prefijo <= inicio:
            self._prefijo_rec(nodo.izquierdo, prefijo, resultado)
        # Esta palabra coincide: va en orden alfabético (inorden)
        if inicio == prefijo:
            resultado.append(nodo.palabra)
        # Si el prefijo es mayor, nada a la izquierda puede coincidir
        if prefijo >= inicio:
            self._prefijo_rec(nodo.derecho, prefijo, resultado)

    # ---------- Listado en orden ----------
    def listar(self):
        resultado = []
        self._inorden_rec(self.raiz, resultado)
        return resultado

    def _inorden_rec(self, nodo, resultado):
        if nodo is not None:
            self._inorden_rec(nodo.izquierdo, resultado)
            resultado.append(nodo.palabra)
            self._inorden_rec(nodo.derecho, resultado)


# ---------- Datos iniciales (55 palabras) ----------
PALABRAS_INICIALES = [
    ("aurora", "Luz rosada que aparece en el cielo antes de salir el sol."),
    ("auto", "Vehículo de motor para transportar personas."),
    ("autonomía", "Capacidad de actuar o decidir por uno mismo."),
    ("autor", "Persona que crea una obra."),
    ("árbol", "Planta de tronco leñoso que se ramifica a cierta altura."),
    ("algoritmo", "Conjunto ordenado de pasos para resolver un problema."),
    ("array", "Estructura que guarda elementos en posiciones consecutivas."),
    ("atributo", "Variable que pertenece a un objeto."),
    ("base", "Parte inferior sobre la que se apoya algo."),
    ("bit", "Unidad mínima de información: 0 o 1."),
    ("bucle", "Estructura que repite instrucciones mientras se cumpla una condición."),
    ("byte", "Conjunto de 8 bits."),
    ("cadena", "Secuencia de caracteres."),
    ("clase", "Plantilla para crear objetos."),
    ("cola", "Estructura de datos FIFO: el primero en entrar es el primero en salir."),
    ("compilador", "Programa que traduce código fuente a lenguaje máquina."),
    ("consola", "Interfaz de texto para interactuar con el computador."),
    ("dato", "Información que procesa un programa."),
    ("depurar", "Buscar y corregir errores en un programa."),
    ("diccionario", "Estructura que asocia claves con valores."),
    ("escritorio", "Pantalla principal de un sistema operativo."),
    ("excepción", "Error que ocurre durante la ejecución de un programa."),
    ("función", "Bloque de código reutilizable que puede recibir parámetros."),
    ("grafo", "Conjunto de nodos conectados por aristas."),
    ("hash", "Función que convierte un dato en un número de tamaño fijo."),
    ("hoja", "Nodo de un árbol que no tiene hijos."),
    ("herencia", "Mecanismo por el que una clase adquiere atributos de otra."),
    ("imprimir", "Mostrar información en pantalla o papel."),
    ("iteración", "Cada repetición de un ciclo."),
    ("java", "Lenguaje de programación orientado a objetos."),
    ("lista", "Colección ordenada de elementos."),
    ("lógica", "Forma de razonar que sigue reglas válidas."),
    ("método", "Función que pertenece a una clase."),
    ("memoria", "Espacio donde el computador guarda datos temporalmente."),
    ("nodo", "Elemento de una estructura enlazada que guarda un dato."),
    ("objeto", "Instancia de una clase."),
    ("operador", "Símbolo que realiza una operación, como + o -."),
    ("pila", "Estructura de datos LIFO: el último en entrar es el primero en salir."),
    ("polimorfismo", "Capacidad de un método de comportarse distinto según el objeto."),
    ("programa", "Conjunto de instrucciones que ejecuta un computador."),
    ("python", "Lenguaje de programación de sintaxis simple y legible."),
    ("raíz", "Primer nodo de un árbol."),
    ("recursión", "Técnica en la que una función se llama a sí misma."),
    ("red", "Conjunto de computadores conectados entre sí."),
    ("script", "Archivo con instrucciones que se ejecutan en orden."),
    ("servidor", "Computador que ofrece servicios a otros."),
    ("tabla", "Organización de datos en filas y columnas."),
    ("ternario", "Que consta de tres elementos o partes."),
    ("usuario", "Persona que utiliza un sistema."),
    ("variable", "Espacio con nombre donde se guarda un valor."),
    ("vector", "Arreglo de una dimensión."),
    ("web", "Sistema de páginas conectadas por internet."),
    ("xml", "Lenguaje de marcado para describir datos."),
    ("yottabyte", "Unidad de almacenamiento enorme: 10^24 bytes."),
    ("zip", "Formato de archivo comprimido."),
]


def cargar_palabras(diccionario):
    """Carga las palabras en el BST.

    Se insertan desde el medio de la lista ordenada para que el
    árbol quede balanceado y no se vuelva una lista enlazada.
    """
    lista = sorted(PALABRAS_INICIALES, key=lambda p: p[0].lower())
    _cargar_balanceado(diccionario, lista, 0, len(lista) - 1)


def _cargar_balanceado(diccionario, lista, inicio, fin):
    if inicio > fin:
        return
    medio = (inicio + fin) // 2
    texto, definicion = lista[medio]
    diccionario.insertar(Palabra(texto, definicion))
    _cargar_balanceado(diccionario, lista, inicio, medio - 1)
    _cargar_balanceado(diccionario, lista, medio + 1, fin)


# ---------- Interfaz de consola ----------
def mostrar_menu():
    print("\n==============================")
    print("   DICCIONARIO INTELIGENTE")
    print("==============================")
    print("1. Buscar palabra exacta")
    print("2. Autocompletar (buscar por prefijo)")
    print("3. Ver diccionario completo")
    print("4. Salir")


def main():
    diccionario = Diccionario()
    cargar_palabras(diccionario)
    print(f"Se cargaron {diccionario.cantidad} palabras.")

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            texto = input("Palabra a buscar: ")
            palabra = diccionario.buscar(texto)
            if palabra:
                print(f"\n{palabra}")
            else:
                print(f"\nLa palabra '{texto}' no está en el diccionario.")

        elif opcion == "2":
            prefijo = input("Escribe el prefijo: ")
            if prefijo.strip() == "":
                print("\nDebes escribir al menos una letra.")
                continue
            resultados = diccionario.buscar_por_prefijo(prefijo)
            if resultados:
                print(f"\n{len(resultados)} palabra(s) con '{prefijo}':")
                for p in resultados:
                    print(f"  - {p.texto}")
            else:
                print(f"\nNo hay palabras que empiecen con '{prefijo}'.")

        elif opcion == "3":
            print("\n--- Diccionario completo ---")
            for p in diccionario.listar():
                print(p)

        elif opcion == "4":
            print("¡Hasta luego!")
            break

        else:
            print("\nOpción no válida, intenta de nuevo.")


if __name__ == "__main__":
    main()
