## Jonathan Beltran Neri
# Algoritmo: Planificación Continua y Multiagente

# Estructura del grafo utilizado:
#
#         Caminar
#         /     \
#     Camión   Tren
#       |        |
#     Taxi     Avión
#       \       /
#       Destino

# Este algoritmo simula múltiples agentes planificando sus rutas de forma continua,
# ajustando decisiones si los recursos (transportes) se saturan o fallan.

import random

# Definimos el grafo de transporte
grafo = {
    "Caminar": ["Camión", "Tren"],
    "Camión": ["Taxi"],
    "Tren": ["Avión"],
    "Taxi": ["Destino"],
    "Avión": ["Destino"],
    "Destino": []
}

# Estado de disponibilidad de los medios
disponibilidad = {
    "Caminar": True,
    "Camión": True,
    "Tren": True,
    "Taxi": True,
    "Avión": True
}

# Agentes y sus planes preferidos
agentes = {
    "Agente_A": ["Caminar", "Tren", "Avión", "Destino"],
    "Agente_B": ["Caminar", "Camión", "Taxi", "Destino"]
}

# Simula ejecución continua y coordinada de planes
def ejecutar_multiagente(agentes, disponibilidad):
    resultados = {}
    for nombre, plan in agentes.items():
        resultado = []
        print(f"\n{name_format(nombre)} inicia su planificación:")
        for paso in plan:
            if disponibilidad.get(paso, True):
                resultado.append(paso)
            else:
                print(f" - {paso} no disponible. Buscando alternativa...")
                alternativa = buscar_alternativa(paso)
                if alternativa:
                    resultado.append(alternativa)
                else:
                    resultado.append("ERROR")
                    break
        resultados[nombre] = resultado
    return resultados

# Buscar alternativa sencilla si un transporte falla
def buscar_alternativa(paso):
    if paso == "Tren":
        return "Camión"
    elif paso == "Camión":
        return "Tren"
    elif paso == "Avión":
        return "Taxi"
    elif paso == "Taxi":
        return "Avión"
    return None

# Dar formato limpio a los nombres
def name_format(name):
    return name.replace("_", " ")

# Ejecutar simulación
resultado_final = ejecutar_multiagente(agentes, disponibilidad)

# Mostrar rutas finales
print("\nResultados finales por agente:")
for agente, ruta in resultado_final.items():
    print(f"{name_format(agente)}: {' → '.join(ruta)}")
