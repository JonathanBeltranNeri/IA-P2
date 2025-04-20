## Jonathan Beltran Neri
# Algoritmo: Valor de la Información

# Estructura del modelo:
#
# Se analiza si es conveniente obtener más información (por ejemplo, hacer un test)
# antes de tomar una decisión. El valor de la información se mide como la diferencia
# entre la utilidad esperada con la información y sin ella.
#
# Caso: decidir tratar o no tratar a un paciente con o sin realizar una prueba diagnóstica.

# Probabilidades sin información
probabilidades_sin_info = {
    'enfermo': 0.3,
    'sano': 0.7
}

# Utilidades si se actúa sin información
utilidades = {
    ('tratar', 'enfermo'): 100,
    ('no_tratar', 'enfermo'): -100,
    ('tratar', 'sano'): -20,
    ('no_tratar', 'sano'): 0
}

# Decisiones posibles
decisiones = ['tratar', 'no_tratar']

# Utilidad esperada sin información
def utilidad_sin_informacion():
    mejor = float('-inf')
    for decision in decisiones:
        total = 0
        for estado in probabilidades_sin_info:
            total += probabilidades_sin_info[estado] * utilidades[(decision, estado)]
        if total > mejor:
            mejor = total
    return mejor

# Supongamos que con un test perfecto podemos saber el estado real
# Valor esperado con información perfecta
def utilidad_con_informacion():
    total = 0
    for estado in probabilidades_sin_info:
        mejor = float('-inf')
        for decision in decisiones:
            valor = utilidades[(decision, estado)]
            if valor > mejor:
                mejor = valor
        total += probabilidades_sin_info[estado] * mejor
    return total

# Calcular el valor de la información
def valor_de_la_informacion():
    sin_info = utilidad_sin_informacion()
    con_info = utilidad_con_informacion()
    valor_info = con_info - sin_info

    print(f"Utilidad esperada sin información: {sin_info}")
    print(f"Utilidad esperada con información perfecta: {con_info}")
    print(f"Valor de la información: {valor_info}")

# Ejecutar
print("Valor de la Información - Comparación entre actuar con o sin conocer el estado real\n")
valor_de_la_informacion()
