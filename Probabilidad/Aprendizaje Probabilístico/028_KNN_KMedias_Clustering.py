## Jonathan Beltran Neri
# Tema: k-NN, k-Medias y Clustering

# Este ejemplo compara dos métodos comunes:
# - k-NN (clasificación supervisada)
# - k-Medias (agrupamiento no supervisado)

from sklearn.neighbors import KNeighborsClassifier
from sklearn.cluster import KMeans
import numpy as np

# Simulamos observaciones acústicas (duración, volumen)
# Y asignamos etiquetas para entrenamiento k-NN

X_train = np.array([
    [8.0, 9.1],  [8.2, 8.8],  [7.8, 9.0],     # Tren
    [5.1, 6.0],  [5.2, 6.1],  [4.9, 5.8],     # Camión
    [2.0, 2.2],  [1.9, 1.8],  [2.1, 2.0]      # Caminando
])
y_train = ['Tren', 'Tren', 'Tren', 'Camión', 'Camión', 'Camión', 'Caminando', 'Caminando', 'Caminando']

# Nuevas observaciones desconocidas
X_test = np.array([
    [7.9, 9.0],    # ¿Tren?
    [5.0, 6.2],    # ¿Camión?
    [2.2, 2.1]     # ¿Caminando?
])

# Clasificación k-NN
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
predicciones_knn = knn.predict(X_test)

# Agrupamiento k-medias
kmeans = KMeans(n_clusters=3, random_state=42)
kmeans.fit(X_train)
grupos_kmeans = kmeans.predict(X_test)

# Mostrar resultados
print("Clasificación con k-NN:")
for i, pred in enumerate(predicciones_knn):
    print(f"  Observación {i+1}: {X_test[i]} → Clase estimada: {pred}")

print("\nAgrupamiento con k-Medias (grupos sin etiquetas):")
for i, grupo in enumerate(grupos_kmeans):
    print(f"  Observación {i+1}: {X_test[i]} → Grupo: {grupo}")
