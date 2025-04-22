## Jonathan Beltran Neri
# Tema: Distribución de Probabilidad

# Una distribución de probabilidad asigna una probabilidad a cada posible valor de una variable aleatoria.
# En IA, esto se usa para modelar la creencia de un agente sobre el mundo en términos probabilísticos.

# Supongamos que un agente puede estar ubicado en cualquiera de los nodos del grafo,
# y mantiene una distribución que refleja su creencia de estar en cada uno.

# Grafo utilizado:
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

# Estados del agente (nodos del grafo)
estados = ['M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']

# Distribución de probabilidad que refleja la creencia actual del agente
# Basada en una situación donde el agente tiende a estar más cerca de la meta (T)

distribucion = {
    'M': 0.05,
    'N': 0.08,
    'O': 0.07,
    'P': 0.15,
    'Q': 0.15,
    'R': 0.1,
    'S': 0.15,
    'T': 0.25
}

# Verificar que sea una distribución válida
suma = sum(distribucion.values())

# Mostrar la distribución
print("Distribución de Probabilidad del agente sobre su ubicación:\n")
for estado in estados:
    print(f"  Estado '{estado}': Probabilidad = {distribucion[estado]:.4f}")

print(f"\nSuma total de la distribución: {suma:.4f}")
