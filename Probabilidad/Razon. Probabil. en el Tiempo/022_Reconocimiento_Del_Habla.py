## Jonathan Beltran Neri
# Tema: Reconocimiento del Habla con HMM

# Simulamos reconocimiento de comandos de voz:
# Estados reales (ocultos): comandos esperados
# Observaciones: lo que el sistema realmente detecta (puede tener errores)

import random

# Comandos de voz esperados (estados ocultos)
comandos = ['enciende', 'apaga', 'sube', 'baja']

# Transición de comandos (puede repetirse o cambiar de comando)
transicion = {
    'enciende': {'enciende': 0.6, 'apaga': 0.2, 'sube': 0.1, 'baja': 0.1},
    'apaga':    {'enciende': 0.2, 'apaga': 0.6, 'sube': 0.1, 'baja': 0.1},
    'sube':     {'sube': 0.6, 'baja': 0.2, 'enciende': 0.1, 'apaga': 0.1},
    'baja':     {'baja': 0.6, 'sube': 0.2, 'enciende': 0.1, 'apaga': 0.1}
}

# Observaciones ruidosas (palabras mal reconocidas)
observacion = {
    'enciende': {'enciende': 0.8, 'enciendé': 0.1, 'enciendee': 0.1},
    'apaga':    {'apaga': 0.8, 'apagga': 0.1, 'apaka': 0.1},
    'sube':     {'sube': 0.8, 'sobe': 0.1, 'subé': 0.1},
    'baja':     {'baja': 0.8, 'basa': 0.1, 'bajaa': 0.1}
}

# Secuencia simulada de estados reales y observaciones
estado_actual = 'enciende'
estados_reales = [estado_actual]
observaciones = []

# Simulamos 10 pasos del reconocimiento
for _ in range(10):
    # Generar observación con ruido
    r = random.random()
    acumulado = 0
    for obs, prob in observacion[estado_actual].items():
        acumulado += prob
        if r < acumulado:
            observaciones.append(obs)
            break

    # Transición al siguiente comando
    r = random.random()
    acumulado = 0
    for siguiente, prob in transicion[estado_actual].items():
        acumulado += prob
        if r < acumulado:
            estado_actual = siguiente
            estados_reales.append(estado_actual)
            break

# Mostrar resultados
print("Reconocimiento del Habla - Simulación de comandos y observaciones\n")
print("Comandos reales:     " + " → ".join(estados_reales[:-1]))
print("Observaciones ruidosas: " + " → ".join(observaciones))
