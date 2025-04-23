## Jonathan Beltran Neri
# Tema: Filtro de Kalman

# El Filtro de Kalman es un algoritmo de estimación usado para rastrear el estado de un sistema dinámico
# que evoluciona en el tiempo y está sujeto a incertidumbre (ruido). 
# Funciona mejor en espacios continuos y lineales con ruido gaussiano.

# En este ejemplo, simulamos el seguimiento de una posición 1D (ej. ubicación de una persona caminando)
# con mediciones ruidosas.

import random

# Parámetros del modelo
posicion_real = 0.0               # Posición real inicial
velocidad_real = 1.0             # Movimiento constante por paso
ruido_movimiento = 0.5           # Ruido en el modelo (incertidumbre al moverse)
ruido_medicion = 1.0             # Ruido en el sensor de medición

# Estimación inicial
posicion_estimada = 0.0
incertidumbre = 1.0

# Listas para mostrar evolución
reales = []
estimadas = []
mediciones = []

print("Filtro de Kalman - Seguimiento de posición 1D con ruido\n")

# Simulación de 20 pasos
for t in range(20):
    # Movimiento real con ruido
    posicion_real += velocidad_real + random.gauss(0, ruido_movimiento)
    reales.append(posicion_real)

    # Medición ruidosa
    medicion = posicion_real + random.gauss(0, ruido_medicion)
    mediciones.append(medicion)

    # PREDICCIÓN
    posicion_estimada += velocidad_real
    incertidumbre += ruido_movimiento ** 2

    # ACTUALIZACIÓN
    K = incertidumbre / (incertidumbre + ruido_medicion ** 2)  # Ganancia de Kalman
    posicion_estimada = posicion_estimada + K * (medicion - posicion_estimada)
    incertidumbre = (1 - K) * incertidumbre
    estimadas.append(posicion_estimada)

    print(f"Paso {t+1:02d}: Real = {posicion_real:.2f}, Medido = {medicion:.2f}, Estimado = {posicion_estimada:.2f}")

