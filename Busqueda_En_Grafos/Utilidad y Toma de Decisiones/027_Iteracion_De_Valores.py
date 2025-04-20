## Jonathan Beltran Neri
# Algoritmo: Iteración de Valores (Value Iteration)

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
# Este algoritmo recorre un grafo y calcula el valor óptimo de cada estado
# considerando las recompensas de transición y un factor de descuento.

# Grafo con transiciones y recompensas
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
gamma = 0.9         # Factor de descuento
umbral = 0.001      # Criterio de convergencia

# Inicializar todos los valores en 0
valores = {estado: 0 for estado in grafo}

# Algoritmo de iteración de valores
def iteracion_de_valores():
    while True:
        delta = 0
        nuevos_valores = valores.copy()

        for estado in grafo:
            if not grafo[estado]:
                continue  # Estado terminal

            # Evaluar el valor máximo esperado entre las acciones posibles
            valor_max = max(
                recompensa + gamma * valores[siguiente]
                for siguiente, recompensa in grafo[estado]
            )

            nuevos_valores[estado] = valor_max
            delta = max(delta, abs(valores[estado] - valor_max))

        # Actualizar los valores
        valores.update(nuevos_valores)

        if delta < umbral:
            break

# Ejecutar la iteración
print("Iteración de Valores - Cálculo de valor óptimo por estado\n")
iteracion_de_valores()

# Mostrar resultados
for estado in sorted(valores.keys()):
    print(f"Estado '{estado}': Valor óptimo = {valores[estado]:.2f}")
