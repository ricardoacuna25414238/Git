#Los entornos virtuales se cran para controlar el versionamiento de las librerias#
from collections import deque
import heapq
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# 1. Definición de la clase> Grafo
class Grafo:
    #Inicialización del la clase lista de adyacencia
    def __init__(self, dirigido = False):
        self.adyacencia = {}
        self.dirigido = dirigido
        
    def agregar_vertice(self, v):
        if v not in self.adyacencia:
            self.adyacencia[v] = []
            return True
        return False
    
    def agregar_arista(self, u, v):
        # Agrega una arista entre los vértices u y v
        self.agregar_vertice(u)
        self.agregar_vertice(v)
        
        self.adyacencia[u].append(v)
        if not self.dirigido:
            self.adyacencia[v].append(u)
    
    def vecinos (self, v):
        # Devuelve la lista de vecinos del vértice 
        return self.adyacencia.get(v, [])
    
    def bfs (self, inicio):
        # Recorrido de anchura del grafo
        visitados = set()
        cola = deque([inicio])
        resultado = []
        
        visitados.add(inicio)
        while cola:
            actual = cola.popleft()
            resultado.append(actual)
            
            for vecino in self.vecinos(actual):
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)
                    
        return resultado
    
    def dfs (self, inicio, visitados = None, resultado = None):
        # Recorrido en profundidad del grafo
        if visitados is None:
            visitados = set()
            resultado = []
            
        visitados.add(inicio)
        resultado.append(inicio)
        
        for vecino in self.vecinos(inicio):
            if vecino not in visitados:
                self.dfs(vecino, visitados, resultado)
                
        return resultado        
            
    def mostrar(self):
        #Mostrar grafo
        for vertice, vecinos in self.adyacencia.items():
            print(f"{vertice}: {vecinos}")
    
class GrafoPonderado(Grafo):
    def __init__(self, dirigido = False):
        super(). __init__(dirigido)
        #adyacencia sera un diccionario donde la clave es el vertice y el valor es una lista de tuplas (vecino, peso)
        
    def agregar_arista(self, u, v, peso):
        # Agrega una arista ponderada entre los vértices u y v 
        self.agregar_vertice(u)
        self.agregar_vertice(v)
        
        self.adyacencia[u].append((v, peso))
        if not self.dirigido:
            self.adyacencia[v].append((u, peso))
       
    def vecinos(self, v):
        # Devuelve la lista de vecinos del vértie junto con los pesos de compatibilidad
        return [(vecino, peso) for vecino, peso in self.adyacencia.get(v, [])]
    
    def dijkstra(self, inicio):
        # Algoritmo de Dijkstra para encontrar el camino más corto desde el vértice inicio a todos los demás vértices
        distancias = {vertice: float('infinity') for vertice in self.adyacencia}
        distancias[inicio] = 0
        pq = [(0, inicio)]  # Cola de prioridad (distancia, vértice)
        
        while pq:
            distancia_actual, vertice_actual = heapq.heappop(pq)
            
            if distancia_actual > distancias[vertice_actual]:
                continue
            
            for vecino, peso in self.vecinos(vertice_actual):
                distancia = distancia_actual + peso
                
                if distancia < distancias[vecino]:
                    distancias[vecino] = distancia
                    heapq.heappush(pq, (distancia, vecino))
                    
            return distancias        