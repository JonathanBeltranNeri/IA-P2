## Jonathan Beltran Neri
# Tema: Mapas Autoorganizados de Kohonen (Self-Organizing Maps - SOM)

# Los Mapas Autoorganizados (SOM) son redes no supervisadas que organizan los datos
# en un espacio reducido preservando sus relaciones topológicas.

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import numpy as np
from minisom import MiniSom

# Generamos datos simulados (dos clases en el espacio)
X = np.vstack([
    np.random.normal(loc=[2, 2], scale=0.5, size=(50, 2)),  # Clase 1
    np.random.normal(loc=[7, 7], scale=0.5, size=(50, 2))   # Clase 2
])

# Creamos el SOM
som = MiniSom(x=7, y=7, input_len=2, sigma=1.0, learning_rate=0.5, random_seed=42)

# Inicializamos los pesos
som.random_weights_init(X)

# Entrenamos el SOM
som.train_random(X, num_iteration=100)

# Visualización del mapa de respuesta
plt.figure(figsize=(7, 7))
for dato in X:
    w = som.winner(dato)  # Nodo ganador
    plt.plot(w[0] + 0.5, w[1] + 0.5, 'o', markerfacecolor='None', markeredgecolor='k', markersize=12)

plt.title('Mapa Autoorganizado de Kohonen')
plt.grid(True)
plt.xlim([0, 7])
plt.ylim([0, 7])
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.show()
