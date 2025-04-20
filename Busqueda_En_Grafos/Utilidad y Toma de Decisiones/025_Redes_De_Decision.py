## Jonathan Beltran Neri
# Algoritmo: Redes de Decisión

# Estructura del modelo utilizado:
#
# Este ejemplo simula una red de decisión donde un agente debe decidir si tratar o no a un paciente,
# sin hacer pruebas previas, considerando las probabilidades de que esté enfermo o sano,
# y las utilidades de cada combinación de decisión y estado real.
#
#         [Decisión]
#              ↓
#         [Estado real]
#              ↓
#          [Utilidad]
#
# Este algoritmo calcula la utilidad esperada para cada decisión
# y recomienda la mejor según la máxima utilidad esperada.

# Probabilidades de los estados del mundo
probabilidades = {
    'enfermo': 0.3,
    'sano': 0.7
}

# Utilidades para cada decisión dada una condición real
utilidades = {
    ('tratar', 'enfermo'): 100,
    ('no_tratar', 'enfermo'): -100,
    ('tratar', 'sano'): -20,
    ('no_tratar', 'sano'): 0
}

# Decisiones posibles
decisiones = ['tratar', 'no_tratar']

# Calcular la utilidad esperada de cada decisión
def utilidad_esperada(decision):
    utilidad_total = 0
    for estado in probabilidades:
        prob = probabilidades[estado]
        utilidad = utilidades[(decision, estado)]
        utilidad_total += prob * utilidad
    return utilidad_total

# Evaluar todas las decisiones posibles
def evaluar_red_de_decision():
    mejor_decision = None
    mejor_utilidad = float('-inf')

    print("Evaluando utilidad esperada para cada decisión:\n")

    for decision in decisiones:
        utilidad = utilidad_esperada(decision)
        print(f" - Decisión '{decision}': Utilidad esperada = {utilidad}")
        if utilidad > mejor_utilidad:
            mejor_utilidad = utilidad
            mejor_decision = decision

    print(f"\nMejor decisión: '{mejor_decision.upper()}' con utilidad esperada de {mejor_utilidad}")

# Ejecutar
print("Red de Decisión - Evaluación de decisiones sin prueba previa")
evaluar_red_de_decision()
