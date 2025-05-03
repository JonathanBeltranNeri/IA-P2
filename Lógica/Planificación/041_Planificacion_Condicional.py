## Jonathan Beltran Neri
# Algoritmo: Planificación Condicional

# Estructura del grafo utilizado:
#
#         Caminar
#         /     \
#     Camión   Tren
#       |        |
#     Taxi     Avión
#       \       /
#       Destino

# Este algoritmo considera decisiones condicionadas al entorno.
# Si una ruta no está disponible, intenta una alternativa.

# Definimos disponibilidad de medios
estado_medio = {
    "Caminar": True,
    "Camión": False,  # Ruta no disponible
    "Tren": True,
    "Taxi": True,
    "Avión": False    # Avión fuera de servicio
}

# Función para planificar condicionalmente
def planificacion_condicional():
    plan = []

    if estado_medio["Caminar"]:
        plan.append("Caminar")

        if estado_medio["Camión"]:
            plan.append("Camión")
            if estado_medio["Taxi"]:
                plan.append("Taxi")
                plan.append("Destino")
        elif estado_medio["Tren"]:
            plan.append("Tren")
            if estado_medio["Avión"]:
                plan.append("Avión")
                plan.append("Destino")
            else:
                plan.append("Destino")  # Tren directo
    else:
        plan.append("No hay forma de comenzar el viaje")

    return plan

# Ejecutar la planificación
plan = planificacion_condicional()

# Mostrar resultado
print("Planificación Condicional:")
for paso, accion in enumerate(plan, 1):
    print(f"Paso {paso}: {accion}")
