## Jonathan Beltran Neri
# Algoritmo: Ascensión de Colinas (Hill Climbing)

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
# Este algoritmo recorre un grafo y busca un camino desde un nodo inicial hasta uno objetivo
# avanzando siempre al vecino con la heurística más baja.

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

# Algoritmo de Ascensión de Colinas
def ascension_colinas(grafo, heuristica, inicio, objetivo):
    actual = inicio
    camino = [actual]

    while actual != objetivo:
        vecinos = grafo.get(actual, [])
        if not vecinos:
            break  # No hay a dónde ir

        # Elegir el vecino con la mejor heurística
        mejor_vecino = min(vecinos, key=lambda n: heuristica.get(n, float('inf')))

        # Solo avanza si mejora
        if heuristica[mejor_vecino] >= heuristica[actual]:
            break  # Máximo local

        actual = mejor_vecino
        camino.append(actual)

    if actual == objetivo:
        return camino
    else:
        return None  # No se encontró camino

# Ejecutar la búsqueda desde M hasta T
camino = ascension_colinas(grafo, heuristica, 'M', 'T')

# Mostrar resultado
print("Búsqueda por Ascensión de Colinas")
if camino:
    print("Camino encontrado:", camino)
else:
    print("No se encontró un camino hasta el objetivo.")
