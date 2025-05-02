## Jonathan Beltran Neri
# Tema: Eventos y Objetos Mentales – Creencias

# En inteligencia artificial, una creencia representa lo que un agente considera verdadero
# sobre el mundo, aunque pueda estar equivocado.

# En este ejemplo, simulamos las creencias de una persona sobre el transporte disponible.

# Base de creencias del agente
creencias_agente = {
    "tren_funciona": True,
    "camion_funciona": False,
    "bicicleta_disponible": True
}

# Función para mostrar todas las creencias actuales
def mostrar_creencias(creencias):
    print("Base de Creencias del Agente:\n")
    for hecho, valor in creencias.items():
        estado = "cree que sí" if valor else "cree que no"
        print(f"El agente {estado} en '{hecho}'.")

# Función para consultar si el agente cree que puede usar un medio
def puede_usar_transporte(creencias, medio):
    clave = f"{medio}_funciona" if medio != "bicicleta" else "bicicleta_disponible"
    return creencias.get(clave, False)

# Evaluación de decisión del agente
def decidir_transporte(creencias):
    for medio in ["tren", "camion", "bicicleta"]:
        if puede_usar_transporte(creencias, medio):
            return medio
    return "caminar"

# Ejecutar
mostrar_creencias(creencias_agente)
decision = decidir_transporte(creencias_agente)
print(f"\nEl agente decide transportarse usando: {decision}")
