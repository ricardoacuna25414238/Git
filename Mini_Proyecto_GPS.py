
import heapq  # sirve para sacar siempre la ciudad con menor tiempo


# ======================================================
# PARTE 1: EL GRAFO PONDERADO
# ======================================================
class Grafo:
    def __init__(self):
        # Diccionario de diccionarios.
        # Significa: de Lima a Ica hay 180 minutos.
        self.conexiones = {}

    def agregar_ciudad(self, ciudad):
        """Agrega una ciudad nueva (si no existe todavía)."""
        if ciudad not in self.conexiones:
            self.conexiones[ciudad] = {}

    def existe_ciudad(self, ciudad):
        return ciudad in self.conexiones

    def agregar_ruta(self, origen, destino, minutos):
        """Agrega una autopista entre dos ciudades (va y viene)."""
        # Si la ciudad no existe, la creamos
        self.agregar_ciudad(origen)
        self.agregar_ciudad(destino)

        # Guardamos la autopista en las dos direcciones
        self.conexiones[origen][destino] = minutos
        self.conexiones[destino][origen] = minutos

    def listar_ciudades(self):
        """Devuelve las ciudades ordenadas por nombre."""
        return sorted(self.conexiones.keys())

    def vecinos(self, ciudad):
        """Devuelve las ciudades conectadas directamente a otra."""
        return self.conexiones[ciudad]


# ======================================================
# PARTE 2: ALGORITMO DE DIJKSTRA
# ======================================================
def dijkstra(grafo, inicio, fin):
    """
    Busca la ruta más rápida entre inicio y fin.
    Devuelve (tiempo_total, lista_de_ciudades).
    Si no hay camino, devuelve (None, []).
    """
    # Al principio todas las ciudades están a "infinito" minutos
    tiempos = {}
    for ciudad in grafo.conexiones:
        tiempos[ciudad] = float("inf")
    tiempos[inicio] = 0  # de la ciudad inicial a ella misma son 0 minutos

    # Aquí guardamos de qué ciudad venimos (para armar la ruta al final)
    anterior = {}

    # Cola de prioridad: siempre sale la ciudad con menos tiempo
    cola = [(0, inicio)]

    while len(cola) > 0:
        tiempo_actual, ciudad_actual = heapq.heappop(cola)

        # Si ya llegamos al destino, podemos parar
        if ciudad_actual == fin:
            break

        # Si encontramos antes un camino mejor, ignoramos este
        if tiempo_actual > tiempos[ciudad_actual]:
            continue

        # Revisamos todas las ciudades vecinas
        for vecino, minutos in grafo.vecinos(ciudad_actual).items():
            nuevo_tiempo = tiempo_actual + minutos

            # ¿Este camino es más rápido que el que ya teníamos?
            if nuevo_tiempo < tiempos[vecino]:
                tiempos[vecino] = nuevo_tiempo
                anterior[vecino] = ciudad_actual
                heapq.heappush(cola, (nuevo_tiempo, vecino))

    # Si el tiempo sigue en infinito, no hay camino
    if tiempos[fin] == float("inf"):
        return None, []

    # Reconstruimos la ruta yendo hacia atrás desde el destino
    ruta = []
    ciudad = fin
    while ciudad != inicio:
        ruta.append(ciudad)
        ciudad = anterior[ciudad]
    ruta.append(inicio)
    ruta.reverse()  # la dimos vuelta, así que la volteamos otra vez

    return tiempos[fin], ruta


# ======================================================
# PARTE 3: INTERFAZ DE CONSOLA
# ======================================================
def pedir_ciudad(mensaje):
    """Pide una ciudad al usuario y revisa que no esté vacía."""
    nombre = input(mensaje).strip().title()
    if nombre == "":
        raise ValueError("El nombre de la ciudad no puede estar vacío.")
    return nombre


def mostrar_ciudades(grafo):
    ciudades = grafo.listar_ciudades()
    if len(ciudades) == 0:
        print("\nTodavía no hay ciudades registradas.")
        return

    print("\n--- Ciudades y sus autopistas ---")
    for ciudad in ciudades:
        print(f"{ciudad}:")
        for vecino, minutos in grafo.vecinos(ciudad).items():
            print(f"   -> {vecino} ({minutos} min)")


def agregar_ruta(grafo):
    print("\n--- Agregar ruta ---")
    origen = pedir_ciudad("Ciudad de origen: ")
    destino = pedir_ciudad("Ciudad de destino: ")

    if origen == destino:
        raise ValueError("El origen y el destino no pueden ser la misma ciudad.")

    texto = input("Tiempo en minutos: ").strip()
    try:
        minutos = int(texto)
    except ValueError:
        raise ValueError("El tiempo debe ser un número entero.")

    if minutos <= 0:
        raise ValueError("El tiempo debe ser mayor que 0.")

    grafo.agregar_ruta(origen, destino, minutos)
    print(f"Listo! Ruta agregada: {origen} <-> {destino} ({minutos} min)")


def consultar_ruta(grafo):
    print("\n--- Consultar ruta más rápida ---")
    inicio = pedir_ciudad("Ciudad de salida: ")
    fin = pedir_ciudad("Ciudad de llegada: ")

    if not grafo.existe_ciudad(inicio):
        raise ValueError(f"La ciudad '{inicio}' no existe.")
    if not grafo.existe_ciudad(fin):
        raise ValueError(f"La ciudad '{fin}' no existe.")
    if inicio == fin:
        raise ValueError("Ya estás en esa ciudad (0 minutos).")

    tiempo, ruta = dijkstra(grafo, inicio, fin)

    if tiempo is None:
        print(f"No hay ningún camino entre {inicio} y {fin}.")
    else:
        print("\nRuta más rápida:")
        print("  " + " -> ".join(ruta))
        print(f"Tiempo total: {tiempo} minutos")


def cargar_datos_de_ejemplo(grafo):
    """
    Datos iniciales de Nicaragua.
    """
    # Zona del Pacífico sur
    grafo.agregar_ruta("Managua", "Masaya", 30)
    grafo.agregar_ruta("Managua", "Granada", 55)
    grafo.agregar_ruta("Masaya", "Granada", 25)
    grafo.agregar_ruta("Managua", "Jinotepe", 60)
    grafo.agregar_ruta("Masaya", "Jinotepe", 45)
    grafo.agregar_ruta("Jinotepe", "Rivas", 50)
    grafo.agregar_ruta("Granada", "Rivas", 60)
    grafo.agregar_ruta("Rivas", "San Juan Del Sur", 30)

    # Zona del Pacífico norte
    grafo.agregar_ruta("Managua", "León", 90)
    grafo.agregar_ruta("León", "Chinandega", 50)

    # Zona norte y centro
    grafo.agregar_ruta("Managua", "Estelí", 150)
    grafo.agregar_ruta("Estelí", "Somoto", 70)
    grafo.agregar_ruta("Estelí", "Ocotal", 80)
    grafo.agregar_ruta("Managua", "Matagalpa", 130)
    grafo.agregar_ruta("Estelí", "Matagalpa", 90)
    grafo.agregar_ruta("Matagalpa", "Jinotega", 50)

    # Zona central y Caribe
    grafo.agregar_ruta("Managua", "Boaco", 90)
    grafo.agregar_ruta("Managua", "Juigalpa", 120)
    grafo.agregar_ruta("Boaco", "Juigalpa", 50)
    grafo.agregar_ruta("Juigalpa", "Rama", 240)
    grafo.agregar_ruta("Rama", "Bluefields", 120)  # este tramo es en lancha

    # Corn Island queda sin conectar a propósito (es una isla),
    # así podemos probar el caso "no hay camino"
    grafo.agregar_ciudad("Corn Island")


def mostrar_menu():
    print("\n===== SISTEMA DE NAVEGACIÓN GPS =====")
    print("1. Ver todas las ciudades")
    print("2. Agregar una ruta nueva")
    print("3. Consultar la ruta más rápida")
    print("4. Salir")


def main():
    grafo = Grafo()
    cargar_datos_de_ejemplo(grafo)

    while True:
        mostrar_menu()
        opcion = input("Elige una opción: ").strip()

        # try/except para que el programa no se caiga si algo sale mal
        try:
            if opcion == "1":
                mostrar_ciudades(grafo)
            elif opcion == "2":
                agregar_ruta(grafo)
            elif opcion == "3":
                consultar_ruta(grafo)
            elif opcion == "4":
                print("Hasta luego!")
                break
            else:
                print("Opción no válida, elige un número del 1 al 4.")
        except ValueError as error:
            print(f"Error: {error}")
        except (EOFError, KeyboardInterrupt):
            print("\nPrograma cerrado.")
            break


if __name__ == "__main__":
    main()