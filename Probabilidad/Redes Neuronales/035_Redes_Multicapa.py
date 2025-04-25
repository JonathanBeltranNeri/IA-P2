## Jonathan Beltran Neri
# Tema: Redes Multicapa (MLP) - Clasificación de datos no lineales (moons)

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_moons

# Generamos un conjunto de datos en forma de "lunas" (moons)
X, y = make_moons(n_samples=200, noise=0.2, random_state=42)

# Creamos y entrenamos la red neuronal MLP
modelo = MLPClassifier(hidden_layer_sizes=(10,), activation='tanh', solver='adam', max_iter=5000, random_state=42)
modelo.fit(X, y)

# Predicción en toda una malla de puntos para graficar frontera de decisión
x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 300),
                     np.linspace(y_min, y_max, 300))
Z = modelo.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Gráfica
plt.contourf(xx, yy, Z, alpha=0.8, cmap=plt.cm.coolwarm)
plt.scatter(X[:, 0], X[:, 1], c=y, edgecolor='k', cmap=plt.cm.coolwarm)
plt.title('Red Neuronal Multicapa (MLP) - Datos No Lineales (Moons)')
plt.xlabel('x1')
plt.ylabel('x2')
plt.show()
