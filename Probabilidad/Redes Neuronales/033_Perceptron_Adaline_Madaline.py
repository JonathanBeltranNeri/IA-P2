## Jonathan Beltran Neri
# Tema: Perceptrón, ADALINE y MADALINE

# Estos son modelos de redes neuronales básicos para clasificación binaria.

# ===========================================
# 1. Perceptrón
# ===========================================

# El perceptrón aprende modificando sus pesos basándose en el error de clasificación.
# Funciona bien para problemas linealmente separables.

def perceptron(x, w, bias):
    suma = sum(xi * wi for xi, wi in zip(x, w)) + bias
    return 1 if suma >= 0 else 0

# Entrenamiento simple para un perceptrón AND
entradas = [
    ([0, 0], 0),
    ([0, 1], 0),
    ([1, 0], 0),
    ([1, 1], 1)
]

pesos = [0.0, 0.0]
bias = 0.0
tasa_aprendizaje = 0.1
epocas = 10

for _ in range(epocas):
    for x, salida_esperada in entradas:
        salida = perceptron(x, pesos, bias)
        error = salida_esperada - salida
        pesos = [w + tasa_aprendizaje * error * xi for w, xi in zip(pesos, x)]
        bias += tasa_aprendizaje * error

print("Perceptrón entrenado (AND):")
print(f"Pesos: {pesos}, Bias: {bias:.2f}")

# ===========================================
# 2. ADALINE (ADAptive LInear NEuron)
# ===========================================

# ADALINE utiliza una función lineal de activación y minimiza el error cuadrático.

def adaline(x, w, bias):
    return sum(xi * wi for xi, wi in zip(x, w)) + bias

pesos = [0.0, 0.0]
bias = 0.0
tasa_aprendizaje = 0.1
epocas = 10

for _ in range(epocas):
    for x, salida_esperada in entradas:
        salida = adaline(x, pesos, bias)
        error = salida_esperada - salida
        pesos = [w + tasa_aprendizaje * error * xi for w, xi in zip(pesos, x)]
        bias += tasa_aprendizaje * error

print("\nADALINE entrenado (AND):")
print(f"Pesos: {pesos}, Bias: {bias:.2f}")

# ===========================================
# 3. MADALINE (Multiple ADAptive LInear NEuron)
# ===========================================

# MADALINE es una red de múltiples ADALINEs en paralelo.
# Aquí solo mostramos la idea, no el entrenamiento completo.

print("\nMADALINE sería una red de varias neuronas ADALINE conectadas en paralelo.")
print("No implementado en este ejemplo por simplicidad.")
