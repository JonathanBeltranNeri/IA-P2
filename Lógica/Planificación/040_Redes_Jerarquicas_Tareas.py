## Jonathan Beltran Neri
# Algoritmo: Redes Jerárquicas de Tareas (HTN)

# Estructura del grafo utilizado:
#
#         Caminar
#         /     \
#     Camión   Tren
#       |        |
#     Taxi     Avión
#       \       /
#       Destino

# Este algoritmo descompone una tarea compleja ("Viajar al destino")
# en subtareas más simples, hasta llegar a acciones primitivas.

# Definimos las tareas y subtareas
tareas = {
    "Viajar al destino": ["Llegar por tierra", "Llegar por aire"],
    "Llegar por tierra": ["Caminar", "Camión", "Taxi"],
    "Llegar por aire": ["Caminar", "Tren", "Avión"],
    "Caminar": [],
    "Camión": [],
    "Taxi": [],
    "Tren": [],
    "Avión": [],
    "Destino": []
}

# Función para expandir tareas jerárquicamente
def descomponer_tarea(tarea):
    plan = []
    pila = [tarea]
    
    while pila:
        actual = pila.pop()
        subtareas = tareas.get(actual, [])
        if not subtareas:
            plan.append(actual)
        else:
            pila.extend(reversed(subtareas))
    
    return plan

# Ejecutar la descomposición desde la tarea raíz
plan = descomponer_tarea("Viajar al destino")

# Mostrar resultado
print("Red Jerárquica de Tareas (HTN):")
print("Plan generado:")
for paso, accion in enumerate(plan, 1):
    print(f"Paso {paso}: {accion}")
