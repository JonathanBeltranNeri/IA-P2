## Jonathan Beltran Neri
# Tema: Explicaciones e Información Relevante

# Este código muestra cómo identificar información relevante para tomar decisiones basadas en ejemplos observados.
# Utiliza un conjunto simple de datos y extrae las características más importantes mediante análisis de correlación.

import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt

# Cargar el conjunto de datos de ejemplo
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target, name='target')

# Crear y entrenar un modelo para evaluar la importancia de las características
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X, y)

# Obtener importancia de características
importancias = modelo.feature_importances_

# Mostrar resultados
for nombre, importancia in zip(X.columns, importancias):
    print(f"Característica: {nombre:30s} Importancia: {importancia:.4f}")

# Graficar importancia de características
plt.figure(figsize=(8, 5))
plt.barh(X.columns, importancias)
plt.xlabel("Importancia")
plt.title("Importancia de características para clasificación")
plt.tight_layout()
plt.show()
