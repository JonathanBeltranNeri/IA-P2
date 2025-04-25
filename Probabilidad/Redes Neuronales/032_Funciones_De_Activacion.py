## Jonathan Beltran Neri
# Tema: Funciones de Activación

# Las funciones de activación deciden si una neurona se "activa" o no.
# También introducen no linealidad al modelo, permitiendo que redes neuronales aprendan patrones complejos.

import math

# Funciones de activación comunes

# 1. Función escalón
def escalon(x):
    return 1 if x >= 0 else 0

# 2. Función sigmoide
def sigmoide(x):
    return 1 / (1 + math.exp(-x))

# 3. Función tangente hiperbólica (tanh)
def tanh(x):
    return math.tanh(x)

# 4. Función ReLU
def relu(x):
    return max(0, x)

# Prueba de las funciones
valores = [-2, -1, 0, 1, 2]

print("Evaluación de funciones de activación:")
for v in valores:
    print(f"x = {v}")
    print(f"  Escalón:  {escalon(v)}")
    print(f"  Sigmoide: {sigmoide(v):.4f}")
    print(f"  Tanh:     {tanh(v):.4f}")
    print(f"  ReLU:     {relu(v):.4f}")
    print()
