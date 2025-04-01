## Jonathan Beltran Neri
# Algoritmo: Búsqueda en Profundidad Iterativa (Iterative Deepening Search)

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
# El objetivo es encontrar un camino desde M hasta T combinando profundidad limitada con búsqueda progresiva.

# Subrutina: búsqueda en profundidad limitada
def busqueda_profundidad_limitada(grafo, nodo, objetivo, limite):
    if nodo == objetivo:
        return [nodo]
    if limite <= 0:
        return None
    for vecino in grafo.get(nodo, []):
        resultado = busqueda_profundidad_limitada(grafo, vecino, objetivo, limite - 1)
        if resultado:
            return [nodo] + resultado
    return None

# Algoritmo principal: profundidad iterativa
def busqueda_profundidad_iterativa(grafo, inicio, objetivo, limite_max):
    for limite in range(limite_max + 1):
        resultado = busqueda_profundidad_limitada(grafo, inicio, objetivo, limite)
        if resultado:
            return resultado
    return None

# Grafo sin pesos
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

# Ejecutar búsqueda
limite_maximo = 5
camino = busqueda_profundidad_iterativa(grafo, 'M', 'T', limite_maximo)
print("Camino encontrado:", camino)
