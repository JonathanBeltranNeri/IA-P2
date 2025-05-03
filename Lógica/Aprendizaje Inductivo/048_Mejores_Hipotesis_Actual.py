# Jonathan Beltran Neri
# Tema: Mejor Hipótesis Actual

# Estructura del grafo utilizado:
#
#         Caminar
#         /     \
#     Camión   Tren
#       |        |
#    Bicicleta  Taxi
#       \       /
#       Destino

# Este algoritmo busca entre varias hipótesis cuál es la que mejor explica los datos observados,
# eligiendo la hipótesis con mayor número de aciertos.

# Observaciones reales (medio usado en cada caso)
observaciones = ['Camión', 'Tren', 'Tren', 'Caminar', 'Camión', 'Tren', 'Bicicleta']

# Conjunto de hipótesis posibles
hipotesis = {
    'H1': ['Camión'] * len(observaciones),
    'H2': ['Tren'] * len(observaciones),
    'H3': ['Caminar', 'Camión', 'Tren', 'Caminar', 'Camión', 'Tren', 'Caminar'],
    'H4': ['Camión', 'Tren', 'Tren', 'Caminar', 'Camión', 'Tren', 'Bicicleta'],  # coincide perfectamente
}

# Función para calcular cuántos aciertos tiene una hipótesis
def evaluar_hipotesis(hip, datos):
    return sum(1 for h, d in zip(hip, datos) if h == d)

# Evaluar todas las hipótesis y encontrar la mejor
mejor = None
mayor_aciertos = -1

for nombre, h in hipotesis.items():
    aciertos = evaluar_hipotesis(h, observaciones)
    print(f"{nombre}: {aciertos} aciertos")
    if aciertos > mayor_aciertos:
        mayor_aciertos = aciertos
        mejor = nombre

print(f"\nLa mejor hipótesis actual es: {mejor} con {mayor_aciertos} aciertos")
