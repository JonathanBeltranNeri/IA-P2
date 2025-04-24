## Jonathan Beltran Neri
# Tema: Red Bayesiana Dinámica (DBN - Dynamic Bayesian Network)

# Una Red Bayesiana Dinámica extiende una red bayesiana tradicional a través del tiempo.
# Modela cómo las variables cambian de un paso a otro, manteniendo dependencias entre el pasado y el presente.

# En este ejemplo, usamos los estados: Tren, Camión, Caminando
# y modelamos cómo cambia el estado de transporte de un día al siguiente.

import random

# Estados posibles
estados = ['Tren', 'Camión', 'Caminando']

# Probabilidad de transición de estado_t a estado_t+1
transicion = {
    'Tren':      {'Tren': 0.6, 'Camión': 0.3, 'Caminando': 0.1},
    'Camión':    {'Tren': 0.4, 'Camión': 0.4, 'Caminando': 0.2},
    'Caminando': {'Tren': 0.3, 'Camión': 0.2, 'Caminando': 0.5}
}

# Probabilidad de observación: P(ruido | estado)
observacion = {
    'Tren':      {'Ruido': 0.7, 'Motor': 0.2, 'Silencio': 0.1},
    'Camión':    {'Ruido': 0.3, 'Motor': 0.6, 'Silencio': 0.1},
    'Caminando': {'Ruido': 0.1, 'Motor': 0.2, 'Silencio': 0.7}
}

# Iniciamos con una creencia inicial uniforme
creencia = {'Tren': 1/3, 'Camión': 1/3, 'Caminando': 1/3}

# Observaciones recibidas en el tiempo
evidencias = ['Ruido', 'Motor', 'Silencio', 'Ruido', 'Motor']

# Normalizar función
def normalizar(dist):
    total = sum(dist.values())
    return {k: v / total for k, v in dist.items()}

# Proceso dinámico
for t, evidencia in enumerate(evidencias):
    # Predicción del siguiente estado
    prediccion = {}
    for estado_actual in estados:
        prediccion[estado_actual] = sum(
            creencia[estado_anterior] * transicion[estado_anterior][estado_actual]
            for estado_anterior in estados
        )

    # Incorporar evidencia
    creencia = {
        estado: observacion[estado][evidencia] * prediccion[estado]
        for estado in estados
    }

    # Normalizar
    creencia = normalizar(creencia)

    print(f"Día {t+1} - Observación: {evidencia}")
    for estado in estados:
        print(f"  P({estado}) = {creencia[estado]:.4f}")
    print()
