## Jonathan Beltran Neri
# Tema: Redes de Hamming, Hopfield, Hebb y Boltzmann

# Este archivo da una pequeña introducción con ejemplos sencillos 
# de cómo funcionan estas redes clásicas de la computación neuronal.

import numpy as np

# ===========================================
# 1. Red de Hamming
# ===========================================

# Clasifica patrones por distancia (generalmente usando distancia de Hamming)

def red_hamming(x, patrones):
    distancias = [np.sum(x != p) for p in patrones]
    return np.argmin(distancias)

# Ejemplo:
patrones_hamming = [np.array([0, 1, 0]), np.array([1, 0, 1])]
entrada_hamming = np.array([1, 1, 1])

print("Red de Hamming:")
print(f"Patrón más cercano: {red_hamming(entrada_hamming, patrones_hamming)}\n")


# ===========================================
# 2. Red de Hopfield
# ===========================================

# Es una red recurrente que almacena patrones de manera estable (memoria asociativa)

def red_hopfield(patrones, entrada):
    n = patrones[0].size
    W = np.zeros((n, n))
    for p in patrones:
        W += np.outer(p, p)
    np.fill_diagonal(W, 0)

    estado = entrada.copy()
    for _ in range(5):  # Actualización síncrona en 5 pasos
        estado = np.sign(W @ estado)
    return estado

# Ejemplo:
patrones_hopfield = [np.array([1, -1, 1]), np.array([-1, 1, -1])]
entrada_hopfield = np.array([1, 1, -1])

print("Red de Hopfield:")
print(f"Estado estabilizado: {red_hopfield(patrones_hopfield, entrada_hopfield)}\n")


# ===========================================
# 3. Regla de Hebb
# ===========================================

# "Las neuronas que se activan juntas, se conectan más fuerte."
# Entrenamiento muy simple: w = suma(x * y)

def regla_hebb(X, Y):
    W = np.zeros((X.shape[1],))
    for x, y in zip(X, Y):
        W += x * y
    return W

# Ejemplo:
X_hebb = np.array([
    [1, 0],
    [0, 1],
    [1, 1]
])
Y_hebb = np.array([1, 1, -1])

print("Regla de Hebb:")
print(f"Pesos aprendidos: {regla_hebb(X_hebb, Y_hebb)}\n")


# ===========================================
# 4. Red de Boltzmann
# ===========================================

# Simula redes neuronales estocásticas (usa temperatura y probabilidad de activación).

# Aquí mostramos solo un principio básico:
def energia_boltzmann(W, estado):
    return -0.5 * estado @ W @ estado

# Ejemplo:
W_boltzmann = np.array([
    [0, 1],
    [1, 0]
])
estado_boltzmann = np.array([1, -1])

print("Red de Boltzmann:")
print(f"Energía del estado: {energia_boltzmann(W_boltzmann, estado_boltzmann):.2f}")
