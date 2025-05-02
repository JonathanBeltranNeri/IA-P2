## Jonathan Beltran Neri
# Algoritmo: Planificación Lógica Proposicional (SATPLAN)

# Estructura del grafo utilizado:
#
#         Caminar
#         /     \
#     Camión   Tren
#       |        |
#     Taxi     Avión
#       \       /
#       Destino

# SATPLAN convierte el problema de planificación en una fórmula lógica
# y busca una asignación que la satisfaga.

from itertools import product

# Estado inicial y acciones
estado_inicial = {'Caminar'}
objetivo = {'Destino'}

acciones = [
    {'nombre': 'Camión', 'pre': {'Caminar'}, 'efecto': 'Camión'},
    {'nombre': 'Tren', 'pre': {'Caminar'}, 'efecto': 'Tren'},
    {'nombre': 'Taxi', 'pre': {'Camión'}, 'efecto': 'Taxi'},
    {'nombre': 'Avión', 'pre': {'Tren'}, 'efecto': 'Avión'},
    {'nombre': 'Destino', 'pre': {'Taxi', 'Avión'}, 'efecto': 'Destino'}
]

# Función simplificada para simular SATPLAN
def satplan(estado_inicial, objetivo, acciones, pasos=5):
    estado = estado_inicial.copy()
    plan = []

    for _ in range(pasos):
        for accion in acciones:
            if accion['pre'].issubset(estado):
                estado.add(accion['efecto'])
                plan.append(accion['nombre'])
                if objetivo.issubset(estado):
                    return plan
    return None

# Ejecutar SATPLAN
plan = satplan(estado_inicial, objetivo, acciones)

# Mostrar resultado
print("Planificación Lógica Proposicional (SATPLAN):")
if plan:
    for paso, accion in enumerate(plan, 1):
        print(f"Paso {paso}: {accion}")
else:
    print("No se encontró un plan para alcanzar el objetivo.")
