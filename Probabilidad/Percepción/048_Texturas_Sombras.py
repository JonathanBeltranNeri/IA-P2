## Jonathan Beltran Neri
# Tema: Texturas y Sombras

# El análisis de texturas y sombras ayuda a identificar la estructura
# de los objetos en una imagen más allá del color o la forma.

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import cv2
import numpy as np

# Creamos una imagen de prueba con textura: líneas horizontales
imagen = np.zeros((100, 100), dtype=np.uint8)

for i in range(0, 100, 10):
    imagen[i:i+5, :] = 150  # Bandas grises simulando textura

# Simulamos una sombra: gradiente de oscuridad
sombra = np.tile(np.linspace(255, 50, 100), (100, 1)).astype(np.uint8)

# Imagen final combinando textura y sombra
imagen_con_sombra = cv2.addWeighted(imagen, 0.7, sombra, 0.3, 0)

# Mostrar imágenes
fig, axs = plt.subplots(1, 3, figsize=(12, 4))

axs[0].imshow(imagen, cmap='gray')
axs[0].set_title('Imagen con Textura')
axs[0].axis('off')

axs[1].imshow(sombra, cmap='gray')
axs[1].set_title('Sombra Simulada')
axs[1].axis('off')

axs[2].imshow(imagen_con_sombra, cmap='gray')
axs[2].set_title('Textura + Sombra')
axs[2].axis('off')

plt.tight_layout()
plt.show()
