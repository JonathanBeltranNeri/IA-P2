## Jonathan Beltran Neri
# Tema: Retropropagación del Error (Backpropagation)

# La retropropagación del error es el algoritmo que permite ajustar los pesos
# en una red neuronal multicapa entrenándola para minimizar el error.


import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_circles

# Generamos datos en círculos (no lineales)
X, y = make_circles(n_samples=200, noise=0.1, factor=0.5, random_state=42)

# Creamos un MLP que usa retropropagación automáticamente (en sklearn)
modelo = MLPClassifier(hidden_layer_sizes=(10, 5), activation='tanh', solver='adam', max_iter=5000, random_state=42)
modelo.fit(X, y)

# Predicción para graficar la frontera
x_min, x_max = X[:, 0].min() - 0.5, X[:, 0].max() + 0.5
y_min, y_max = X[:, 1].min() - 0.5, X[:, 1].max() + 0.5
xx, yy = np.meshgrid(np.linspace(x_min, x_max, 300),
                     np.linspace(y_min, y_max, 300))
Z = modelo.predict(np.c_[xx.ravel(), yy.ravel()])
Z = Z.reshape(xx.shape)

# Gráfica
plt.contourf(xx, yy, Z, alpha=0.8, cmap=plt.cm.PuOr)
plt.scatter(X[:, 0], X[:, 1], c=y, edgecolor='k', cmap=plt.cm.PuOr)
plt.title('Retropropagación del Error - MLP sobre Círculos')
plt.xlabel('x1')
plt.ylabel('x2')
plt.show()
