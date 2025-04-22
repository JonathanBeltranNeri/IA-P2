## Jonathan Beltran Neri
# Tema: Red Bayesiana

# Una red bayesiana es un modelo gráfico probabilístico que representa
# un conjunto de variables y sus dependencias condicionales mediante un grafo dirigido y acíclico (DAG).

# Grafo utilizado:
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

# Este grafo representa relaciones entre variables.
# Supongamos que cada nodo es una variable binaria (cierto / falso)
# y que cada una depende de sus padres, si los tiene.

# Definimos la estructura como una red bayesiana
red_bayesiana = {
    'M': [],
    'N': ['M'],
    'O': ['M'],
    'P': ['N'],
    'Q': ['N'],
    'R': ['O'],
    'S': ['R'],
    'T': ['P', 'Q', 'S']
}

# Mostrar estructura de dependencias condicionales
print("Red Bayesiana - Estructura del grafo como red probabilística\n")
for nodo in red_bayesiana:
    padres = red_bayesiana[nodo]
    if padres:
        print(f"  Nodo '{nodo}' depende de: {', '.join(padres)}")
    else:
        print(f"  Nodo '{nodo}' no depende de ningún otro (es raíz)")

# Ejemplo: interpretación
print("\nInterpretación:")
print("  - 'M' puede ser la causa principal (ej. evento inicial)")
print("  - 'T' depende de P, Q y S → combinación de caminos")
