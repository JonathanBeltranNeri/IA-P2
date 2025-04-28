## Jonathan Beltran Neri
# Tema: Ingeniería del Conocimiento

# La Ingeniería del Conocimiento consiste en capturar, estructurar y representar
# el conocimiento de expertos de manera que pueda ser utilizado por un sistema inteligente.

# En este ejemplo, modelamos conocimiento sobre transporte.

# Base de conocimiento estructurada
conocimiento_transporte = {
    "medios": ["tren", "camión", "bicicleta", "caminar"],
    "propiedades": {
        "tren": {"rapido": True, "caro": True, "ecologico": False},
        "camión": {"rapido": False, "caro": False, "ecologico": False},
        "bicicleta": {"rapido": False, "caro": False, "ecologico": True},
        "caminar": {"rapido": False, "caro": False, "ecologico": True}
    }
}

# Ejemplo de consulta: buscar medios de transporte que sean ecológicos
def medios_ecologicos(base_conocimiento):
    resultados = []
    for medio, propiedades in base_conocimiento["propiedades"].items():
        if propiedades.get("ecologico"):
            resultados.append(medio)
    return resultados

# Ejecutar consulta
resultado_ecologico = medios_ecologicos(conocimiento_transporte)

# Mostrar resultados
print("Medios de Transporte Ecológicos Identificados:")
for medio in resultado_ecologico:
    print(f"- {medio}")
