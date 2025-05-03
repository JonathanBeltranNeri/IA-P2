# Jonathan Beltran Neri
# Tema: Aprendizaje Inductivo - Árboles de Decisión: ID3

# Este código ejemplifica cómo construir un árbol de decisión simple utilizando el algoritmo ID3.
# Se utiliza una tabla de datos sobre transporte (Caminar, Camión, Tren) y el clima para decidir si salir o no.

import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn import tree

# Datos de ejemplo: transporte, clima y decisión de salir
data = {
    'Transporte': ['Caminar', 'Caminar', 'Camión', 'Camión', 'Tren', 'Tren'],
    'Clima': ['Soleado', 'Lluvioso', 'Soleado', 'Lluvioso', 'Soleado', 'Lluvioso'],
    'Salir': ['Sí', 'No', 'Sí', 'No', 'Sí', 'No']
}

# Convertimos a DataFrame
df = pd.DataFrame(data)

# Convertir variables categóricas a numéricas
X = pd.get_dummies(df[['Transporte', 'Clima']])
y = df['Salir']

# Creamos el árbol de decisión usando ID3 (criterio="entropy")
modelo = DecisionTreeClassifier(criterion="entropy")
modelo.fit(X, y)

# Visualización del árbol
tree.plot_tree(modelo, feature_names=X.columns, class_names=modelo.classes_, filled=True)
