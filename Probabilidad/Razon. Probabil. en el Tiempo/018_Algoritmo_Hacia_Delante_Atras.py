## Jonathan Beltran Neri
# Tema: Algoritmo Hacia Delante y Atrás (Forward-Backward)

# Este algoritmo se utiliza en Modelos Ocultos de Markov (HMM)
# para calcular la probabilidad de cada estado en cada instante de tiempo,
# dado todo el conjunto de observaciones.

import random

# Estados posibles
estados = ['Tren', 'Camión', 'Caminando']

# Matriz de transición: P(estado_t | estado_t-1)
transicion = {
    'Tren':      {'Tren': 0.6, 'Camión': 0.3, 'Caminando': 0.1},
    'Camión':    {'Tren': 0.4, 'Camión': 0.4, 'Caminando': 0.2},
    'Caminando': {'Tren': 0.3, 'Camión': 0.2, 'Caminando': 0.5}
}

# Matriz de observación: P(observación | estado_real)
observacion = {
    'Tren':      {'Tren': 0.8, 'Camión': 0.1, 'Caminando': 0.1},
    'Camión':    {'Tren': 0.1, 'Camión': 0.8, 'Caminando': 0.1},
    'Caminando': {'Tren': 0.1, 'Camión': 0.2, 'Caminando': 0.7}
}

# Observaciones registradas
evidencias = ['Tren', 'Camión', 'Caminando', 'Camión', 'Tren']

# Distribución inicial (uniforme)
inicial = {'Tren': 1/3, 'Camión': 1/3, 'Caminando': 1/3}

# Normalizar distribución
def normalizar(dist):
    total = sum(dist.values())
    return {k: v / total for k, v in dist.items()}

# Paso hacia adelante (forward)
adelante = []
alpha = inicial
for obs in evidencias:
    nuevo = {}
    for estado_actual in estados:
        suma = sum(alpha[prev] * transicion[prev][estado_actual] for prev in estados)
        nuevo[estado_actual] = observacion[estado_actual][obs] * suma
    alpha = normalizar(nuevo)
    adelante.append(alpha)

# Paso hacia atrás (backward)
atras = [{} for _ in range(len(evidencias))]
atras[-1] = {estado: 1.0 for estado in estados}  # Último paso = 1

for t in reversed(range(len(evidencias)-1)):
    for estado in estados:
        suma = sum(
            transicion[estado][siguiente] *
            observacion[siguiente][evidencias[t+1]] *
            atras[t+1][siguiente]
            for siguiente in estados
        )
        atras[t][estado] = suma
    atras[t] = normalizar(atras[t])

# Combinación: P(estado | evidencias)
print("Algoritmo Hacia Delante y Atrás - Estimación completa de estados ocultos:")
for t in range(len(evidencias)):
    estimacion = {
        estado: adelante[t][estado] * atras[t][estado]
        for estado in estados
    }
    estimacion = normalizar(estimacion)
    print(f"Día {t+1} - Observación: {evidencias[t]}")
    for estado in estados:
        print(f"  P({estado}) = {estimacion[estado]:.4f}")
    print()
