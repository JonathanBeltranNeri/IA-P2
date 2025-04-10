## Jonathan Beltran Neri
# Algoritmo: Algoritmos Genéticos

# Este algoritmo utiliza principios de la selección natural para encontrar una solución aproximada a un problema.
# Los algoritmos genéticos se basan en la selección de una población de posibles soluciones
# y utilizan operadores como la selección, el cruce y la mutación para generar nuevas soluciones.

import random

# Función de fitness para evaluar las soluciones
def fitness(solution):
    # Ejemplo de función de fitness (por ejemplo, maximizar la suma de los números)
    return sum(solution)

# Función para generar una población inicial
def generar_poblacion(tamano_poblacion, longitud_solucion):
    return [[random.randint(0, 1) for _ in range(longitud_solucion)] for _ in range(tamano_poblacion)]

# Función para seleccionar a los padres utilizando ruleta
def seleccionar_padres(poblacion, fitnesses):
    total_fitness = sum(fitnesses)
    seleccion = random.randint(0, total_fitness)
    acumulado = 0
    for i, fit in enumerate(fitnesses):
        acumulado += fit
        if acumulado >= seleccion:
            return poblacion[i]
    return poblacion[-1]

# Función de cruce (crossover)
def cruce(padre1, padre2):
    punto_cruce = random.randint(1, len(padre1)-1)
    hijo1 = padre1[:punto_cruce] + padre2[punto_cruce:]
    hijo2 = padre2[:punto_cruce] + padre1[punto_cruce:]
    return hijo1, hijo2

# Función de mutación
def mutacion(hijo, tasa_mutacion):
    for i in range(len(hijo)):
        if random.random() < tasa_mutacion:
            hijo[i] = 1 - hijo[i]  # Invertir el valor del bit
    return hijo

# Algoritmo Genético
def algoritmo_genetico(tamano_poblacion, longitud_solucion, generaciones, tasa_mutacion):
    poblacion = generar_poblacion(tamano_poblacion, longitud_solucion)
    for _ in range(generaciones):
        fitnesses = [fitness(individuo) for individuo in poblacion]
        nueva_poblacion = []
        while len(nueva_poblacion) < tamano_poblacion:
            padre1 = seleccionar_padres(poblacion, fitnesses)
            padre2 = seleccionar_padres(poblacion, fitnesses)
            hijo1, hijo2 = cruce(padre1, padre2)
            nueva_poblacion.append(mutacion(hijo1, tasa_mutacion))
            nueva_poblacion.append(mutacion(hijo2, tasa_mutacion))
        
        poblacion = nueva_poblacion
    
    # Mejor solución encontrada
    fitnesses = [fitness(individuo) for individuo in poblacion]
    mejor_solucion = poblacion[fitnesses.index(max(fitnesses))]
    return mejor_solucion

# Parámetros del algoritmo
tamano_poblacion = 10
longitud_solucion = 6
generaciones = 100
tasa_mutacion = 0.01

# Ejecutar el algoritmo genético
mejor_solucion = algoritmo_genetico(tamano_poblacion, longitud_solucion, generaciones, tasa_mutacion)

# Mostrar el resultado
print("Mejor solución encontrada:", mejor_solucion)
print("Fitness de la solución:", fitness(mejor_solucion))
