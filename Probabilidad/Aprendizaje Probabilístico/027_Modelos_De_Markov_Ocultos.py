## Jonathan Beltran Neri
# Tema: Modelos de Markov Ocultos (HMM)

# Este ejemplo usa la librería hmmlearn para crear un HMM que modele 
# los medios de transporte como estados ocultos (Tren, Camión, Caminando),
# basándose en observaciones numéricas de sonidos.

from hmmlearn import hmm
import numpy as np

# Simulamos 3 tipos de observaciones (características acústicas)
# Cada estado corresponde a un medio de transporte
# Cada muestra es: [duración del sonido, volumen]

# Estado 0: Tren
tren = np.random.normal(loc=[8, 9], scale=0.5, size=(10, 2))

# Estado 1: Camión
camion = np.random.normal(loc=[5, 6], scale=0.5, size=(10, 2))

# Estado 2: Caminando
caminando = np.random.normal(loc=[2, 2], scale=0.5, size=(10, 2))

# Unimos los datos
X = np.vstack([tren, camion, caminando])
longitudes = [10, 10, 10]  # Número de muestras por secuencia

# Creamos el modelo HMM (GaussianHMM)
modelo = hmm.GaussianHMM(n_components=3, covariance_type="diag", n_iter=100, random_state=42)

# Entrenamos el modelo
modelo.fit(X, lengths=longitudes)

# Predecimos la secuencia de estados
estados_ocultos = modelo.predict(X)

# Mostrar resultados
print("Modelo de Markov Oculto - Estados estimados:")
for i, obs in enumerate(X):
    print(f"  Observación {i+1:02d}: duración={obs[0]:.2f}, volumen={obs[1]:.2f} → Estado {estados_ocultos[i]}")
