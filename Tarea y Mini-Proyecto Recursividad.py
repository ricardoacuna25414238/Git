"""
Recursividad - Práctica en clase, Tarea y Mini-Proyecto
Estudiante de segundo año - Estructuras de Datos / Algoritmos
"""

# =====================================================================
# 5. PRÁCTICA EN CLASE
# =====================================================================

def countdown(n):
    """Cuenta hacia atrás desde n e imprime 'Despegue!' al llegar a 0."""
    # Caso base: llegamos a cero
    if n == 0:
        print("Despegue!")
        return
    # Caso recursivo: imprimo n y sigo con n-1
    print(n)
    countdown(n - 1)


def invertir(cadena):
    """Invierte una cadena recursivamente."""
    # Caso base: cadena vacía
    if cadena == "":
        return ""
    # Caso recursivo: invierto el resto y pongo el primer caracter al final
    return invertir(cadena[1:]) + cadena[0]


def potencia(a, b):
    """Calcula a^b (b entero >= 0)."""
    # Caso base: cualquier número elevado a 0 es 1
    if b == 0:
        return 1
    # Caso recursivo: a^b = a * a^(b-1)
    return a * potencia(a, b - 1)


def es_palindromo(palabra):
    """Verifica si una palabra es palíndromo."""
    # Caso base: vacía o de 1 letra siempre es palíndromo
    if len(palabra) <= 1:
        return True
    # Caso recursivo: extremos iguales Y el interior también es palíndromo
    return palabra[0] == palabra[-1] and es_palindromo(palabra[1:-1])


def maximo(lista):
    """Encuentra el máximo de una lista no vacía."""
    if len(lista) == 0:
        raise ValueError("La lista no puede estar vacía")
    # Caso base: un solo elemento, ese es el máximo
    if len(lista) == 1:
        return lista[0]
    # Caso recursivo: comparo el primero con el máximo del resto
    return max(lista[0], maximo(lista[1:]))


# =====================================================================
# 6. TAREA
# =====================================================================

# --- 1. Multiplicación rusa (sin usar *) ---------------------------
def multiplicacion_rusa(a, b):
    """
    Multiplica a y b (enteros, b >= 0) usando solo sumas (más la división
    entera entre 2 y el módulo, propios del método ruso).

    Idea: a*b = (2a) * (b//2)       si b es par
          a*b = a + (2a) * (b//2)   si b es impar
    """
    # Caso base: cualquier cosa por 0 es 0
    if b == 0:
        return 0
    # Caso recursivo: duplico a (a + a) y reduzco b a la mitad
    if b % 2 == 0:
        return multiplicacion_rusa(a + a, b // 2)
    return a + multiplicacion_rusa(a + a, b // 2)


def multiplicar_simple(a, b):
    """Versión ingenua: a*b = a + a*(b-1). Solo sumas, b >= 0."""
    if b == 0:
        return 0
    return a + multiplicar_simple(a, b - 1)

# Análisis Big-O:
#  - multiplicacion_rusa: en cada llamada b se divide entre 2, así que hay
#    log2(b) llamadas. Cada una hace una suma => Tiempo O(log b).
#    Espacio (pila de recursión): O(log b).
#  - multiplicar_simple: b llamadas => Tiempo O(b), Espacio O(b).


# --- 2. Conteo de vocales -----------------------------------------
def contar_vocales(texto):
    """Cuenta las vocales (con o sin tilde) de un string."""
    # Caso base: string vacío, no hay vocales
    if texto == "":
        return 0
    # Caso recursivo: 1 si el primer caracter es vocal + vocales del resto
    es_vocal = 1 if texto[0].lower() in "aeiouáéíóúü" else 0
    return es_vocal + contar_vocales(texto[1:])


# --- 3. Imprimir patrón -------------------------------------------
def imprimir_patron(n):
    """Imprime un triángulo de asteriscos de n filas."""
    # Caso base: nada que imprimir
    if n == 0:
        return
    # Caso recursivo: primero imprimo las n-1 filas anteriores, luego la mía
    imprimir_patron(n - 1)
    print("*" * n)


# --- 4. Caminos en un tablero -------------------------------------
def caminos(filas, columnas):
    """
    Número de caminos de la esquina superior izquierda a la inferior
    derecha de una matriz filas x columnas, moviéndose solo abajo/derecha.
    """
    # Caso base: si solo hay 1 fila o 1 columna, hay un único camino
    if filas == 1 or columnas == 1:
        return 1
    # Caso recursivo: llego desde arriba o desde la izquierda
    return caminos(filas - 1, columnas) + caminos(filas, columnas - 1)


def caminos_memo(filas, columnas, memo=None):
    """Misma idea pero guardando resultados ya calculados (memoización)."""
    if memo is None:
        memo = {}
    if filas == 1 or columnas == 1:
        return 1
    if (filas, columnas) not in memo:
        memo[(filas, columnas)] = (caminos_memo(filas - 1, columnas, memo)
                                   + caminos_memo(filas, columnas - 1, memo))
    return memo[(filas, columnas)]

# Análisis Big-O (N filas, M columnas):
#  - caminos (ingenua): cada llamada genera 2 más y la profundidad máxima es
#    N+M-2, así que el árbol de llamadas crece como 2^(N+M)
#    => Tiempo O(2^(N+M)) (cota superior), Espacio O(N+M) por la pila.
#  - caminos_memo: solo hay N*M estados distintos y cada uno se calcula una
#    vez => Tiempo O(N*M), Espacio O(N*M).


# --- 5. Flatten list ----------------------------------------------
def flatten(lista):
    """Aplana una lista con listas anidadas a cualquier nivel."""
    # Caso base: lista vacía -> resultado vacío
    if not lista:
        return []
    primero, resto = lista[0], lista[1:]
    # Caso recursivo A: el primero es una lista -> la aplano y sigo con el resto
    if isinstance(primero, list):
        return flatten(primero) + flatten(resto)
    # Caso recursivo B: el primero es un entero -> lo dejo y sigo con el resto
    return [primero] + flatten(resto)


# =====================================================================
# 7. MINI-PROYECTO: EXPLORADOR DE DIRECTORIOS
# =====================================================================

class ExploradorRecursivo:
    """Recorre recursivamente un sistema de archivos (dict anidado)."""

    def imprimir_arbol(self, sistema, nivel=0):
        """Muestra la estructura con indentación según el nivel."""
        # Caso base implícito: si el dict está vacío, el for no itera
        for nombre, contenido in sistema.items():
            indentacion = "    " * nivel
            if isinstance(contenido, dict):
                # Es carpeta: imprimo y bajo un nivel (caso recursivo)
                print(f"{indentacion}|-- [{nombre}]")
                self.imprimir_arbol(contenido, nivel + 1)
            else:
                # Es archivo (hoja): solo imprimo, no hay más recursión
                print(f"{indentacion}|-- {nombre} ({contenido})")

    def buscar_archivo(self, sistema, nombre):
        """Devuelve la ruta del archivo o None si no existe."""
        for clave, contenido in sistema.items():
            if isinstance(contenido, dict):
                # Caso recursivo: busco dentro de la carpeta
                ruta = self.buscar_archivo(contenido, nombre)
                if ruta is not None:
                    return f"{clave}/{ruta}"
            elif clave == nombre:
                # Caso base: encontré el archivo (hoja)
                return clave
        # Caso base: recorrí todo y no está
        return None

    def contar_archivos(self, sistema):
        """Cuenta los archivos (las carpetas no cuentan)."""
        total = 0
        for contenido in sistema.values():
            if isinstance(contenido, dict):
                # Caso recursivo: sumo los archivos de la subcarpeta
                total += self.contar_archivos(contenido)
            else:
                # Caso base: es un archivo, cuenta 1
                total += 1
        return total


# =====================================================================
# PRUEBAS
# =====================================================================
if __name__ == "__main__":
    print("--- Ej 1: countdown(3) ---")
    countdown(3)

    print("\n--- Ej 2: invertir ---")
    print(invertir("recursion"))                 # noisrucer

    print("\n--- Ej 3: potencia ---")
    print(potencia(2, 10), potencia(5, 0))       # 1024 1

    print("\n--- Ej 4: palindromo ---")
    print(es_palindromo("reconocer"), es_palindromo("python"))   # True False

    print("\n--- Ej 5: maximo ---")
    print(maximo([3, 9, 2, 15, 7]))              # 15

    print("\n--- Tarea 1: multiplicacion rusa ---")
    print(multiplicacion_rusa(13, 7), multiplicacion_rusa(25, 0), multiplicar_simple(6, 4))

    print("\n--- Tarea 2: vocales ---")
    print(contar_vocales("Murciélago"))          # 5

    print("\n--- Tarea 3: patron ---")
    imprimir_patron(3)

    print("\n--- Tarea 4: caminos ---")
    print(caminos(3, 3), caminos(3, 7), caminos_memo(18, 18))    # 6 28 2333606220

    print("\n--- Tarea 5: flatten ---")
    print(flatten([1, [2, [3, 4], 5]]))          # [1, 2, 3, 4, 5]

    print("\n--- Mini-proyecto ---")
    sistema_archivos = {
        "Documentos": {
            "apuntes.txt": "10kb",
            "fotos": {
                "vacaciones.png": "2mb",
                "perro.jpg": "1mb"
            }
        },
        "sistema.dll": "500kb"
    }
    explorador = ExploradorRecursivo()
    explorador.imprimir_arbol(sistema_archivos)
    print("Ruta de perro.jpg:", explorador.buscar_archivo(sistema_archivos, "perro.jpg"))
    print("Ruta de fantasma.exe:", explorador.buscar_archivo(sistema_archivos, "fantasma.exe"))
    print("Total de archivos:", explorador.contar_archivos(sistema_archivos))
