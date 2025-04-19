## Jonathan Beltran Neri
# Algoritmo: Salto Atrás Dirigido por Conflictos (Conflict-Directed Backjumping)

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
# Este algoritmo mejora el backtracking tradicional al detectar conflictos
# y "saltar hacia atrás" directamente al nodo que causó el problema, en lugar de retroceder uno por uno.

grafo = {
    'M': ['N', 'O'],
    'N': ['M', 'P', 'Q'],
    'O': ['M', 'R'],
    'P': ['N', 'T'],
    'Q': ['N', 'T'],
    'R': ['O', 'S'],
    'S': ['R', 'T'],
    'T': ['P', 'Q', 'S']
}

valores = ['Rojo', 'Verde', 'Azul']

# Función principal de Backjumping
def backjumping(asignacion, orden, nivel, grafo, valores, conflictos):
    if nivel == len(orden):
        return asignacion

    var = orden[nivel]
    for valor in valores:
        asignacion[var] = valor
        conflictos[var] = set()
        conflicto = False

        for vecino in grafo[var]:
            if vecino in asignacion and asignacion[vecino] == valor:
                conflictos[var].add(vecino)
                conflicto = True

        if not conflicto:
            resultado = backjumping(asignacion.copy(), orden, nivel + 1, grafo, valores, conflictos)
            if resultado:
                return resultado
        else:
            # Si hay conflicto, decide si hacer backjump o seguir probando valores
            continue

    # Si no hay más valores válidos, revisar a qué nivel saltar
    if conflictos[var]:
        salto = max(orden.index(c) for c in conflictos[var])
        return backjumping(asignacion.copy(), orden, salto, grafo, valores, conflictos)
    else:
        return None

# Ejecutar algoritmo
orden = list(grafo.keys())
conflictos = {}
solucion = backjumping({}, orden, 0, grafo, valores, conflictos)

# Mostrar resultado
print("Salto Atrás Dirigido por Conflictos (Conflict-Directed Backjumping)")
if solucion:
    print("Solución encontrada:")
    for nodo, color in solucion.items():
        print(f"  {nodo}: {color}")
else:
    print("No se encontró una solución válida.")
