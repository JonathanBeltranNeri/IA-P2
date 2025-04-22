## Jonathan Beltran Neri
# Tema: Regla de Bayes aplicada al grafo

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
# Supongamos que un sensor da una señal fuerte cuando el agente está en 'T'.
# Queremos saber: ¿Cuál es la probabilidad de que el agente esté en 'T' si el sensor se activa?

# Distribución a priori (P(estado))
P_priori = {
    'T': 0.05,
    'P': 0.15,
    'Q': 0.15,
    'R': 0.10,
    'S': 0.15,
    'N': 0.08,
    'O': 0.07,
    'M': 0.05
}

# Probabilidad de que el sensor se active si el agente está en cada estado (P(sensor | estado))
P_sensor_dado_estado = {
    'T': 0.9,
    'P': 0.6,
    'Q': 0.6,
    'R': 0.3,
    'S': 0.4,
    'N': 0.2,
    'O': 0.2,
    'M': 0.1
}

# Calcular P(sensor) usando la regla de probabilidad total
P_sensor = sum(
    P_priori[estado] * P_sensor_dado_estado[estado]
    for estado in P_priori
)

# Calcular P(estado | sensor) usando la Regla de Bayes para todos los estados
P_posterior = {}
for estado in P_priori:
    numerador = P_sensor_dado_estado[estado] * P_priori[estado]
    P_posterior[estado] = numerador / P_sensor

# Mostrar resultados
print("Regla de Bayes aplicada al grafo:")
print("Probabilidad de estar en cada estado dado que el sensor se activó:\n")
for estado in sorted(P_posterior, key=P_posterior.get, reverse=True):
    print(f"  Estado '{estado}': P(estado | sensor) = {P_posterior[estado]:.4f}")

print(f"\nP(sensor) total: {P_sensor:.4f}")
