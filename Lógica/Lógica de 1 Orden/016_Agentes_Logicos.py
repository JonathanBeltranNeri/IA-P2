## Jonathan Beltran Neri
# Tema: Agentes Lógicos

# Un agente lógico percibe su entorno, razona utilizando una base de conocimiento,
# y toma decisiones basadas en inferencias lógicas.

# Simularemos un agente de transporte que decide cómo llegar a destino.

# Base de conocimiento: condiciones
condiciones = {
    "tren_disponible": True,
    "camion_disponible": False,
    "caminando_posible": True
}

# Reglas de decisión
def decidir_medio(condiciones):
    if condiciones["tren_disponible"]:
        return "tren"
    elif condiciones["camion_disponible"]:
        return "camión"
    elif condiciones["caminando_posible"]:
        return "caminar"
    else:
        return "sin transporte disponible"

# Función del agente
def agente_logico(condiciones):
    medio = decidir_medio(condiciones)
    return medio

# Ejecutar agente
medio_seleccionado = agente_logico(condiciones)

# Mostrar resultado
print("Agente Lógico - Selección de Medio de Transporte:")
print(f"Medio seleccionado: {medio_seleccionado}")
