## Jonathan Beltran Neri
# Algoritmo: Búsqueda en Grafos (DFS usando pila explícita)

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
# usando una pila en lugar de recursión.

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

# Algoritmo de Búsqueda en Profundidad usando pila explícita
def busqueda_en_grafos(grafo, inicio, objetivo):
    pila = [(inicio, [inicio])]  # Cada elemento es (nodo_actual, camino_actual)
    visitados = set()

    while pila:
        nodo, camino = pila.pop()  # Último en entrar, primero en salir (LIFO)

        if nodo == objetivo:
            return camino

        if nodo not in visitados:
            visitados.add(nodo)

            for vecino in grafo.get(nodo, []):
                if vecino not in visitados:
                    pila.append((vecino, camino + [vecino]))

    return None  # Si no se encuentra el objetivo

# Ejecutar búsqueda desde M hasta T
camino = busqueda_en_grafos(grafo, 'M', 'T')

# Mostrar resultado
print("Búsqueda en Grafos (DFS con pila)")
if camino:
    print("Camino encontrado:", camino)
else:
    print("No se encontró un camino hasta el objetivo.")
