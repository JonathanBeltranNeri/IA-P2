## Jonathan Beltran Neri
# Tema: Sintaxis y Semántica - Cuantificadores

# En lógica de primer orden, los cuantificadores nos permiten hablar sobre todos
# o algunos elementos de un dominio.

# Usamos dos tipos principales:
# - ∀ (para todo / "todos")
# - ∃ (existe / "al menos uno")

# Simularemos ejemplos de transporte:

# Conjunto de ciudades con transporte disponible
ciudades = {
    "Guadalajara": {"tren": True, "camion": True},
    "Puebla": {"tren": False, "camion": True},
    "Querétaro": {"tren": True, "camion": False},
    "Veracruz": {"tren": False, "camion": True}
}

# Cuantificador Universal (∀): ¿En todas las ciudades hay tren?
def todos_tienen_tren(ciudades):
    return all(info["tren"] for info in ciudades.values())

# Cuantificador Existencial (∃): ¿Existe alguna ciudad con camión?
def existe_ciudad_con_camion(ciudades):
    return any(info["camion"] for info in ciudades.values())

# Mostrar resultados
print("Evaluación de Cuantificadores sobre Transporte:\n")
print(f"¿Todas las ciudades tienen tren? {'Sí' if todos_tienen_tren(ciudades) else 'No'}")
print(f"¿Existe al menos una ciudad con camión? {'Sí' if existe_ciudad_con_camion(ciudades) else 'No'}")
