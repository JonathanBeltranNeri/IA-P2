## Jonathan Beltran Neri
# Tema: Modelos Ocultos de Markov (HMM - Hidden Markov Models)

# Un Modelo Oculto de Markov es una extensión de una cadena de Markov,
# donde los estados reales no se observan directamente, pero generan observaciones con cierta probabilidad.

# Estados ocultos: medios reales de transporte
# Observaciones: lo que "creemos" haber visto (ruido del motor, velocidad, etc.)

import random

# Estados ocultos (no se observan directamente)
estados = ['Tren', 'Camión', 'Caminando']

# Matriz de transición entre estados ocultos
transicion = {
    'Tren':      {'Tren': 0.6, 'Camión': 0.3, 'Caminando': 0.1},
    'Camión':    {'Tren': 0.4, 'Camión': 0.4, 'Caminando': 0.2},
    'Caminando': {'Tren': 0.3, 'Camión': 0.2, 'Caminando': 0.5}
}

# Matriz de observación: P(observación | estado real)
observacion = {
    'Tren':      {'Ruido': 0.7, 'Motor': 0.2, 'Silencio': 0.1},
    'Camión':    {'Ruido': 0.3, 'Motor': 0.6, 'Silencio': 0.1},
    'Caminando': {'Ruido': 0.1, 'Motor': 0.2, 'Silencio': 0.7}
}

# Simulación de secuencia de estados ocultos y observaciones
estado_actual = 'Camión'
secuencia_estados = [estado_actual]
secuencia_observaciones = []

# Generamos 10 pasos del HMM
for _ in range(10):
    # Generar observación basada en el estado actual
    r = random.random()
    acumulado = 0
    for obs, prob in observacion[estado_actual].items():
        acumulado += prob
        if r < acumulado:
            secuencia_observaciones.append(obs)
            break

    # Transición al siguiente estado oculto
    r = random.random()
    acumulado = 0
    for siguiente, prob in transicion[estado_actual].items():
        acumulado += prob
        if r < acumulado:
            estado_actual = siguiente
            secuencia_estados.append(estado_actual)
            break

# Mostrar resultados
print("Modelo Oculto de Markov - Simulación de estados y observaciones")
print("Estados ocultos:")
print(" → ".join(secuencia_estados[:-1]))  # El último se genera después
print("\nObservaciones:")
print(" → ".join(secuencia_observaciones))
