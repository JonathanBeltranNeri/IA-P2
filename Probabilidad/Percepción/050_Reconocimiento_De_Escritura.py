## Jonathan Beltran Neri
# Tema: Reconocimiento de Escritura

# El reconocimiento de escritura trata de identificar letras o números escritos a mano
# a partir de imágenes.

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

# Cargamos el dataset de dígitos escritos a mano de sklearn
digitos = datasets.load_digits()

# Visualizamos algunas imágenes de ejemplo
fig, axs = plt.subplots(2, 5, figsize=(10, 5))
for i in range(10):
    ax = axs[i // 5, i % 5]
    ax.imshow(digitos.images[i], cmap='gray')
    ax.axis('off')
    ax.set_title(f'Dígito: {digitos.target[i]}')
plt.tight_layout()
plt.show()

# Preparamos los datos para entrenamiento
X = digitos.data
y = digitos.target

# Dividimos en entrenamiento y prueba
X_entrenamiento, X_prueba, y_entrenamiento, y_prueba = train_test_split(X, y, test_size=0.2, random_state=42)

# Creamos un clasificador k-NN
modelo_knn = KNeighborsClassifier(n_neighbors=3)
modelo_knn.fit(X_entrenamiento, y_entrenamiento)

# Evaluamos el modelo
precision = modelo_knn.score(X_prueba, y_prueba)
print(f"Precisión del reconocimiento de escritura (k-NN): {precision:.4f}")
