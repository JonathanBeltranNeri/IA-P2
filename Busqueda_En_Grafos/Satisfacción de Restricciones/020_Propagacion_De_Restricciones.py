## Jonathan Beltran Neri
# Algoritmo: Propagación de Restricciones (Constraint Propagation)

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
# Este algoritmo asigna valores a variables asegurándose que todas las restricciones
# se mantengan consistentes. Si una variable cambia su dominio, se revisan nuevamente
# sus vecinos para asegurar que también sigan siendo válidos. Este proceso se propaga recursivamente.

# Grafo de restricciones (bidireccional)
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

# Dominios posibles para cada nodo (colores en este ejemplo)
valores = ['Rojo', 'Verde', 'Azul']

# Función que aplica propagación de restricciones
def propagar_restricciones(grafo, dominios):
    cola = [(x, y) for x in grafo for y in grafo[x]]  # Todas las parejas de nodos conectados

    while cola:
        xi, xj = cola.pop(0)
        if revisar_dominio(xi, xj, dominios):
            if not dominios[xi]:  # Si un dominio queda vacío, no hay solución
                return False
            for xk in grafo[xi]:
                if xk != xj:
                    cola.append((xk, xi))  # Revisar de nuevo los vecinos de xi
    return True

# Revisa si hay que eliminar valores de xi según xj
def revisar_dominio(xi, xj, dominios):
    eliminado = False
    for valor in dominios[xi][:]:
        if not any(valor != otro for otro in dominios[xj]):
            dominios[xi].remove(valor)
            eliminado = True
    return eliminado

# Algoritmo principal que asigna valores usando propagación de restricciones
def propagacion_de_restricciones(grafo, valores):
    # Crear copia de dominios para cada nodo
    dominios = {nodo: list(valores) for nodo in grafo}

    # Aplicar propagación inicial
    if not propagar_restricciones(grafo, dominios):
        return None

    # Aplicar backtracking con dominios reducidos
    return backtracking_con_dominios({}, dominios, grafo)

# Backtracking usando los dominios propagados
def backtracking_con_dominios(asignacion, dominios, grafo):
    if len(asignacion) == len(grafo):
        return asignacion

    # Elegir la siguiente variable sin asignar
    for nodo in grafo:
        if nodo not in asignacion:
            break

    for valor in dominios[nodo]:
        # Verifica que no haya conflictos con los vecinos ya asignados
        if all(asignacion.get(vecino) != valor for vecino in grafo[nodo]):
            asignacion[nodo] = valor
            resultado = backtracking_con_dominios(asignacion.copy(), dominios, grafo)
            if resultado:
                return resultado

    return None  # No se pudo completar la asignación

# Ejecutar el algoritmo
solucion = propagacion_de_restricciones(grafo, valores)

# Mostrar resultado
print("Propagación de Restricciones (Constraint Propagation)")
if solucion:
    print("Solución encontrada:")
    for nodo, color in solucion.items():
        print(f"  {nodo}: {color}")
else:
    print("No se encontró una solución válida.")
