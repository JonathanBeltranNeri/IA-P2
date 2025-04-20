## Jonathan Beltran Neri
# Algoritmo: Proceso de Decisión de Markov (MDP)

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
# Este algoritmo simula un MDP donde el agente se mueve entre estados con transiciones determinísticas
# y recibe recompensas. Se calcula el valor esperado para cada estado usando la ecuación de Bellman.

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

gamma = 0.9
umbral = 0.001

# Inicialización de valores
valores = {estado: 0 for estado in grafo}

# Ecuación de Bellman aplicada en iteración de valores
def resolver_mdp():
    while True:
        delta = 0
        nuevos_valores = valores.copy()

        for estado in grafo:
            if not grafo[estado]:
                continue

            # Se elige la acción con mayor valor esperado
            mejor_valor = max(
                recompensa + gamma * valores[siguiente]
                for siguiente, recompensa in grafo[estado]
            )

            nuevos_valores[estado] = mejor_valor
            delta = max(delta, abs(valores[estado] - mejor_valor))

        valores.update(nuevos_valores)

        if delta < umbral:
            break

# Ejecutar el cálculo
print("Proceso de Decisión de Markov (MDP) - Evaluación de estados\n")
resolver_mdp()

# Mostrar resultados
for estado in sorted(valores.keys()):
    print(f"  Estado '{estado}': Valor esperado = {valores[estado]:.2f}")
