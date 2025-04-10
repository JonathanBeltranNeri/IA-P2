## Jonathan Beltran Neri
# Algoritmo: Búsqueda de Haz (Beam Search)

# Estructura del grafo utilizado:
#
#         M
#        / \
#       N   O
#      / \    \
#     P   Q    R
#      \  |     \
#       T T      S
#                |
#                T
#
# Este algoritmo recorre un grafo y busca una ruta desde un nodo inicial hasta uno objetivo
# limitando el número de nodos que se exploran en cada nivel.

import heapq

# Grafo no ponderado
grafo = {
    'M': ['N', 'O'],
    'N': ['P', 'Q'],
    'O': ['R'],
    'P': ['T'],
    'Q': ['T'],
    'R': ['S'],
    'S': ['T'],
    'T': []
}

# Heurística estimada hacia 'T'
heuristica = {
    'M': 4,
    'N': 3,
    'O': 3,
    'P': 1,
    'Q': 1,
    'R': 2,
    'S': 1,
    'T': 0
}

# Algoritmo de Búsqueda de Haz
def busqueda_de_haz(grafo, heuristica, inicio, objetivo, k=2):
    visitados = set()
    cola = [(heuristica[inicio], [inicio])]
    
    while cola:
        # Expandir hasta el número máximo de nodos (k)
        nodos_expandidos = []
        for _ in range(k):
            if not cola:
                break
            f, camino = heapq.heappop(cola)
            nodo = camino[-1]
            
            if nodo == objetivo:
                return camino
            
            if nodo not in visitados:
                visitados.add(nodo)
                for vecino in grafo.get(nodo, []):
                    if vecino not in visitados:
                        nueva_ruta = camino + [vecino]
                        nodos_expandidos.append((heuristica.get(vecino, float('inf')), nueva_ruta))
        
        # Ordenar y expandir los nodos con el menor valor de heurística
        nodos_expandidos.sort()
        for nodo in nodos_expandidos:
            heapq.heappush(cola, nodo)
    
    return None

# Ejecutar la búsqueda desde M hasta T
camino = busqueda_de_haz(grafo, heuristica, 'M', 'T')

# Mostrar resultado
print("Búsqueda de Haz")
if camino:
    print("Camino encontrado:", camino)
else:
    print("No se encontró un camino hasta el objetivo.")
