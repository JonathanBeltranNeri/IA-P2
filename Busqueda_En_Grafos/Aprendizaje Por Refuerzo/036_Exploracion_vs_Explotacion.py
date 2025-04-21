## Jonathan Beltran Neri
# Algoritmo: Exploración vs. Explotación

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
# Este experimento compara dos políticas:
# 1. Agente que explora mucho (elige acciones al azar)
# 2. Agente que explota siempre (elige acciones con mejor Q)

import random

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

# Q-Table inicializada en 0
Q_explorador = {s: {a: 0 for a, _ in grafo[s]} for s in grafo}
Q_explotador = {s: {a: 0 for a, _ in grafo[s]} for s in grafo}

# Parámetros
alpha = 0.1
gamma = 0.9
episodios = 1000

# Función Q-Learning con control de epsilon
def q_learning(Q, epsilon):
    for _ in range(episodios):
        estado = 'M'
        while grafo[estado]:
            acciones = list(Q[estado].keys())
            if random.random() < epsilon:
                accion = random.choice(acciones)
            else:
                accion = max(Q[estado], key=Q[estado].get)

            recompensa = next(r for s, r in grafo[estado] if s == accion)
            siguiente = accion
            max_q_siguiente = max(Q[siguiente].values(), default=0)

            Q[estado][accion] += alpha * (recompensa + gamma * max_q_siguiente - Q[estado][accion])
            estado = siguiente

# Ejecutar con diferentes políticas
q_learning(Q_explorador, epsilon=0.9)  # Explora casi siempre
q_learning(Q_explotador, epsilon=0.0)  # Solo explota

# Comparar resultados
print("Comparación: Exploración vs. Explotación\n")
print("Q-values del agente EXPLORADOR:")
for estado in Q_explorador:
    for accion in Q_explorador[estado]:
        print(f"  Q({estado}, {accion}) = {Q_explorador[estado][accion]:.2f}")

print("\nQ-values del agente EXPLOTADOR:")
for estado in Q_explotador:
    for accion in Q_explotador[estado]:
        print(f"  Q({estado}, {accion}) = {Q_explotador[estado][accion]:.2f}")

