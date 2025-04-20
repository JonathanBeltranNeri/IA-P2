## Jonathan Beltran Neri
# Algoritmo: Red Bayesiana Dinámica (DBN)

# Estructura del grafo utilizado (tiempo t y t+1):
#
# Tiempo t:
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
# En una Red Bayesiana Dinámica, los estados cambian con el tiempo.
# Se representan como una red bayesiana extendida con nodos en múltiples pasos temporales.

import random

# Estados posibles (basado en los nodos del grafo)
estados = ['M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']

# Transiciones probabilísticas (simplificadas para este ejemplo)
transiciones = {
    'M': {'N': 0.5, 'O': 0.5},
    'N': {'P': 0.5, 'Q': 0.5},
    'O': {'R': 1.0},
    'P': {'T': 1.0},
    'Q': {'T': 1.0},
    'R': {'S': 1.0},
    'S': {'T': 1.0},
    'T': {}  # Estado terminal
}

# Estado inicial en t=0
estado_actual = 'M'

# Simulación de la red por varios pasos de tiempo
def simular_red_bayesiana_dinamica(pasos):
    secuencia = [estado_actual]
    estado = estado_actual

    for _ in range(pasos):
        opciones = transiciones.get(estado, {})
        if not opciones:
            break
        siguiente = random.choices(list(opciones.keys()), weights=opciones.values())[0]
        secuencia.append(siguiente)
        estado = siguiente

    return secuencia

# Ejecutar la simulación
print("Red Bayesiana Dinámica - Simulación de secuencia de estados a través del tiempo\n")
secuencia_resultado = simular_red_bayesiana_dinamica(pasos=5)

# Mostrar secuencia
print("Secuencia generada:")
for i, estado in enumerate(secuencia_resultado):
    print(f"  t={i}: {estado}")
