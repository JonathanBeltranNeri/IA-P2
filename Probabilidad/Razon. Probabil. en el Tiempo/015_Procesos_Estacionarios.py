## Jonathan Beltran Neri
# Tema: Procesos Estacionarios 
# Un proceso es estacionario si sus transiciones no cambian con el tiempo.
# Aquí simulamos mi proceso de cambio  de transporte día con día:
# Metro, Camión o Caminando, y con el tiempo se estabiliza la distribución de uso.

import random

# Matriz de transición: P(modo_t+1 | modo_t)
transicion = {
    'Metro':     {'Metro': 0.6, 'Camión': 0.3, 'Caminando': 0.1},
    'Camión':    {'Metro': 0.4, 'Camión': 0.4, 'Caminando': 0.2},
    'Caminando': {'Metro': 0.3, 'Camión': 0.2, 'Caminando': 0.5}
}

# Estado inicial
estado = 'Metro'
conteo = {'Metro': 0, 'Camión': 0, 'Caminando': 0}
pasos = 10000

# Simulación del proceso
for _ in range(pasos):
    conteo[estado] += 1
    r = random.random()
    acumulado = 0
    for siguiente, prob in transicion[estado].items():
        acumulado += prob
        if r < acumulado:
            estado = siguiente
            break

# Mostrar la distribución estacionaria aproximada
print("Distribución de transporte después de 10,000 días:")
total = sum(conteo.values())
for modo in conteo:
    print(f"  {modo}: {conteo[modo] / total:.4f}")
