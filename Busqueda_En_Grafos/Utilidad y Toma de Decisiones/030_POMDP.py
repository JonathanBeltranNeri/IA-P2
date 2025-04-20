## Jonathan Beltran Neri
# Algoritmo: MDP Parcialmente Observable (POMDP)

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
# En un POMDP, el agente no conoce con certeza en qué estado se encuentra.
# Tiene creencias (probabilidades) sobre los estados posibles y toma decisiones
# que maximizan la utilidad esperada según esa creencia.

import random

# Definición del grafo con recompensas
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

# Creencias iniciales del agente sobre el estado actual (distribución de probabilidad)
creencias = {
    'M': 0.5,
    'N': 0.3,
    'O': 0.2
}

gamma = 0.9

# Valor estimado de cada estado
valores = {estado: 0 for estado in grafo}

# Función para simular un paso del agente bajo incertidumbre
def accion_con_belief(belief):
    utilidad_total = 0
    for estado in belief:
        prob = belief[estado]
        if not grafo[estado]:
            continue
        mejor = max(
            recompensa + gamma * valores[siguiente]
            for siguiente, recompensa in grafo[estado]
        )
        utilidad_total += prob * mejor
    return utilidad_total

# Simulación simple de actualización de creencias
def actualizar_creencia(belief, observacion_prob):
    nueva = {}
    for estado in belief:
        nueva[estado] = belief[estado] * observacion_prob.get(estado, 0.0)
    total = sum(nueva.values())
    if total > 0:
        for estado in nueva:
            nueva[estado] /= total
    return nueva

# Ejecutar evaluación desde creencias iniciales
print("MDP Parcialmente Observable (POMDP) - Evaluación con incertidumbre\n")

# Primera evaluación suponiendo valores convergidos desde MDP
for i in range(10):  # simular convergencia básica
    nuevos = valores.copy()
    for estado in grafo:
        if not grafo[estado]:
            continue
        nuevos[estado] = max(
            recompensa + gamma * valores[siguiente]
            for siguiente, recompensa in grafo[estado]
        )
    valores = nuevos

# Evaluar utilidad esperada con las creencias actuales
utilidad = accion_con_belief(creencias)
print(f"Utilidad esperada desde creencias actuales: {utilidad:.2f}")

# Mostrar las creencias actuales
print("\nCreencias iniciales del agente:")
for estado in creencias:
    print(f"  Estado '{estado}': Probabilidad = {creencias[estado]:.2f}")
