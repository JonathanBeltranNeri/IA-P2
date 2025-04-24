## Jonathan Beltran Neri
# Tema: Agrupamiento No Supervisado (Unsupervised Clustering)

# Este ejemplo muestra cómo agrupar observaciones acústicas (ruido, motor, silencio)
# sin saber de antemano a qué medio de transporte pertenecen.

# Simulamos características numéricas (por ejemplo, duración del sonido y volumen)
# y agrupamos usando k-medias (k-means) sin conocer las etiquetas reales.

from sklearn.cluster import KMeans
import numpy as np

# Simulación de datos: [duración, volumen]
# Generamos puntos para cada tipo de transporte (desconocido para el algoritmo)

# Tren: sonidos largos y fuertes
tren = np.random.normal(loc=[8, 9], scale=0.5, size=(10, 2))

# Camión: duración media y volumen medio
camion = np.random.normal(loc=[5, 6], scale=0.5, size=(10, 2))

# Caminando: sonidos cortos y suaves
caminando = np.random.normal(loc=[2, 2], scale=0.5, size=(10, 2))

# Combinamos todos los datos
X = np.vstack([tren, camion, caminando])

# Algoritmo de agrupamiento k-medias
kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(X)

# Resultados
etiquetas = kmeans.labels_
centroides = kmeans.cluster_centers_

# Mostrar resultados
print("Agrupamiento No Supervisado con k-medias:")
for i, centroide in enumerate(centroides):
    print(f"  Grupo {i+1}: Centroide en duración={centroide[0]:.2f}, volumen={centroide[1]:.2f}")

print("\nAsignación de observaciones a grupos:")
for i, punto in enumerate(X):
    grupo = etiquetas[i] + 1
    print(f"  Observación {i+1:02d}: duración={punto[0]:.2f}, volumen={punto[1]:.2f} → Grupo {grupo}")
