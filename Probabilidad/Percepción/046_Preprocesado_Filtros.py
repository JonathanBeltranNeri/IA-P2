## Jonathan Beltran Neri
# Tema: Preprocesado - Filtros

# El preprocesado en visión por computadora implica limpiar o mejorar
# las imágenes para facilitar su análisis posterior.

# En este ejemplo aplicaremos filtros de suavizado y detección de bordes.

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import cv2
import numpy as np

# Generamos una imagen simulada: fondo gris con un cuadrado blanco
imagen = np.full((100, 100), 120, dtype=np.uint8)
cv2.rectangle(imagen, (30, 30), (70, 70), 255, -1)

# Aplicamos filtro de suavizado (blur)
imagen_suavizada = cv2.GaussianBlur(imagen, (5, 5), 0)

# Aplicamos filtro de detección de bordes (Sobel)
bordes_x = cv2.Sobel(imagen, cv2.CV_64F, 1, 0, ksize=3)
bordes_y = cv2.Sobel(imagen, cv2.CV_64F, 0, 1, ksize=3)
bordes = np.sqrt(bordes_x**2 + bordes_y**2)
bordes = np.uint8(bordes)

# Mostrar imágenes
fig, axs = plt.subplots(1, 3, figsize=(12, 4))

axs[0].imshow(imagen, cmap='gray')
axs[0].set_title('Imagen Original')
axs[0].axis('off')

axs[1].imshow(imagen_suavizada, cmap='gray')
axs[1].set_title('Imagen Suavizada (Blur)')
axs[1].axis('off')

axs[2].imshow(bordes, cmap='gray')
axs[2].set_title('Bordes Detectados (Sobel)')
axs[2].axis('off')

plt.tight_layout()
plt.show()
