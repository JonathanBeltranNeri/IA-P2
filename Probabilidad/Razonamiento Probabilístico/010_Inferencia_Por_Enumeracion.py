## Jonathan Beltran Neri
# Tema: Inferencia por Enumeración

# Este algoritmo calcula la probabilidad de una variable (consulta)
# dada una evidencia, sumando sobre todas las combinaciones posibles
# de las demás variables.

# Nota: Este ejemplo se basa en una red simplificada derivada del grafo principal.

# Definimos una red bayesiana con variables binarias (True/False)
# y tablas de probabilidad condicional (simplificadas para claridad)

# Dependencias:
# M → N → P

# Tabla de probabilidades (P)
P = {
    'M': {True: 0.6, False: 0.4},
    'N': {
        True: {True: 0.8, False: 0.2},   # P(N=True | M)
        False: {True: 0.3, False: 0.7}   # P(N=True | not M)
    },
    'P': {
        True: {True: 0.9, False: 0.1},   # P(P=True | N)
        False: {True: 0.5, False: 0.5}
    }
}

# Enumeración de todas las combinaciones posibles de variables no observadas
def enumerate_all(variables, evidence):
    if not variables:
        return 1.0
    first = variables[0]
    rest = variables[1:]

    if first in evidence:
        prob = probability(first, evidence[first], evidence)
        return prob * enumerate_all(rest, evidence)
    else:
        total = 0
        for val in [True, False]:
            evidence_extended = evidence.copy()
            evidence_extended[first] = val
            prob = probability(first, val, evidence)
            total += prob * enumerate_all(rest, evidence_extended)
        return total

# Función de probabilidad condicional
def probability(var, val, evidence):
    if var == 'M':
        return P['M'][val]
    elif var == 'N':
        return P['N'][evidence['M']][val]
    elif var == 'P':
        return P['P'][evidence['N']][val]

# Función principal de inferencia
def inference(query_var, evidence):
    vars_all = ['M', 'N', 'P']
    hidden_vars = [v for v in vars_all if v != query_var and v not in evidence]
    distribution = {}
    for val in [True, False]:
        evidence_extended = evidence.copy()
        evidence_extended[query_var] = val
        prob = enumerate_all(vars_all, evidence_extended)
        distribution[val] = prob
    # Normalizar
    total = sum(distribution.values())
    for val in distribution:
        distribution[val] /= total
    return distribution

# Consulta: P(P=True | M=True)
resultado = inference('P', {'M': True})
print("Inferencia por Enumeración:")
print("P(P | M=True):")
for val in resultado:
    print(f"  {val}: {resultado[val]:.4f}")
