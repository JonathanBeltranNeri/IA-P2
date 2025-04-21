## Jonathan Beltran Neri
# Algoritmo: Q-Learning

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
# Este algoritmo aprende los valores Q(s, a) para cada estado y acción,
# actualizando sus estimaciones con base en las recompensas observadas
# y el mejor valor futuro posible.

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

# Parámetros
alpha = 0.1     # Tasa de aprendizaje
gamma = 0.9     # Factor de descuento
epsilon = 0.2   # Probabilidad de exploración
episodios = 1000

# Inicializar tabla Q
Q = {}
for estado in grafo:
    Q[estado] = {}
    for accion, _ in grafo[estado]:
        Q[estado][accion] = 0.0

# Función para elegir acción según epsilon-greedy
def elegir_accion(estado):
    if random.random() < epsilon:
        return random.choice(list(Q[estado].keys()))
    return max(Q[estado], key=Q[estado].get)

# Algoritmo Q-Learning
for _ in range(episodios):
    estado = 'M'
    while grafo[estado]:
        accion = elegir_accion(estado)
        recompensa = next(r for s, r in grafo[estado] if s == accion)
        siguiente = accion

        # Valor futuro máximo desde siguiente estado
        max_q_siguiente = max(Q[siguiente].values(), default=0)

        # Actualizar Q(s, a)
        Q[estado][accion] += alpha * (recompensa + gamma * max_q_siguiente - Q[estado][accion])
        estado = siguiente

# Mostrar resultados
print("Q-Learning - Tabla de valores Q(s, a)\n")
for estado in sorted(Q.keys()):
    for accion in Q[estado]:
        print(f"Q({estado}, {accion}) = {Q[estado][accion]:.2f}")
