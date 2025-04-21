## Jonathan Beltran Neri
# Algoritmo: Aprendizaje por Refuerzo Activo

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
# Este algoritmo no solo evalúa una política, sino que la mejora
# activamente mediante la exploración y retroalimentación de recompensas.

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

# Inicialización de valores y política
valores = {estado: 0 for estado in grafo}
politica = {estado: random.choice(grafo[estado])[0] if grafo[estado] else None for estado in grafo}
visitas = {estado: 0 for estado in grafo}
gamma = 0.9

# Simulación con mejora de política (exploración simple)
def aprendizaje_activo(n_episodios):
    for _ in range(n_episodios):
        estado = 'M'
        trayectoria = []

        while estado and politica[estado]:
            acciones = grafo[estado]
            if random.random() < 0.2:  # 20% de exploración
                siguiente, recompensa = random.choice(acciones)
            else:  # 80% seguir política actual
                siguiente = politica[estado]
                recompensa = next(r for s, r in acciones if s == siguiente)

            trayectoria.append((estado, recompensa))
            estado = siguiente

        # Evaluar retorno
        retorno = 0
        for estado, recompensa in reversed(trayectoria):
            retorno = recompensa + gamma * retorno
            visitas[estado] += 1
            valores[estado] += (retorno - valores[estado]) / visitas[estado]

        # Mejorar política basada en nuevos valores
        for estado in politica:
            if grafo[estado]:
                politica[estado] = max(grafo[estado], key=lambda x: x[1] + gamma * valores[x[0]])[0]

# Ejecutar
print("Aprendizaje por Refuerzo Activo - Evaluación y mejora de política mediante exploración\n")
aprendizaje_activo(n_episodios=1000)

# Resultados
for estado in sorted(politica.keys()):
    print(f"Política: Estado '{estado}' → Acción → {politica[estado]}")

print("\nValores estimados:")
for estado in sorted(valores.keys()):
    print(f"  Estado '{estado}': Valor = {valores[estado]:.2f}")
