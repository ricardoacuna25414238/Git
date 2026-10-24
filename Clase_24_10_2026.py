class Digrafo:
    def __init__(self):
        # Diccionario: cada vértice guarda la lista de vértices a los que apunta
        self.adyacencia = {}
 
    def insertar_vertice(self, v):
        if v in self.adyacencia:
            return False
        self.adyacencia[v] = []
        return True
 
    def insertar_arista(self, origen, destino):
        self.insertar_vertice(origen)
        self.insertar_vertice(destino)
        if destino in self.adyacencia[origen]:
            return False
        self.adyacencia[origen].append(destino)
        return True
 
    def buscar_vertice(self, v):
        return v in self.adyacencia
 
    def buscar_arista(self, origen, destino):
        return origen in self.adyacencia and destino in self.adyacencia[origen]
 
    def eliminar_arista(self, origen, destino):
        if not self.buscar_arista(origen, destino):
            return False
        self.adyacencia[origen].remove(destino)
        return True
 
    def eliminar_vertice(self, v):
        if v not in self.adyacencia:
            return False
        del self.adyacencia[v]
        for destinos in self.adyacencia.values():
            if v in destinos:
                destinos.remove(v)
        return True
 
    def leer(self):
        if not self.adyacencia:
            print("El grafo está vacío.")
            return
        for v, destinos in self.adyacencia.items():
            print(f"{v} -> {destinos}")
 
def main():
    g = Digrafo()
 
    print("1. INSERTAR vértices y aristas")
    for v in ["A", "B", "C", "D"]:
        g.insertar_vertice(v)
    g.insertar_arista("A", "B")
    g.insertar_arista("A", "C")
    g.insertar_arista("B", "D")
    g.insertar_arista("C", "D")
    g.insertar_arista("D", "A")
 
    print("\n2. LEER el grafo")
    g.leer()
 
    print("\n3. BUSCAR")
    print("¿Existe el vértice B?", g.buscar_vertice("B"))
    print("¿Existe la arista A -> B?", g.buscar_arista("A", "B"))
    print("¿Existe la arista B -> A?", g.buscar_arista("B", "A"))
 
    print("\n4. ELIMINAR la arista A -> C y el vértice D")
    g.eliminar_arista("A", "C")
    g.eliminar_vertice("D")
 
    print("\n5. LEER el grafo final")
    g.leer()
 
if __name__ == "__main__":
    main()