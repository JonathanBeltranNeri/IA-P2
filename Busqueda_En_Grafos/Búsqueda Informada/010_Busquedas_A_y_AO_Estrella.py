## Jonathan Beltran Neri
# Algoritmos: Búsqueda A* y AO*

# Estructura del grafo para A*:
#
#         M
#        / \
#     (2)  (3)
#      N     O
#     / \     \
#  (2) (4)    (2)
#   P   Q      R
#    \  |       \
#   (1)(3)       (1)
#      T         S
#                \
#                T
#
# El objetivo es encontrar un camino desde 'M' hasta 'T' con el menor costo estimado usando heurística.

import heapq

# ========================
# A* (A estrella)
# ========================
grafo_a = {
    'M': [('N', 2), ('O', 3)],
    'N': [('P', 2), ('Q', 4)],
    'O': [('R', 2)],
    'P': [('T', 1)],
    'Q': [('T', 3)],
    'R': [('S', 1)],
    'S': [('T', 2)],
    'T': []
}

heuristica_a = {
    'M': 6,
    'N': 4,
    'O': 5,
    'P': 3,
    'Q': 2,
    'R': 4,
    'S': 1,
    'T': 0
}

def busqueda_a_estrella(grafo, heuristica, inicio, objetivo):
    cola = [(heuristica[inicio], 0, [inicio])]  # (f, g, camino)
    visitados = set()

    while cola:
        f, g, camino = heapq.heappop(cola)
        nodo = camino[-1]

        if nodo == objetivo:
            return camino, g

        if nodo not in visitados:
            visitados.add(nodo)

            for vecino, costo in grafo.get(nodo, []):
                if vecino not in visitados:
                    g_nuevo = g + costo
                    f_nuevo = g_nuevo + heuristica.get(vecino, 0)
                    heapq.heappush(cola, (f_nuevo, g_nuevo, camino + [vecino]))

    return None, None

# ========================
# AO* (AO estrella)
# ========================
grafo_ao = {
    'M': [['N', 'O']],   # Desde M, se deben resolver N y O (AND)
    'N': [['P']],
    'O': [['R']],
    'P': [['T']],
    'Q': [['T']],
    'R': [['S']],
    'S': [['T']],
    'T': []
}

heuristica_ao = {
    'M': 5,
    'N': 3,
    'O': 2,
    'P': 1,
    'Q': 1,
    'R': 2,
    'S': 1,
    'T': 0
}

def busqueda_ao_estrella(grafo, heuristica, nodo_actual):
    if nodo_actual not in grafo or grafo[nodo_actual] == []:
        return [nodo_actual]

    mejor_opcion = []
    mejor_costo = float('inf')

    for opcion in grafo[nodo_actual]:  # opción: lista AND de subnodos
        costo_total = 0
        solucion = []

        for subnodo in opcion:
            sub_solucion = busqueda_ao_estrella(grafo, heuristica, subnodo)
            solucion.extend(sub_solucion)
            costo_total += heuristica.get(subnodo, 0)

        if costo_total < mejor_costo:
            mejor_costo = costo_total
            mejor_opcion = [nodo_actual] + solucion

    return mejor_opcion

# ========================
# Ejecutar A*
# ========================
camino_a, costo = busqueda_a_estrella(grafo_a, heuristica_a, 'M', 'T')
print("Búsqueda A*")
if camino_a:
    print("Camino encontrado:", camino_a)
    print("Costo total:", costo)
else:
    print("No se encontró un camino hasta el objetivo.")
print()

# ========================
# Ejecutar AO*
# ========================
camino_ao = busqueda_ao_estrella(grafo_ao, heuristica_ao, 'M')
print("Búsqueda AO*")
if camino_ao:
    print("Camino encontrado:", camino_ao)
else:
    print("No se encontró un camino hasta el objetivo.")
