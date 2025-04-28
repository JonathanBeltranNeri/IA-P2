## Jonathan Beltran Neri
# Tema: Encadenamiento: Hacia Delante y Hacia Atrás

# El encadenamiento permite deducir hechos nuevos a partir de una base de conocimiento
# usando dos estrategias:
# - Hacia delante (de los hechos hacia la meta)
# - Hacia atrás (de la meta hacia los hechos necesarios)

# Base de reglas (simuladas sobre transporte)
reglas = [
    {"antecedentes": {"tren_llega"}, "consecuente": "puede_subir"},
    {"antecedentes": {"camion_sale"}, "consecuente": "puede_subir"},
    {"antecedentes": {"no_puede_subir"}, "consecuente": "caminando_llegamos"}
]

# Hechos iniciales
hechos = {"tren_llega"}

# Encadenamiento hacia delante
def encadenamiento_hacia_delante(hechos, reglas, objetivo):
    nuevos_hechos = hechos.copy()
    while True:
        aplicado = False
        for regla in reglas:
            if regla["consecuente"] not in nuevos_hechos and regla["antecedentes"].issubset(nuevos_hechos):
                nuevos_hechos.add(regla["consecuente"])
                aplicado = True
                if objetivo in nuevos_hechos:
                    return True
        if not aplicado:
            return objetivo in nuevos_hechos

# Encadenamiento hacia atrás
def encadenamiento_hacia_atras(hechos, reglas, objetivo):
    if objetivo in hechos:
        return True
    for regla in reglas:
        if regla["consecuente"] == objetivo:
            if all(encadenamiento_hacia_atras(hechos, reglas, antecedente) for antecedente in regla["antecedentes"]):
                return True
    return False

# Ejecutamos los dos métodos para un objetivo
objetivo = "puede_subir"

resultado_adelante = encadenamiento_hacia_delante(hechos, reglas, objetivo)
resultado_atras = encadenamiento_hacia_atras(hechos, reglas, objetivo)

# Mostrar resultados
print(f"¿Se puede llegar a '{objetivo}' por encadenamiento hacia delante? {'Sí' if resultado_adelante else 'No'}")
print(f"¿Se puede llegar a '{objetivo}' por encadenamiento hacia atrás? {'Sí' if resultado_atras else 'No'}")
