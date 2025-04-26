## Jonathan Beltran Neri
# Tema: Detección de Aristas y Segmentación

# La detección de aristas identifica bordes y contornos en una imagen.
# La segmentación divide una imagen en regiones coherentes (por ejemplo, objetos).

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import cv2
import numpy as np

# Creamos una imagen de prueba: fondo negro con un cuadrado blanco
imagen = np.zeros((100, 100), dtype=np.uint8)
cv2.rectangle(imagen, (30, 30), (70, 70), 255, -1)

# Detectamos aristas usando el algoritmo de Canny
bordes_canny = cv2.Canny(imagen, threshold1=50, threshold2=150)

# Segmentamos usando umbralización simple
_, segmentada = cv2.threshold(imagen, 127, 255, cv2.THRESH_BINARY)

# Mostrar imágenes
fig, axs = plt.subplots(1, 3, figsize=(12, 4))

axs[0].imshow(imagen, cmap='gray')
axs[0].set_title('Imagen Original')
axs[0].axis('off')

axs[1].imshow(bordes_canny, cmap='gray')
axs[1].set_title('Detección de Aristas (Canny)')
axs[1].axis('off')

axs[2].imshow(segmentada, cmap='gray')
axs[2].set_title('Segmentación (Umbralización)')
axs[2].axis('off')

plt.tight_layout()
plt.show()
