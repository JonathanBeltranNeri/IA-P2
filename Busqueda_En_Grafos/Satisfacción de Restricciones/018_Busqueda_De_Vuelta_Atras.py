## Jonathan Beltran Neri
# Algoritmo: Búsqueda de Vuelta Atrás (Backtracking)

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
# Este algoritmo intenta encontrar una asignación válida de valores para un conjunto de variables,
# retrocediendo (backtracking) cuando se viola alguna restricción, hasta hallar una solución completa.

# Grafo representado como variables relacionadas por restricciones (como en problemas de coloración)
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

# Valores posibles para asignar (ej. colores)
valores = ['Rojo', 'Verde', 'Azul']

# Algoritmo de Búsqueda de Vuelta Atrás
def vuelta_atras(asignacion, grafo, valores, nodo_actual):
    if nodo_actual == len(grafo):
        return asignacion  # Todas las variables fueron asignadas correctamente

    nodos = list(grafo.keys())
    nodo = nodos[nodo_actual]

    for valor in valores:
        # Verificar si el valor es válido para el nodo actual
        valido = True
        for vecino in grafo[nodo]:
            if vecino in asignacion and asignacion[vecino] == valor:
                valido = False
                break

        if valido:
            asignacion[nodo] = valor
            resultado = vuelta_atras(asignacion.copy(), grafo, valores, nodo_actual + 1)
            if resultado:
                return resultado

    return None  # No se encontró solución válida en este camino

# Ejecutar algoritmo
solucion = vuelta_atras({}, grafo, valores, 0)

# Mostrar resultado
print("Búsqueda de Vuelta Atrás (Backtracking)")
if solucion:
    print("Solución encontrada:")
    for nodo, valor in solucion.items():
        print(f"  {nodo}: {valor}")
else:
    print("No se encontró una solución válida.")
