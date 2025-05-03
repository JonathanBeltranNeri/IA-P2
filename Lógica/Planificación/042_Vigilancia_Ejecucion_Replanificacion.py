## Jonathan Beltran Neri
# Algoritmo: Vigilancia de Ejecución y Replanificación

# Estructura del grafo utilizado:
#
#         Caminar
#         /     \
#     Camión   Tren
#       |        |
#     Taxi     Avión
#       \       /
#       Destino

# Este algoritmo supervisa cada paso de la planificación.
# Si una acción falla durante la ejecución, replantea un nuevo camino.

# Estado dinámico de los medios de transporte
estado_medio = {
    "Caminar": True,
    "Camión": True,
    "Tren": False,   # Se descompone el tren a mitad del plan
    "Taxi": True,
    "Avión": True
}

# Plan inicial preferido
plan_inicial = ["Caminar", "Tren", "Avión", "Destino"]

# Función de ejecución con vigilancia
def ejecutar_plan(plan):
    plan_final = []
    for paso in plan:
        if estado_medio.get(paso, True):
            plan_final.append(paso)
        else:
            print(f" Fallo detectado en: {paso}")
            nuevo_plan = replanificar(paso)
            plan_final.extend(nuevo_plan)
            break
    return plan_final

# Replanificación a partir del punto de falla
def replanificar(fallo):
    if fallo == "Tren":
        print("Replanificando vía Camión + Taxi...")
        if estado_medio["Camión"] and estado_medio["Taxi"]:
            return ["Camión", "Taxi", "Destino"]
    return ["Destino"]  # Plan mínimo si no hay opciones

# Ejecutar la vigilancia y replanificación
plan_final = ejecutar_plan(plan_inicial)

# Mostrar resultado
print("\nPlan final ejecutado:")
for paso, accion in enumerate(plan_final, 1):
    print(f"Paso {paso}: {accion}")
