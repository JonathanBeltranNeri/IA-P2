## Jonathan Beltran Neri
# Tema: Reconocimiento de Objetos

# El reconocimiento de objetos consiste en identificar y localizar elementos
# específicos dentro de una imagen.

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import cv2
import numpy as np

# Creamos una imagen simulada: varios círculos (objetos) sobre un fondo negro
imagen = np.zeros((200, 200), dtype=np.uint8)
cv2.circle(imagen, (50, 50), 20, 255, -1)
cv2.circle(imagen, (150, 50), 30, 255, -1)
cv2.circle(imagen, (100, 150), 25, 255, -1)

# Detectamos contornos
contornos, _ = cv2.findContours(imagen, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Dibujamos los contornos detectados
imagen_contornos = cv2.cvtColor(imagen, cv2.COLOR_GRAY2BGR)
cv2.drawContours(imagen_contornos, contornos, -1, (0, 255, 0), 2)

# Mostrar imágenes
fig, axs = plt.subplots(1, 2, figsize=(10, 5))

axs[0].imshow(imagen, cmap='gray')
axs[0].set_title('Imagen Original')
axs[0].axis('off')

axs[1].imshow(imagen_contornos)
axs[1].set_title('Contornos Detectados (Reconocimiento de Objetos)')
axs[1].axis('off')

plt.tight_layout()
plt.show()
