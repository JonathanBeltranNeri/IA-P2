## Jonathan Beltran Neri
# Algoritmo: Búsqueda en Profundidad (DFS - Depth-First Search)

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
# El objetivo es encontrar un camino desde M hasta T,
# recorriendo el grafo lo más profundo posible antes de retroceder.


def busqueda_profundidad(grafo, inicio, objetivo, visitados=None, camino=None):
    if visitados is None:
        visitados = set()  # Conjunto para registrar nodos visitados
    if camino is None:
        camino = [inicio]  # Lista para guardar el camino actual

    visitados.add(inicio)  # Marca el nodo como visitado

    if inicio == objetivo:
        return camino  # Si se llegó al objetivo, devuelve el camino

    for vecino in grafo.get(inicio, []):  # Recorre vecinos del nodo actual
        if vecino not in visitados:  # Solo visita si no ha sido visitado
            resultado = busqueda_profundidad(grafo, vecino, objetivo, visitados, camino + [vecino])
            if resultado:
                return resultado  # Si encuentra una solución, la retorna
    return None  # Si no encuentra el objetivo desde este camino


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

# Ejecuta la búsqueda desde M hasta T
resultado = busqueda_profundidad(grafo, 'M', 'T')
print("Camino encontrado:", resultado)
