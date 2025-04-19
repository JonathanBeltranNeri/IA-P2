## Jonathan Beltran Neri
# Algoritmo: Búsqueda Local - Mínimos Conflictos (Min-Conflicts)

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
# Este algoritmo intenta resolver problemas de satisfacción de restricciones
# comenzando con una asignación aleatoria y luego haciendo pequeños ajustes
# para reducir el número de conflictos, hasta que se alcance una solución válida.

import random

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

# Colores posibles
valores = ['Rojo', 'Verde', 'Azul']

# Inicializa una asignación aleatoria
def asignacion_aleatoria(nodos, valores):
    return {nodo: random.choice(valores) for nodo in nodos}

# Cuenta cuántos conflictos tiene una asignación
def contar_conflictos(asignacion, grafo):
    conflictos = 0
    for nodo in grafo:
        for vecino in grafo[nodo]:
            if asignacion[nodo] == asignacion.get(vecino):
                conflictos += 1
    return conflictos // 2  # Se cuenta cada conflicto dos veces

# Encuentra el valor con menos conflictos para una variable
def mejor_valor_para(nodo, asignacion, grafo, valores):
    min_conflictos = float('inf')
    mejor_valor = None

    for valor in valores:
        asignacion_temp = asignacion.copy()
        asignacion_temp[nodo] = valor
        conflictos = contar_conflictos(asignacion_temp, grafo)
        if conflictos < min_conflictos:
            min_conflictos = conflictos
            mejor_valor = valor

    return mejor_valor

# Algoritmo principal de mínimos conflictos
def minimos_conflictos(grafo, valores, max_intentos=1000):
    nodos = list(grafo.keys())
    asignacion = asignacion_aleatoria(nodos, valores)

    for _ in range(max_intentos):
        if contar_conflictos(asignacion, grafo) == 0:
            return asignacion

        # Seleccionar una variable en conflicto
        conflicto = [n for n in nodos if any(asignacion[n] == asignacion.get(v) for v in grafo[n])]
        if not conflicto:
            break

        nodo = random.choice(conflicto)
        mejor = mejor_valor_para(nodo, asignacion, grafo, valores)
        asignacion[nodo] = mejor

    return None

# Ejecutar algoritmo
solucion = minimos_conflictos(grafo, valores)

# Mostrar resultado
print("Búsqueda Local - Mínimos Conflictos (Min-Conflicts)")
if solucion:
    print("Solución encontrada:")
    for nodo, color in solucion.items():
        print(f"  {nodo}: {color}")
else:
    print("No se encontró una solución válida.")
