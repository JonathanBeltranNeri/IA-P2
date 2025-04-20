## Jonathan Beltran Neri
# Algoritmo: Iteración de Políticas (Policy Iteration)

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
# Este algoritmo encuentra una política óptima para un agente en un entorno tipo MDP.
# Alterna entre evaluar la política actual y mejorarla hasta que se estabiliza.

# Grafo con acciones y recompensas
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

estados = list(grafo.keys())
gamma = 0.9
umbral = 0.001

# Inicializar política aleatoria (elige la primera acción disponible)
politica = {estado: grafo[estado][0][0] if grafo[estado] else None for estado in estados}
valores = {estado: 0 for estado in estados}

# Evaluación de política
def evaluar_politica():
    while True:
        delta = 0
        nuevos_valores = valores.copy()
        for estado in estados:
            accion = politica[estado]
            if accion is None:
                continue
            for destino, recompensa in grafo[estado]:
                if destino == accion:
                    nuevos_valores[estado] = recompensa + gamma * valores[destino]
                    delta = max(delta, abs(nuevos_valores[estado] - valores[estado]))
        valores.update(nuevos_valores)
        if delta < umbral:
            break

# Mejora de política
def mejorar_politica():
    politica_estable = True
    for estado in estados:
        if not grafo[estado]:
            continue
        acciones = grafo[estado]
        mejor_accion = max(
            acciones,
            key=lambda a: a[1] + gamma * valores[a[0]]
        )[0]
        if mejor_accion != politica[estado]:
            politica[estado] = mejor_accion
            politica_estable = False
    return politica_estable

# Algoritmo de iteración de políticas
def iteracion_de_politicas():
    while True:
        evaluar_politica()
        if mejorar_politica():
            break

# Ejecutar
print("Iteración de Políticas - Evaluación y mejora de política\n")
iteracion_de_politicas()

# Mostrar resultados
print("Política óptima encontrada:")
for estado in sorted(politica.keys()):
    accion = politica[estado]
    print(f"  Estado '{estado}': Acción -> {accion if accion else 'Terminal'}")

print("\nValores óptimos de cada estado:")
for estado in sorted(valores.keys()):
    print(f"  Estado '{estado}': Valor = {valores[estado]:.2f}")
