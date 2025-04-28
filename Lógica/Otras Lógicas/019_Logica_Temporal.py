## Jonathan Beltran Neri
# Tema: Lógica Temporal

# La lógica temporal permite razonar sobre cómo cambian los hechos a lo largo del tiempo,
# usando operadores como "siempre", "eventualmente", "hasta que", etc.

# Simularemos un ejemplo sencillo relacionado con transporte.

# Estado del transporte a lo largo del tiempo (simulado por lista)
# Cada elemento representa el estado en un momento diferente
estados = [
    {"tren_llega": False, "camion_sale": True},
    {"tren_llega": True, "camion_sale": True},
    {"tren_llega": True, "camion_sale": False}
]

# Operadores temporales
def siempre_tren_llega(estados):
    return all(estado["tren_llega"] for estado in estados)

def eventualmente_tren_llega(estados):
    return any(estado["tren_llega"] for estado in estados)

# Evaluamos
siempre = siempre_tren_llega(estados)
eventualmente = eventualmente_tren_llega(estados)

# Mostrar resultados
print("Lógica Temporal aplicada al Transporte:")
print(f"¿Siempre llega el tren? {'Sí' if siempre else 'No'}")
print(f"¿Eventualmente llega el tren? {'Sí' if eventualmente else 'No'}")
