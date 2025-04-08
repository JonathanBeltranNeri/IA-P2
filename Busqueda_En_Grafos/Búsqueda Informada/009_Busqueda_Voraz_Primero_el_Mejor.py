## Jonathan Beltran Neri
# Algoritmo: Búsqueda Voraz (Primero el Mejor)

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
# eligiendo siempre el vecino con la heurística más baja (más prometedor).

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

# Algoritmo de Búsqueda Voraz
def busqueda_voraz(grafo, heuristica, inicio, objetivo):
    cola = [(heuristica[inicio], [inicio])]  # Cola de prioridad: (heurística, camino)
    visitados = set()

    while cola:
        _, camino = heapq.heappop(cola)
        nodo = camino[-1]

        if nodo == objetivo:
            return camino

        if nodo not in visitados:
            visitados.add(nodo)

            for vecino in grafo.get(nodo, []):
                if vecino not in visitados:
                    nuevo_camino = camino + [vecino]
                    heapq.heappush(cola, (heuristica.get(vecino, float('inf')), nuevo_camino))

    return None

# Ejecutar búsqueda desde M hasta T
camino = busqueda_voraz(grafo, heuristica, 'M', 'T')
print("Camino encontrado:", camino)
