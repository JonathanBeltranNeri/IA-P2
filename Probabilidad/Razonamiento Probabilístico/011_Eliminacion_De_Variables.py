## Jonathan Beltran Neri
# Tema: Eliminación de Variables

# Este algoritmo es una optimización de la inferencia por enumeración.
# En lugar de generar todas las combinaciones posibles, elimina variables intermedias
# mediante factores, reduciendo el costo computacional.

# Red simplificada basada en el grafo:
# M → N → P

# Variables binarios (True / False)
# Usamos factores en forma de diccionarios

# Probabilidades
P_M = {True: 0.6, False: 0.4}

P_N_dado_M = {
    True: {True: 0.8, False: 0.2},
    False: {True: 0.3, False: 0.7}
}

P_P_dado_N = {
    True: {True: 0.9, False: 0.1},
    False: {True: 0.5, False: 0.5}
}

# Multiplica dos factores
def multiplicar_factores(f1, f2, var):
    resultado = {}
    for val1 in [True, False]:
        for val2 in [True, False]:
            if var == 'M':
                prob = f1[val1] * f2[val1]
                resultado[val1] = prob
            else:
                prob = f1[val1] * f2[val2]
                resultado[(val1, val2)] = prob
    return resultado

# Elimina una variable sumando sobre sus valores
def eliminar_variable(factor, var_index):
    nuevo_factor = {}
    for clave in factor:
        clave_sin_var = tuple(x for i, x in enumerate(clave) if i != var_index)
        nuevo_factor[clave_sin_var] = nuevo_factor.get(clave_sin_var, 0) + factor[clave]
    return nuevo_factor

# Construcción de factores
factor_M = P_M
factor_NM = {(n, m): P_N_dado_M[m][n] for m in [True, False] for n in [True, False]}
factor_PN = {(p, n): P_P_dado_N[n][p] for n in [True, False] for p in [True, False]}

# Paso 1: eliminar N
# Multiplicamos los factores que contienen N: factor_NM y factor_PN
factor_con_N = {}
for n in [True, False]:
    for m in [True, False]:
        for p in [True, False]:
            clave = (p, n, m)
            prob = factor_PN[(p, n)] * factor_NM[(n, m)]
            factor_con_N[clave] = prob

# Eliminar N (índice 1 en la tupla)
factor_sin_N = eliminar_variable(factor_con_N, 1)

# Paso 2: multiplicar con P(M)
factor_final = {}
for (p, m) in factor_sin_N:
    factor_final[(p, m)] = factor_sin_N[(p, m)] * factor_M[m]

# Normalizar para obtener P(P | M=True)
P_true = factor_final[(True, True)]
P_false = factor_final[(False, True)]
suma = P_true + P_false

print("Eliminación de Variables:")
print("P(P | M=True):")
print(f"  True: {P_true / suma:.4f}")
print(f"  False: {P_false / suma:.4f}")
