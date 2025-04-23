## Jonathan Beltran Neri
# Tema: Hipótesis de Markov y Procesos de Markov

# La hipótesis de Markov establece que el estado futuro de un sistema
# depende únicamente del estado actual, no de los anteriores.
# Si esto se cumple, el sistema es un Proceso de Markov.

# En este ejemplo usamos la simulación de medios de transporte
# para ilustrar cómo el siguiente estado se determina solo por el actual.

import random

# Matriz de transición fija
transicion = {
    'Tren':      {'Tren': 0.6, 'Camión': 0.3, 'Caminando': 0.1},
    'Camión':    {'Tren': 0.4, 'Camión': 0.4, 'Caminando': 0.2},
    'Caminando': {'Tren': 0.3, 'Camión': 0.2, 'Caminando': 0.5}
}

# Secuencia simulada
estado_actual = 'Camión'
secuencia = [estado_actual]

# Generar 20 pasos simulando un proceso de Markov
for _ in range(20):
    r = random.random()
    acumulado = 0
    for siguiente, prob in transicion[estado_actual].items():
        acumulado += prob
        if r < acumulado:
            estado_actual = siguiente
            secuencia.append(estado_actual)
            break

# Mostrar la secuencia
print("Hipótesis de Markov - Secuencia generada (solo depende del estado anterior):")
print(" → ".join(secuencia))
