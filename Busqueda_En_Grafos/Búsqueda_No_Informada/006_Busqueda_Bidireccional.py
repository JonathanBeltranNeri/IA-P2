## Jonathan Beltran Neri
# Algoritmo: Búsqueda Bidireccional (Bidirectional Search)

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
# Este algoritmo busca simultáneamente desde el nodo inicial hacia el objetivo
# y desde el objetivo hacia el inicio, encontrándose en el medio.

from collections import deque

def busqueda_bidireccional(grafo, inicio, objetivo):
    if inicio == objetivo:
        return [inicio]

    # Inicializamos las colas de ambos extremos
    cola_inicio = deque([[inicio]])
    cola_objetivo = deque([[objetivo]])

    # Visitados con rutas
    visitados_inicio = {inicio: [inicio]}
    visitados_objetivo = {objetivo: [objetivo]}

    while cola_inicio and cola_objetivo:
        # Desde el inicio
        camino_i = cola_inicio.popleft()
        nodo_i = camino_i[-1]
        if nodo_i in visitados_objetivo:
            return camino_i + visitados_objetivo[nodo_i][-2::-1]
        for vecino in grafo.get(nodo_i, []):
            if vecino not in visitados_inicio:
                visitados_inicio[vecino] = camino_i + [vecino]
                cola_inicio.append(visitados_inicio[vecino])

        # Desde el objetivo
        camino_o = cola_objetivo.popleft()
        nodo_o = camino_o[-1]
        if nodo_o in visitados_inicio:
            return visitados_inicio[nodo_o] + camino_o[-2::-1]
        for vecino in grafo.get(nodo_o, []):
            if vecino not in visitados_objetivo:
                visitados_objetivo[vecino] = camino_o + [vecino]
                cola_objetivo.append(visitados_objetivo[vecino])

    return None

# Grafo bidireccional
grafo = {
    'M': ['N', 'O'],
    'N': ['M', 'P', 'Q'],
    'O': ['M', 'R'],
    'P': ['N', 'T'],
    'Q': ['N', 'T'],
    'R': ['O', 'S'],
    'S': ['R', 'T'],
    'T': ['P', 'Q', 'S']
}

# Ejecutar búsqueda desde M hasta T
camino = busqueda_bidireccional(grafo, 'M', 'T')
print("Camino encontrado:", camino)
