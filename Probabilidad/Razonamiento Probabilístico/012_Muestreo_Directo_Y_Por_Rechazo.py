## Jonathan Beltran Neri
# Tema: Muestreo Directo y Por Rechazo

# En lugar de calcular las probabilidades de manera exacta,
# estos métodos aproximan la distribución usando simulaciones aleatorias.

# Red simplificada: M → N → P
import random

# Probabilidades (simulación de una red bayesiana)
P_M = {True: 0.6, False: 0.4}
P_N_dado_M = {
    True: {True: 0.8, False: 0.2},
    False: {True: 0.3, False: 0.7}
}
P_P_dado_N = {
    True: {True: 0.9, False: 0.1},
    False: {True: 0.5, False: 0.5}
}

# Genera una muestra usando muestreo directo
def muestreo_directo():
    M = random.random() < P_M[True]
    N = random.random() < P_N_dado_M[M][True]
    P = random.random() < P_P_dado_N[N][True]
    return {'M': M, 'N': N, 'P': P}

# Muestreo por rechazo: solo cuenta muestras que cumplen con la evidencia
def muestreo_por_rechazo(evidencia, cantidad):
    muestras_validas = []
    for _ in range(cantidad * 2):  # Generamos más para compensar el rechazo
        muestra = muestreo_directo()
        if all(muestra[var] == val for var, val in evidencia.items()):
            muestras_validas.append(muestra)
            if len(muestras_validas) == cantidad:
                break
    return muestras_validas

# Usamos ambas técnicas para aproximar P(P | M=True)
num_muestras = 10000
cuenta_directo = {True: 0, False: 0}
cuenta_rechazo = {True: 0, False: 0}

# Muestreo directo con filtro
for _ in range(num_muestras):
    muestra = muestreo_directo()
    if muestra['M'] == True:
        cuenta_directo[muestra['P']] += 1

# Muestreo por rechazo con M=True
muestras_rechazo = muestreo_por_rechazo({'M': True}, num_muestras)
for muestra in muestras_rechazo:
    cuenta_rechazo[muestra['P']] += 1

# Normalización
total_directo = cuenta_directo[True] + cuenta_directo[False]
total_rechazo = cuenta_rechazo[True] + cuenta_rechazo[False]

print("Muestreo Directo - P(P | M=True):")
print(f"  True:  {cuenta_directo[True] / total_directo:.4f}")
print(f"  False: {cuenta_directo[False] / total_directo:.4f}")

print("\nMuestreo por Rechazo - P(P | M=True):")
print(f"  True:  {cuenta_rechazo[True] / total_rechazo:.4f}")
print(f"  False: {cuenta_rechazo[False] / total_rechazo:.4f}")
