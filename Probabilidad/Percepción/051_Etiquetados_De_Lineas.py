## Jonathan Beltran Neri
# Tema: Etiquetados de Líneas

# El etiquetado de líneas o regiones consiste en identificar y asignar una etiqueta única
# a cada objeto o segmento conectado dentro de una imagen.

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt
import cv2
import numpy as np

# Creamos una imagen con varias regiones (objetos blancos sobre fondo negro)
imagen = np.zeros((200, 200), dtype=np.uint8)
cv2.rectangle(imagen, (20, 20), (80, 80), 255, -1)
cv2.rectangle(imagen, (120, 20), (180, 80), 255, -1)
cv2.circle(imagen, (100, 150), 30, 255, -1)

# Aplicamos etiquetado de componentes conectados
numero_etiquetas, etiquetas_imagen = cv2.connectedComponents(imagen)

# Visualizamos la imagen etiquetada
# Normalizamos los valores para mostrarlos bien en un mapa de colores
etiquetas_normalizadas = etiquetas_imagen * int(255 / (numero_etiquetas - 1))
etiquetas_normalizadas = np.uint8(etiquetas_normalizadas)

# Mostrar resultados
plt.figure(figsize=(8, 5))

plt.subplot(1, 2, 1)
plt.imshow(imagen, cmap='gray')
plt.title('Imagen Original')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(etiquetas_normalizadas, cmap='jet')
plt.title('Etiquetado de Líneas / Regiones')
plt.axis('off')

plt.tight_layout()
plt.show()

print(f"Número de objetos detectados: {numero_etiquetas - 1}")
