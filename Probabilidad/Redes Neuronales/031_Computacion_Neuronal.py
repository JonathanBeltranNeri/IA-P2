## Jonathan Beltran Neri
# Tema: Computación Neuronal

# La computación neuronal se basa en el modelo de cómo las neuronas biológicas 
# reciben, procesan y transmiten señales. 
# En este ejemplo, simulamos una neurona artificial muy simple.

# Una neurona artificial realiza tres pasos básicos:
# - Recibe entradas (inputs)
# - Calcula una combinación lineal de las entradas (suma ponderada)
# - Aplica una función de activación para producir la salida

# Entradas de ejemplo (x1, x2) y sus pesos (w1, w2)
entradas = [0.7, 0.3]
pesos = [0.8, -0.5]
sesgo = 0.1  # También llamado bias

# Cálculo de la combinación lineal
z = sum(x * w for x, w in zip(entradas, pesos)) + sesgo

# Función de activación (por ahora, identidad)
salida = z

# Mostrar resultados
print("Computación Neuronal Básica:")
print(f"Entradas: {entradas}")
print(f"Pesos: {pesos}")
print(f"Sesgo: {sesgo}")
print(f"Salida calculada: {salida:.4f}")
