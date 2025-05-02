## Jonathan Beltran Neri
# Algoritmo: Grafos de Planificación (GRAPHPLAN)

# Estructura del grafo utilizado:
#
#         Caminar
#         /     \
#     Camión   Tren
#       |        |
#     Taxi     Avión
#       \       /
#       Destino

# Este algoritmo construye un grafo de planificación donde alternan niveles de acciones y estados.
# Requiere encontrar un plan que conduzca desde el estado inicial hasta el objetivo.

# Estado inicial y acciones con precondiciones y efectos
estado_inicial = {'Caminar'}
objetivo = {'Destino'}

acciones = [
    {'nombre': 'Camión', 'pre': {'Caminar'}, 'efectos': {'Camión'}},
    {'nombre': 'Tren', 'pre': {'Caminar'}, 'efectos': {'Tren'}},
    {'nombre': 'Taxi', 'pre': {'Camión'}, 'efectos': {'Taxi'}},
    {'nombre': 'Avión', 'pre': {'Tren'}, 'efectos': {'Avión'}},
    {'nombre': 'Destino', 'pre': {'Taxi', 'Avión'}, 'efectos': {'Destino'}}
]

# Construcción del grafo de planificación (simplificado)
def graphplan(estado_inicial, objetivo, acciones, max_niveles=10):
    niveles = [estado_inicial.copy()]
    plan = []

    for nivel in range(max_niveles):
        nuevos_hechos = niveles[-1].copy()
        acciones_aplicadas = []

        for accion in acciones:
            if accion['pre'].issubset(niveles[-1]):
                nuevos_hechos.update(accion['efectos'])
                acciones_aplicadas.append(accion['nombre'])

        plan.append(acciones_aplicadas)
        niveles.append(nuevos_hechos)

        if objetivo.issubset(nuevos_hechos):
            return plan[:nivel + 1]

    return None

# Ejecutar GRAPHPLAN
plan = graphplan(estado_inicial, objetivo, acciones)

# Mostrar resultado
print("Grafo de Planificación (GRAPHPLAN):")
if plan:
    for i, nivel in enumerate(plan):
        print(f"Nivel {i+1}: Acciones ejecutadas → {nivel}")
else:
    print("No se encontró un plan para alcanzar el objetivo.")
