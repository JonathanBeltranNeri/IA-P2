## Jonathan Beltran Neri
# Algoritmo: Temple Simulado (Simulated Annealing)

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
# aceptando, al inicio, algunos movimientos peores para evitar quedarse atrapado en máximos locales.

import random
import math

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

# Algoritmo de Temple Simulado
def temple_simulado(grafo, heuristica, inicio, objetivo, temperatura_inicial=10.0, enfriamiento=0.95):
    actual = inicio
    camino = [actual]
    temperatura = temperatura_inicial

    while temperatura > 0.1 and actual != objetivo:
        vecinos = grafo.get(actual, [])
        if not vecinos:
            break  # Si no hay vecinos, termina

        siguiente = random.choice(vecinos)  # Escoge un vecino aleatorio
        delta = heuristica[actual] - heuristica[siguiente]

        # Si mejora, acepta. Si no mejora, acepta con probabilidad según la temperatura
        if delta > 0 or random.random() < math.exp(delta / temperatura):
            camino.append(siguiente)
            actual = siguiente

        # Reduce la temperatura (enfriamiento)
        temperatura *= enfriamiento

    if actual == objetivo:
        return camino
    else:
        return None

# Ejecutar la búsqueda desde M hasta T
camino = temple_simulado(grafo, heuristica, 'M', 'T')

# Mostrar resultado
print("Búsqueda por Temple Simulado")
if camino:
    print("Camino encontrado:", camino)
else:
    print("No se encontró un camino hasta el objetivo.")
