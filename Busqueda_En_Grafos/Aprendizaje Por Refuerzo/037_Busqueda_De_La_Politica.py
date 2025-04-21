## Jonathan Beltran Neri
# Algoritmo: Búsqueda de la Política

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
# A partir de la tabla Q(s, a) aprendida previamente, este algoritmo extrae
# la política óptima, es decir, qué acción tomar en cada estado.

# Grafo con recompensas
grafo = {
    'M': [('N', -1), ('O', -1)],
    'N': [('P', -1), ('Q', -1)],
    'O': [('R', -1)],
    'P': [('T', 10)],
    'Q': [('T', 10)],
    'R': [('S', -1)],
    'S': [('T', 10)],
    'T': []
}

# Simular tabla Q previamente aprendida
Q = {
    estado: {accion: 0 for accion, _ in grafo[estado]}
    for estado in grafo if grafo[estado]
}

# Asignar valores Q manuales simulando resultados previos
Q['M']['N'] = 6.1
Q['M']['O'] = 5.8
Q['N']['P'] = 7.0
Q['N']['Q'] = 6.7
Q['O']['R'] = 5.5
Q['P']['T'] = 9.0
Q['Q']['T'] = 8.7
Q['R']['S'] = 6.2
Q['S']['T'] = 8.5

# Derivar política óptima: elegir la acción con mayor Q(s, a)
politica_optima = {
    estado: max(Q[estado], key=Q[estado].get)
    for estado in Q
}

# Mostrar política
print("Búsqueda de la Política - Derivación desde Q(s, a)\n")
for estado in sorted(politica_optima.keys()):
    print(f"  Estado '{estado}' → Acción óptima: {politica_optima[estado]}")
