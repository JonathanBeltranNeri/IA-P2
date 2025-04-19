## Jonathan Beltran Neri
# Algoritmo: Acondicionamiento del Corte (Cutset Conditioning)

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
# Este algoritmo simplifica un problema de satisfacción de restricciones eliminando un conjunto
# pequeño de variables (cutset) para convertir el resto del grafo en una estructura sin ciclos.
# Luego prueba todas las combinaciones posibles del cutset para resolver el resto de forma eficiente.

import itertools

# Grafo bidireccional con restricciones entre nodos
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

# Valores posibles a asignar
valores = ['Rojo', 'Verde', 'Azul']

# Función que verifica si una asignación parcial es válida
def es_valida(asignacion, grafo):
    for nodo in asignacion:
        for vecino in grafo[nodo]:
            if vecino in asignacion and asignacion[nodo] == asignacion[vecino]:
                return False
    return True

# Backtracking clásico para el subgrafo sin ciclos
def backtracking_restante(asignacion, nodos_restantes, grafo, valores):
    if not nodos_restantes:
        return asignacion

    nodo = nodos_restantes[0]
    for valor in valores:
        nueva_asignacion = asignacion.copy()
        nueva_asignacion[nodo] = valor
        if es_valida(nueva_asignacion, grafo):
            resultado = backtracking_restante(nueva_asignacion, nodos_restantes[1:], grafo, valores)
            if resultado:
                return resultado
    return None

# Algoritmo principal de Acondicionamiento del Corte
def acondicionamiento_del_corte(grafo, valores, cutset):
    nodos = list(grafo.keys())
    nodos_restantes = [n for n in nodos if n not in cutset]

    # Todas las combinaciones posibles del cutset
    combinaciones = list(itertools.product(valores, repeat=len(cutset)))

    for combinacion in combinaciones:
        asignacion = dict(zip(cutset, combinacion))
        if es_valida(asignacion, grafo):
            resultado = backtracking_restante(asignacion, nodos_restantes, grafo, valores)
            if resultado:
                return resultado

    return None

# Definir un cutset (por simplicidad, seleccionamos nodos clave para romper ciclos)
cutset = ['N', 'S']

# Ejecutar algoritmo
solucion = acondicionamiento_del_corte(grafo, valores, cutset)

# Mostrar resultado
print("Acondicionamiento del Corte (Cutset Conditioning)")
if solucion:
    print("Solución encontrada:")
    for nodo, color in solucion.items():
        print(f"  {nodo}: {color}")
else:
    print("No se encontró una solución válida.")
