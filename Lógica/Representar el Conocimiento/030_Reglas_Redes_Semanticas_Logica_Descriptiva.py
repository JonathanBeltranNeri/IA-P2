## Jonathan Beltran Neri
# Tema: Reglas, Redes Semánticas y Lógica Descriptiva

# En esta representación combinamos:
# - Reglas (tipo si-entonces)
# - Redes semánticas (nodos y relaciones)
# - Conceptos de lógica descriptiva para clasificar conocimiento

# Definimos una red semántica básica del dominio transporte
conceptos = {
    "Transporte": ["Tren", "Camión", "Bicicleta"],
    "VehículoMotorizado": ["Tren", "Camión"],
    "VehículoNoMotorizado": ["Bicicleta"]
}

# Relaciones entre conceptos (tipo es_a)
relaciones = [
    ("Tren", "es_a", "VehículoMotorizado"),
    ("Camión", "es_a", "VehículoMotorizado"),
    ("Bicicleta", "es_a", "VehículoNoMotorizado"),
    ("VehículoMotorizado", "es_a", "Transporte"),
    ("VehículoNoMotorizado", "es_a", "Transporte")
]

# Reglas tipo si-entonces (simples)
reglas = [
    ("VehículoMotorizado", "requiere_energía"),
    ("VehículoNoMotorizado", "no_requiere_energía")
]

# Función para inferir propiedades a partir de relaciones y reglas
def inferir_propiedades(objeto):
    inferencias = []
    for (origen, relacion, destino) in relaciones:
        if origen == objeto and relacion == "es_a":
            for antecedente, consecuente in reglas:
                if destino == antecedente:
                    inferencias.append(consecuente)
            # Búsqueda transitiva
            inferencias += inferir_propiedades(destino)
    return inferencias

# Evaluar un ejemplo
objeto = "Camión"
resultado = inferir_propiedades(objeto)

# Mostrar resultados
print(f"Propiedades inferidas para '{objeto}':")
for propiedad in resultado:
    print(f"- {propiedad}")
