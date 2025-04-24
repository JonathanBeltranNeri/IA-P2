## Jonathan Beltran Neri
# Tema: Máquinas de Vectores de Soporte (SVM) con Núcleo (Kernel)

# Usamos SVM con núcleo RBF (Radial Basis Function) para clasificar observaciones
# basadas en características de sonido como duración y volumen.

from sklearn.svm import SVC
import numpy as np

# Datos simulados de entrenamiento (duración, volumen)
X_train = np.array([
    [8.0, 9.1],  [8.2, 8.8],  [7.8, 9.0],     # Tren
    [5.1, 6.0],  [5.2, 6.1],  [4.9, 5.8],     # Camión
    [2.0, 2.2],  [1.9, 1.8],  [2.1, 2.0]      # Caminando
])
y_train = ['Tren', 'Tren', 'Tren', 'Camión', 'Camión', 'Camión', 'Caminando', 'Caminando', 'Caminando']

# Nuevas observaciones
X_test = np.array([
    [8.1, 8.9],   # ¿Tren?
    [5.0, 6.2],   # ¿Camión?
    [2.2, 1.9]    # ¿Caminando?
])

# Entrenamiento del modelo SVM con núcleo RBF
modelo_svm = SVC(kernel='rbf', C=1.0, gamma='scale')
modelo_svm.fit(X_train, y_train)

# Predicción
predicciones = modelo_svm.predict(X_test)

# Resultados
print("Clasificación con SVM (núcleo RBF):")
for i, pred in enumerate(predicciones):
    print(f"  Observación {i+1}: {X_test[i]} → Clase estimada: {pred}")
