## Jonathan Beltran Neri
# Tema: Probabilidad Condicionada y Normalización

# La probabilidad condicionada representa la probabilidad de que ocurra un evento A dado que ocurrió B: P(A | B)
# La normalización se usa para convertir valores proporcionales en probabilidades válidas que sumen 1.

# Supongamos que un agente recibe una observación parcial de su entorno.
# A partir de una distribución a priori, actualiza sus creencias usando la información observada.

# Estructura del grafo:
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

# Estados posibles
estados = ['M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']

# Distribución a priori
prob_priori = {
    'M': 0.25,
    'N': 0.2,
    'O': 0.15,
    'P': 0.1,
    'Q': 0.1,
    'R': 0.08,
    'S': 0.07,
    'T': 0.05
}

# Supongamos que el agente detecta un ruido cerca del nodo 'P' o 'Q'.
# Por eso actualiza su creencia dando más peso a esos nodos.
# Esta nueva información afecta las probabilidades proporcionales.

# Probabilidad condicional proporcional a la evidencia (sin normalizar)
no_normalizado = {
    estado: prob_priori[estado] * (1.5 if estado in ['P', 'Q'] else 1.0)
    for estado in estados
}

# Normalización: convertir a una distribución de probabilidad válida
suma = sum(no_normalizado.values())
prob_condicionada = {estado: no_normalizado[estado] / suma for estado in estados}

# Mostrar resultado
print("Probabilidad Condicionada (con normalización) dada una observación parcial:\n")
for estado in estados:
    print(f"  Estado '{estado}': {prob_condicionada[estado]:.4f}")

print(f"\nSuma total de la distribución condicionada: {sum(prob_condicionada.values()):.4f}")
