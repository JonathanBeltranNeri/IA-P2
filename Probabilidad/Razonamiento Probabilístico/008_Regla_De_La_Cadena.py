## Jonathan Beltran Neri
# Tema: Regla de la Cadena

# La Regla de la Cadena permite descomponer la probabilidad conjunta de múltiples variables
# en una secuencia de probabilidades condicionales según una red bayesiana.

# Por ejemplo:
#     P(A, B, C) = P(A) * P(B | A) * P(C | A, B)

# Grafo utilizado como Red Bayesiana:
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

# Definimos dependencias condicionales
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

# Orden topológico posible según el grafo (padres antes que hijos)
orden = ['M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']

# Aplicar la regla de la cadena en esta secuencia
print("Regla de la Cadena - Descomposición de la probabilidad conjunta:\n")
print("P(M, N, O, P, Q, R, S, T) =")

expresion = []
for nodo in orden:
    padres = red_bayesiana[nodo]
    if padres:
        condicion = " | " + ", ".join(padres)
    else:
        condicion = ""
    expresion.append(f"P({nodo}{condicion})")

print("  " + " * ".join(expresion))
