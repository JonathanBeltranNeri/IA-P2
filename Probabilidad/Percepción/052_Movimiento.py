## Jonathan Beltran Neri
# Tema: Movimiento

# El análisis de movimiento permite detectar cambios en la posición de objetos
# entre diferentes momentos o cuadros de una secuencia de imágenes.

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import cv2
import numpy as np

# Creamos dos imágenes simuladas: un círculo que se mueve

# Imagen 1: círculo en la posición inicial
imagen1 = np.zeros((100, 100), dtype=np.uint8)
cv2.circle(imagen1, (30, 50), 10, 255, -1)

# Imagen 2: círculo desplazado
imagen2 = np.zeros((100, 100), dtype=np.uint8)
cv2.circle(imagen2, (50, 50), 10, 255, -1)

# Calculamos la diferencia absoluta entre las imágenes
diferencia = cv2.absdiff(imagen1, imagen2)

# Mostrar resultados
fig, axs = plt.subplots(1, 3, figsize=(12, 4))

axs[0].imshow(imagen1, cmap='gray')
axs[0].set_title('Imagen 1')
axs[0].axis('off')

axs[1].imshow(imagen2, cmap='gray')
axs[1].set_title('Imagen 2')
axs[1].axis('off')

axs[2].imshow(diferencia, cmap='gray')
axs[2].set_title('Diferencia (Movimiento Detectado)')
axs[2].axis('off')

plt.tight_layout()
plt.show()
