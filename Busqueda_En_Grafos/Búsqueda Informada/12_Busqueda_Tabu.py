## Jonathan Beltran Neri
# Algoritmo: Búsqueda Tabú (Tabu Search)

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
# evitando repetir nodos recientes gracias a una lista tabú que restringe ciclos locales.

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

# Algoritmo de Búsqueda Tabú
def busqueda_tabu(grafo, heuristica, inicio, objetivo, tamano_tabu=3):
    actual = inicio
    camino = [actual]
    lista_tabu = []

    while actual != objetivo:
        vecinos = grafo.get(actual, [])
        vecinos_validos = [n for n in vecinos if n not in lista_tabu]

        if not vecinos_validos:
            break  # No hay movimiento válido

        # Seleccionamos el mejor vecino que no esté en la lista tabú
        siguiente = min(vecinos_validos, key=lambda n: heuristica.get(n, float('inf')))
        camino.append(siguiente)
        lista_tabu.append(actual)

        # Limitamos el tamaño de la lista tabú
        if len(lista_tabu) > tamano_tabu:
            lista_tabu.pop(0)

        actual = siguiente

    if actual == objetivo:
        return camino
    else:
        return None

# Ejecutar búsqueda desde M hasta T
camino = busqueda_tabu(grafo, heuristica, 'M', 'T')

# Mostrar resultado
print("Búsqueda Tabú")
if camino:
    print("Camino encontrado:", camino)
else:
    print("No se encontró un camino hasta el objetivo.")
