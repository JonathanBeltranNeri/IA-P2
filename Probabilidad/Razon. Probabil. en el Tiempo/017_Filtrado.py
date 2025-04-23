## Jonathan Beltran Neri
# Tema: Filtrado (Filtering)

# El filtrado estima el estado actual de un sistema basado en toda la evidencia observada hasta ese momento.
# En este ejemplo, simulamos cómo se puede usar filtrado para predecir el medio de transporte actual de una persona
# con base en observaciones ruidosas (por ejemplo, sensores de ubicación que pueden fallar).

import random

# Estados posibles del sistema
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

# Evidencias observadas en los últimos 5 días
evidencias = ['Tren', 'Camión', 'Camión', 'Caminando', 'Tren']

# Distribución inicial: creencia uniforme
creencia = {'Tren': 1/3, 'Camión': 1/3, 'Caminando': 1/3}

# Función de normalización
def normalizar(distribucion):
    total = sum(distribucion.values())
    return {k: v / total for k, v in distribucion.items()}

# Aplicar filtrado paso a paso
for t, obs in enumerate(evidencias):
    # Predicción: usar matriz de transición
    prediccion = {}
    for estado_actual in estados:
        prediccion[estado_actual] = sum(
            transicion[estado_anterior][estado_actual] * creencia[estado_anterior]
            for estado_anterior in estados
        )

    # Actualización: usar matriz de observación
    creencia = {
        estado: observacion[estado][obs] * prediccion[estado]
        for estado in estados
    }

    # Normalizar
    creencia = normalizar(creencia)

    print(f"Día {t+1} - Observado: {obs}")
    for estado in estados:
        print(f"  P({estado}) = {creencia[estado]:.4f}")
    print()
