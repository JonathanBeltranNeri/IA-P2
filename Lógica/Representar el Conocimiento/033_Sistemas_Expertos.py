## Jonathan Beltran Neri
# Tema: Sistemas Expertos

# Un sistema experto emula la decisión de un experto humano en un área específica.
# Se basa en reglas del tipo "si-entonces", utilizando hechos conocidos para inferir conclusiones.

# Supongamos un sistema experto que recomienda un medio de transporte en función de ciertos hechos.

# Base de conocimientos (reglas y hechos)
hechos = {
    "es_urgente": True,
    "es_lejos": True,
    "hay_trafico": False
}

# Reglas del sistema experto
def sistema_experto(hechos):
    if hechos["es_urgente"] and hechos["es_lejos"] and not hechos["hay_trafico"]:
        return "Recomendación: Usa el tren."
    elif hechos["es_urgente"] and hechos["hay_trafico"]:
        return "Recomendación: Usa bicicleta o camina."
    elif not hechos["es_lejos"] and not hechos["es_urgente"]:
        return "Recomendación: Puedes usar la patineta."
    else:
        return "Recomendación: Usa el camión."

# Ejecutar el sistema experto
print("Sistema Experto de Recomendación de Transporte")
print("Hechos actuales:", hechos)
print(sistema_experto(hechos))
