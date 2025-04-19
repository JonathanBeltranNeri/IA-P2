## Jonathan Beltran Neri 
## Algoritmo: Búsqueda Online (Online Search)
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
# Este algoritmo recorre un grafo y busca una ruta desde un nodo inicial hasta uno objetivo,
# tomando decisiones con base en la información local disponible en cada paso.
# No conoce el grafo completo desde el inicio.

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

# Algoritmo de Búsqueda Online
def busqueda_online(grafo, inicio, objetivo):
    actual = inicio
    camino = [actual]
    visitados = set()

    while actual != objetivo:
        visitados.add(actual)
        vecinos = grafo.get(actual, [])

        # Filtra vecinos ya visitados
        vecinos_no_visitados = [n for n in vecinos if n not in visitados]

        if not vecinos_no_visitados:
            return None  # Se queda sin opciones

        # Avanza al primer vecino disponible
        actual = vecinos_no_visitados[0]
        camino.append(actual)

    return camino

# Ejecutar la búsqueda desde M hasta T
camino = busqueda_online(grafo, 'M', 'T')

# Mostrar resultado
print("Búsqueda Online")
if camino:
    print("Camino encontrado:", camino)
else:
    print("No se encontró un camino hasta el objetivo.")
