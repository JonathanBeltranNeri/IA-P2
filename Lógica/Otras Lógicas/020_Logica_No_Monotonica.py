## Jonathan Beltran Neri
# Tema: Lógica No Monotónica

# En lógica no monotónica, las conclusiones pueden cambiar cuando se añade nueva información,
# a diferencia de la lógica clásica donde las conclusiones son fijas una vez derivadas.

# Simularemos un ejemplo relacionado con transporte.

# Base inicial de conocimiento
hechos = {
    "tren_funciona": True,
    "camion_funciona": True
}

# Reglas basadas en la información actual
def decidir_transporte(hechos):
    if hechos["tren_funciona"]:
        return "viajar en tren"
    elif hechos["camion_funciona"]:
        return "viajar en camión"
    else:
        return "caminar"

# Evaluamos decisión inicial
decision_inicial = decidir_transporte(hechos)

# Ahora llega nueva información: el tren se descompuso
hechos["tren_funciona"] = False

# Re-evaluamos con nueva información
decision_actualizada = decidir_transporte(hechos)

# Mostrar resultados
print("Lógica No Monotónica aplicada al Transporte:")
print(f"Decisión inicial: {decision_inicial}")
print(f"Decisión después de nueva información: {decision_actualizada}")
