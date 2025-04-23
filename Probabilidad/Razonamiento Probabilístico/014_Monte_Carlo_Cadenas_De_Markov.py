## Jonathan Beltran Neri
# Tema: Monte Carlo para Cadenas de Markov (MCMC)

# El muestreo de Monte Carlo basado en cadenas de Markov (MCMC) genera muestras
# de una distribución construyendo una cadena donde el siguiente estado
# depende solo del estado actual (propiedad de Markov).

# Usaremos el algoritmo de Metropolis-Hastings simplificado para la red: M → N → P

import random

# Distribuciones condicionales
P_M = {True: 0.6, False: 0.4}
P_N_dado_M = {
    True: {True: 0.8, False: 0.2},
    False: {True: 0.3, False: 0.7}
}
P_P_dado_N = {
    True: {True: 0.9, False: 0.1},
    False: {True: 0.5, False: 0.5}
}

# Función para calcular la probabilidad conjunta
def prob_conjunta(m, n, p):
    return P_M[m] * P_N_dado_M[m][n] * P_P_dado_N[n][p]

# Inicialización
estado_actual = {'M': True, 'N': True, 'P': True}
cuenta_P = {True: 0, False: 0}
pasos = 10000
quemado = 1000  # Burn-in

# Variables para muestreo
variables = ['M', 'N', 'P']

for i in range(pasos):
    # Escoger una variable al azar para modificar
    var = random.choice(variables)
    propuesta = estado_actual.copy()
    propuesta[var] = not propuesta[var]  # Cambiar valor booleano

    # Calcular probabilidad conjunta de actual y propuesta
    p_actual = prob_conjunta(estado_actual['M'], estado_actual['N'], estado_actual['P'])
    p_propuesta = prob_conjunta(propuesta['M'], propuesta['N'], propuesta['P'])

    # Aceptar o rechazar
    alpha = min(1, p_propuesta / p_actual)
    if random.random() < alpha:
        estado_actual = propuesta  # Aceptamos el nuevo estado

    # Después del "quemado", contamos el valor de P
    if i >= quemado:
        cuenta_P[estado_actual['P']] += 1

# Normalizar resultados
total = cuenta_P[True] + cuenta_P[False]
print("Monte Carlo con Cadenas de Markov (MCMC) - Estimación de P(P):")
print(f"  True:  {cuenta_P[True] / total:.4f}")
print(f"  False: {cuenta_P[False] / total:.4f}")
