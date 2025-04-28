## Jonathan Beltran Neri
# Tema: Algoritmos de Búsqueda Local

# Los algoritmos de búsqueda local exploran el espacio de soluciones
# moviéndose a estados vecinos sin construir caminos completos.

# En este ejemplo simulamos una búsqueda de optimización:
# encontrar el punto más alto en una "colina" de transporte.

import random

# Definimos un entorno de estados simulando una calidad de transporte
# Cada estado representa un tipo de transporte con un valor de "calidad"
transporte_calidad = {
    "caminar": 2,
    "bicicleta": 4,
    "camion": 5,
    "tren": 8,
    "metro": 7,
    "moto": 6
}

# Función para seleccionar un vecino aleatorio
def seleccionar_vecino(actual):
    vecinos = list(transporte_calidad.keys())
    vecinos.remove(actual)
    return random.choice(vecinos)

# Algoritmo de búsqueda local (ascensión de colinas)
def busqueda_local(estado_inicial):
    actual = estado_inicial
    while True:
        vecino = seleccionar_vecino(actual)
        if transporte_calidad[vecino] > transporte_calidad[actual]:
            actual = vecino
        else:
            break  # No hay mejora
    return actual, transporte_calidad[actual]

# Iniciar búsqueda desde "caminar"
estado_final, calidad_final = busqueda_local("caminar")

# Mostrar resultados
print("Resultado de Búsqueda Local (Ascensión de Colinas):")
print(f"Mejor transporte encontrado: {estado_final} con calidad {calidad_final}")
