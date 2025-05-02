## Jonathan Beltran Neri
# Algoritmo: Planificación de Orden Parcial

# Estructura del grafo utilizado:
#
#         Caminar
#         /     \
#     Camión   Tren
#       |        |
#     Taxi     Avión
#       \       /
#       Destino

# Este algoritmo genera un plan parcial sin un orden total entre acciones independientes.
# Es útil cuando varias acciones no dependen unas de otras y pueden ejecutarse en paralelo.

# Acciones representadas como dependencias
acciones = {
    'Camión': ['Caminar'],
    'Tren': ['Caminar'],
    'Taxi': ['Camión'],
    'Avión': ['Tren'],
    'Destino': ['Taxi', 'Avión']
}

# Ordenamiento Topológico Parcial
def orden_parcial(acciones):
    plan = []
    visitados = set()

    def visitar(accion):
        if accion not in visitados:
            for pre in acciones.get(accion, []):
                visitar(pre)
            visitados.add(accion)
            plan.append(accion)

    for accion in acciones:
        visitar(accion)

    return plan[::-1]  # Se invierte para tener el orden de ejecución

# Ejecutar planificación
plan = orden_parcial(acciones)

# Mostrar resultado
print("Planificación de Orden Parcial:")
print(" → ".join(plan))
