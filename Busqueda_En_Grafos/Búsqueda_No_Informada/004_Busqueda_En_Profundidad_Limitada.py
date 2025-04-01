## Jonathan Beltran Neri
# Algoritmo: Búsqueda en Profundidad Limitada (Depth-Limited Search)

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
# El objetivo es encontrar un camino desde M hasta T sin superar un límite de profundidad.

def busqueda_profundidad_limitada(grafo, nodo, objetivo, limite):
    if nodo == objetivo:
        return [nodo]
    
    if limite <= 0:
        return None  # Límite alcanzado sin éxito

    for vecino in grafo.get(nodo, []):
        resultado = busqueda_profundidad_limitada(grafo, vecino, objetivo, limite - 1)
        if resultado:
            return [nodo] + resultado

    return None  # No se encontró el objetivo dentro del límite

# Definición del grafo
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

# Límite de profundidad
limite_maximo = 3

# Ejecutar búsqueda
camino = busqueda_profundidad_limitada(grafo, 'M', 'T', limite_maximo)
print("Camino encontrado:", camino)
