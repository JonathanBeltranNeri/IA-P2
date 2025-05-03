# Jonathan Beltran Neri
# Tema: Conjuntos de Hipótesis - Boosting

from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
import numpy as np

# Atributos: [Clima, Hora del día]
X = np.array([
    ['Soleado', 'Mañana'],
    ['Lluvioso', 'Tarde'],
    ['Nublado', 'Noche'],
    ['Soleado', 'Tarde'],
    ['Lluvioso', 'Noche'],
    ['Nublado', 'Mañana']
])

# Etiquetas: Medios de transporte preferidos
y = np.array(['Caminar', 'Tren', 'Camión', 'Caminar', 'Tren', 'Camión'])

# Codificar las variables categóricas
le_clima = LabelEncoder()
le_hora = LabelEncoder()
X_encoded = np.column_stack((
    le_clima.fit_transform(X[:, 0]),
    le_hora.fit_transform(X[:, 1])
))

le_transporte = LabelEncoder()
y_encoded = le_transporte.fit_transform(y)

# Modelo base: árbol de decisión simple
modelo_base = DecisionTreeClassifier(max_depth=1)

# Aplicar AdaBoost con 10 clasificadores débiles
modelo_boost = AdaBoostClassifier(estimator=modelo_base, n_estimators=10, random_state=42)

modelo_boost.fit(X_encoded, y_encoded)

# Probar con nuevos datos
nuevos_datos = np.array([
    ['Soleado', 'Noche'],
    ['Lluvioso', 'Mañana'],
    ['Nublado', 'Tarde']
])
nuevos_datos_encoded = np.column_stack((
    le_clima.transform(nuevos_datos[:, 0]),
    le_hora.transform(nuevos_datos[:, 1])
))
predicciones = modelo_boost.predict(nuevos_datos_encoded)
predicciones_texto = le_transporte.inverse_transform(predicciones)

# Mostrar resultados
for entrada, salida in zip(nuevos_datos, predicciones_texto):
    print(f"Condiciones: {entrada} → Transporte recomendado: {salida}")
