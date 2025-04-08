## Jonathan Beltran Neri
# Algoritmo: Heurística para Búsqueda Informada

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
# Este archivo define la heurística estimada desde cada nodo hacia el objetivo 'T'.

# Definición del grafo (sin pesos, solo conexiones)
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

# Heurística estimada hacia el nodo objetivo 'T'
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

# Mostrar la heurística definida para cada nodo
print("Heurística estimada hacia el nodo 'T':")
for nodo in heuristica:
    print(f"{nodo} → {heuristica[nodo]}")
