## Jonathan Beltran Neri
# Tema: Ponderación de Verosimilitud (Likelihood Weighting)

# Esta técnica permite estimar probabilidades condicionales en redes bayesianas
# sin rechazar muestras como en el muestreo por rechazo.
# Se generan muestras forzando la evidencia y asignando un peso a cada muestra según su verosimilitud.

import random

# Red simplificada: M → N → P

P_M = {True: 0.6, False: 0.4}
P_N_dado_M = {
    True: {True: 0.8, False: 0.2},
    False: {True: 0.3, False: 0.7}
}
P_P_dado_N = {
    True: {True: 0.9, False: 0.1},
    False: {True: 0.5, False: 0.5}
}

# Función para generar una muestra con ponderación de verosimilitud
def muestra_ponderada(evidencia):
    peso = 1.0
    muestra = {}

    # Variable M
    if 'M' in evidencia:
        m_val = evidencia['M']
        peso *= P_M[m_val]
    else:
        m_val = random.random() < P_M[True]
    muestra['M'] = m_val

    # Variable N
    if 'N' in evidencia:
        n_val = evidencia['N']
        peso *= P_N_dado_M[m_val][n_val]
    else:
        n_val = random.random() < P_N_dado_M[m_val][True]
    muestra['N'] = n_val

    # Variable P
    if 'P' in evidencia:
        p_val = evidencia['P']
        peso *= P_P_dado_N[n_val][p_val]
    else:
        p_val = random.random() < P_P_dado_N[n_val][True]
    muestra['P'] = p_val

    return muestra, peso

# Ejecutamos el muestreo
num_muestras = 10000
conteo = {True: 0.0, False: 0.0}
evidencia = {'M': True}  # Queremos P(P | M=True)

for _ in range(num_muestras):
    muestra, peso = muestra_ponderada(evidencia)
    conteo[muestra['P']] += peso

# Normalizar
total = conteo[True] + conteo[False]
print("Ponderación de Verosimilitud - P(P | M=True):")
print(f"  True:  {conteo[True] / total:.4f}")
print(f"  False: {conteo[False] / total:.4f}")
