## Jonathan Beltran Neri
# Algoritmo: Árbol de Regresión M5

# Estructura del grafo utilizado:
#
#         Caminar
#         /     \
#     Camión   Tren
#       |        |
#     Moto     Avion
#       \       /
#        Destino
#
# Este algoritmo utiliza un árbol de regresión M5 para predecir el tiempo estimado
# de llegada a un destino dependiendo del modo de transporte utilizado.

from sklearn.tree import DecisionTreeRegressor
import pandas as pd
import numpy as np

# Datos simulados: tipo de transporte y tiempo estimado (en minutos)
datos = {
    'Transporte': ['Caminar', 'Caminar', 'Camion', 'Camion', 'Tren', 'Tren', 'Moto', 'Moto', 'Avion', 'Avion'],
    'Tiempo': [60, 65, 40, 45, 30, 35, 20, 25, 10, 15]
}

# Convertimos los datos en un DataFrame
df = pd.DataFrame(datos)

# Codificamos el transporte como números para que pueda ser usado en el modelo
df['Transporte_Cod'] = pd.factorize(df['Transporte'])[0]

# Entrenamos el árbol de regresión
X = df[['Transporte_Cod']]
y = df['Tiempo']
modelo = DecisionTreeRegressor()
modelo.fit(X, y)

# Predicción de tiempos para cada transporte
print("Predicción de tiempo estimado por medio de transporte:")
for transporte in df['Transporte'].unique():
    cod = df[df['Transporte'] == transporte]['Transporte_Cod'].iloc[0]
    prediccion = modelo.predict([[cod]])[0]
    print(f"{transporte}: {prediccion:.2f} minutos")
