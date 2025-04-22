## Jonathan Beltran Neri
# Tema: Incertidumbre

# Este ejemplo ilustra cómo la inteligencia artificial representa y gestiona la incertidumbre.
# La incertidumbre surge cuando el agente no tiene información completa sobre el entorno.
# Aquí usamos variables booleanas y escenarios posibles para representar esa falta de certeza.

# Supongamos un sensor de lluvia que puede fallar:
# - Puede decir que está lloviendo cuando no (falso positivo)
# - Puede no detectar lluvia aunque esté lloviendo (falso negativo)

# El agente no sabe con certeza si está lloviendo,
# pero puede asignar una probabilidad basada en la observación del sensor.

# Sensor: "Detecta lluvia"
# ¿Está lloviendo en realidad?

eventos = {
    "llueve": True,
    "sensor_detecta_lluvia": True
}

# Base de probabilidad subjetiva del agente (ejemplo)
# P(llueve) = 0.3 → cree que usualmente no llueve
# P(sensor | llueve) = 0.9 → el sensor detecta lluvia correctamente si llueve
# P(sensor | no_llueve) = 0.2 → sensor se equivoca 20% de las veces

P_llueve = 0.3
P_sensor_si_llueve = 0.9
P_sensor_si_no_llueve = 0.2

# ¿Cuál es la probabilidad de que realmente esté lloviendo si el sensor lo indica?
# Este razonamiento se desarrolla con la Regla de Bayes, pero por ahora se entiende como incertidumbre.

print("Ejemplo de Incertidumbre en un Agente Inteligente")
print("Probabilidad de que llueva:", P_llueve)
print("Probabilidad de que el sensor detecte lluvia si realmente llueve:", P_sensor_si_llueve)
print("Probabilidad de que el sensor detecte lluvia cuando no llueve:", P_sensor_si_no_llueve)
