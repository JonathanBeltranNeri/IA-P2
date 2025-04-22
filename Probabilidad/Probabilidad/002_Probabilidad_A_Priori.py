## Jonathan Beltran Neri
# Tema: Probabilidad a Priori

# La probabilidad a priori (o probabilidad previa) representa el conocimiento inicial
# que se tiene sobre un evento antes de observar cualquier evidencia.

# En este ejemplo, un agente asigna probabilidades a cada nodo del grafo como si cada uno fuera
# un posible estado del mundo. Estas probabilidades se basan solo en el conocimiento previo.

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

# Estados posibles del agente (nodos del grafo)
estados = ['M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T']

# Supongamos que el agente cree que es más probable estar en los nodos cercanos a M
# y menos probable en los más lejanos, sin observar nada aún.

probabilidades_priori = {
    'M': 0.25,
    'N': 0.2,
    'O': 0.15,
    'P': 0.1,
    'Q': 0.1,
    'R': 0.08,
    'S': 0.07,
    'T': 0.05
}

# Validar que la suma sea 1.0
suma_total = sum(probabilidades_priori.values())

# Mostrar resultados
print("Probabilidad a Priori sobre los posibles estados:")
for estado, prob in probabilidades_priori.items():
    print(f"  Estado '{estado}': {prob:.2f}")

print(f"\nSuma total de probabilidades: {suma_total:.2f}")
