## Jonathan Beltran Neri
# Tema: Aprendizaje Profundo (Deep Learning)

# Este ejemplo usa una red neuronal simple con Keras para clasificar
# sonidos simulados de transporte: Tren, Camión y Caminando.

import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical

# Datos de entrada simulados: [duración, volumen]
X = np.array([
    [8.0, 9.1],  [8.2, 8.8],  [7.8, 9.0],     # Tren
    [5.1, 6.0],  [5.2, 6.1],  [4.9, 5.8],     # Camión
    [2.0, 2.2],  [1.9, 1.8],  [2.1, 2.0]      # Caminando
])

# Etiquetas: 0 = Tren, 1 = Camión, 2 = Caminando
y = np.array([0, 0, 0, 1, 1, 1, 2, 2, 2])
y_cat = to_categorical(y)

# Modelo secuencial
modelo = Sequential()
modelo.add(Dense(8, input_shape=(2,), activation='relu'))
modelo.add(Dense(6, activation='relu'))
modelo.add(Dense(3, activation='softmax'))  # 3 clases

modelo.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Entrenamiento
modelo.fit(X, y_cat, epochs=100, verbose=0)

# Nuevas observaciones a predecir
X_test = np.array([
    [8.1, 8.9],    # ¿Tren?
    [5.0, 6.2],    # ¿Camión?
    [2.2, 1.9]     # ¿Caminando?
])

# Predicción
predicciones = modelo.predict(X_test)
clases = ['Tren', 'Camión', 'Caminando']

print("Clasificación con Deep Learning:")
for i, salida in enumerate(predicciones):
    pred_clase = clases[np.argmax(salida)]
    print(f"  Observación {i+1}: {X_test[i]} → Clase estimada: {pred_clase}")
