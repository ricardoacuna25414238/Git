"""
Unidad 9 - Árboles Binarios de Búsqueda
Tarea: eliminar, BFS, suma, es_completo y balancear_arbol
"""
from collections import deque


class Nodo:
    """Nodo de un árbol binario."""

    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None


class ArbolBinarioBusqueda:
    """Árbol Binario de Búsqueda (BST)."""

    def __init__(self):
        self.raiz = None

    # ---------- Inserción e inorden (base para probar) ----------
    def insertar(self, valor):
        self.raiz = self._insertar_rec(self.raiz, valor)

    def _insertar_rec(self, nodo, valor):
        if nodo is None:
            return Nodo(valor)
        if valor < nodo.valor:
            nodo.izquierdo = self._insertar_rec(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            nodo.derecho = self._insertar_rec(nodo.derecho, valor)
        # Si el valor ya existe no se inserta (sin duplicados)
        return nodo

    def inorden(self):
        resultado = []
        self._inorden_rec(self.raiz, resultado)
        return resultado

    def _inorden_rec(self, nodo, resultado):
        if nodo is not None:
            self._inorden_rec(nodo.izquierdo, resultado)
            resultado.append(nodo.valor)
            self._inorden_rec(nodo.derecho, resultado)

    def altura(self, nodo):
        if nodo is None:
            return -1
        return 1 + max(self.altura(nodo.izquierdo), self.altura(nodo.derecho))

    # ---------- Ejercicio 1: eliminar ----------
    def eliminar(self, valor):
        """Elimina un valor del árbol (si existe)."""
        self.raiz = self._eliminar_rec(self.raiz, valor)

    def _eliminar_rec(self, nodo, valor):
        if nodo is None:  # el valor no estaba en el árbol
            return None

        if valor < nodo.valor:
            nodo.izquierdo = self._eliminar_rec(nodo.izquierdo, valor)
        elif valor > nodo.valor:
            nodo.derecho = self._eliminar_rec(nodo.derecho, valor)
        else:
            # Caso 1: nodo hoja
            if nodo.izquierdo is None and nodo.derecho is None:
                return None
            # Caso 2: un solo hijo -> el hijo reemplaza al nodo
            if nodo.izquierdo is None:
                return nodo.derecho
            if nodo.derecho is None:
                return nodo.izquierdo
            # Caso 3: dos hijos -> usar el sucesor inorden
            # (el menor valor del subárbol derecho)
            sucesor = nodo.derecho
            while sucesor.izquierdo is not None:
                sucesor = sucesor.izquierdo
            nodo.valor = sucesor.valor
            # Borrar el sucesor original del subárbol derecho
            nodo.derecho = self._eliminar_rec(nodo.derecho, sucesor.valor)
        return nodo

    # ---------- Ejercicio 2: recorrido por niveles (BFS) ----------
    def recorrido_por_niveles(self):
        """Retorna los valores nivel por nivel, usando una cola."""
        resultado = []
        if self.raiz is None:
            return resultado

        cola = deque([self.raiz])
        while cola:
            actual = cola.popleft()
            resultado.append(actual.valor)
            if actual.izquierdo is not None:
                cola.append(actual.izquierdo)
            if actual.derecho is not None:
                cola.append(actual.derecho)
        return resultado

    # ---------- Ejercicio 4: es_completo ----------
    def es_completo(self):
        """True si todos los nodos internos tienen exactamente 2 hijos."""
        return self._es_completo_rec(self.raiz)

    def _es_completo_rec(self, nodo):
        if nodo is None:
            return True  # un árbol vacío cumple
        if nodo.izquierdo is None and nodo.derecho is None:
            return True  # una hoja no es nodo interno
        if nodo.izquierdo is None or nodo.derecho is None:
            return False  # tiene solo un hijo
        return (self._es_completo_rec(nodo.izquierdo)
                and self._es_completo_rec(nodo.derecho))


# ---------- Ejercicio 3: suma de elementos (función externa) ----------
def suma_arbol(arbol):
    """Suma todos los elementos sin modificar el árbol."""
    return _suma_rec(arbol.raiz)


def _suma_rec(nodo):
    if nodo is None:
        return 0
    return nodo.valor + _suma_rec(nodo.izquierdo) + _suma_rec(nodo.derecho)


# ---------- Ejercicio 5: balancear ----------
def balancear_arbol(arbol):
    """Retorna un NUEVO BST balanceado con los elementos del original."""
    elementos = arbol.inorden()  # el inorden de un BST sale ordenado
    nuevo = ArbolBinarioBusqueda()
    nuevo.raiz = _construir_balanceado(elementos, 0, len(elementos) - 1)
    return nuevo


def _construir_balanceado(lista, inicio, fin):
    """Toma el elemento del medio como raíz y repite en cada mitad."""
    if inicio > fin:
        return None
    medio = (inicio + fin) // 2
    nodo = Nodo(lista[medio])
    nodo.izquierdo = _construir_balanceado(lista, inicio, medio - 1)
    nodo.derecho = _construir_balanceado(lista, medio + 1, fin)
    return nodo


# ---------- Pruebas ----------
if __name__ == "__main__":
    # Prueba de eliminar (los 3 casos)
    arbol = ArbolBinarioBusqueda()
    for x in [10, 5, 15, 2, 7, 12, 17]:
        arbol.insertar(x)
    print("Inorden inicial:   ", arbol.inorden())

    arbol.eliminar(2)    # caso 1: hoja
    print("Sin 2 (hoja):      ", arbol.inorden())
    arbol.insertar(1)
    arbol.eliminar(5)    # caso 2: un hijo (o dos según el árbol)
    print("Sin 5:             ", arbol.inorden())
    arbol.eliminar(10)   # caso 3: raíz con dos hijos
    print("Sin 10 (raíz):     ", arbol.inorden())

    # Prueba de BFS
    arbol2 = ArbolBinarioBusqueda()
    for x in [10, 5, 15, 2, 7, 12, 17]:
        arbol2.insertar(x)
    print("BFS:               ", arbol2.recorrido_por_niveles())

    # Prueba de suma
    print("Suma:              ", suma_arbol(arbol2))
    print("Inorden intacto:   ", arbol2.inorden())

    # Prueba de es_completo
    print("¿Completo? (arbol2)", arbol2.es_completo())
    arbol2.insertar(1)
    print("¿Completo? (con 1) ", arbol2.es_completo())

    # Prueba de balancear
    degenerado = ArbolBinarioBusqueda()
    for x in [1, 2, 3, 4, 5, 6, 7]:
        degenerado.insertar(x)
    print("Altura degenerado: ", degenerado.altura(degenerado.raiz))
    balanceado = balancear_arbol(degenerado)
    print("Altura balanceado: ", balanceado.altura(balanceado.raiz))
    print("BFS balanceado:    ", balanceado.recorrido_por_niveles())
