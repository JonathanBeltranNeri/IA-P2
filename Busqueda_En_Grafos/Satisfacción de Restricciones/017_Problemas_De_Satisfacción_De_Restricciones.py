## Jonathan Beltran Neri
# Algoritmo: Nombre del Subtema
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
# Este algoritmo no busca una ruta como tal, sino asignar valores a variables cumpliendo restricciones.
# Usaremos como ejemplo un problema tipo "coloración de grafos" donde ningún nodo adyacente puede tener el mismo color.

# Grafo representado por conexiones (restricciones entre variables)
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

# Colores disponibles para asignar
colores = ['Rojo', 'Verde', 'Azul']

# Algoritmo de satisfacción de restricciones (Backtracking simple)
def asignar_colores(grafo, colores, asignacion={}, nodo_actual=0):
    nodos = list(grafo.keys())
    if nodo_actual == len(nodos):
        return asignacion  # Se asignaron todos correctamente

    nodo = nodos[nodo_actual]
    for color in colores:
        # Verifica que ningún vecino tenga el mismo color
        if all(asignacion.get(vecino) != color for vecino in grafo[nodo]):
            asignacion[nodo] = color
            resultado = asignar_colores(grafo, colores, asignacion.copy(), nodo_actual + 1)
            if resultado:
                return resultado

    return None  # No se pudo asignar sin violar restricciones

# Ejecutar asignación
asignacion_final = asignar_colores(grafo, colores)

# Mostrar resultado
print("Problemas de Satisfacción de Restricciones (CSP)")
if asignacion_final:
    print("Asignación encontrada:")
    for nodo, color in asignacion_final.items():
        print(f"  {nodo}: {color}")
else:
    print("No se encontró una asignación válida.")
