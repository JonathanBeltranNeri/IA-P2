## Jonathan Beltran Neri
# Tema: Incertidumbre y Factores de Certeza

# En los sistemas expertos, cuando no se puede asegurar completamente un hecho,
# se puede usar un "factor de certeza" para representar cuán confiable es la afirmación.

# Simulamos un sistema que evalúa la confiabilidad de ciertos medios de transporte
# para una ruta determinada, con valores de certeza entre -1 y 1.

# Lista de medios evaluados con sus factores de certeza (FC)
evaluaciones = {
    "tren": 0.9,        # Muy seguro que funciona
    "camion": 0.4,      # Algo probable
    "bicicleta": -0.2,  # Poco probable que funcione
    "patineta": -0.7    # Muy poco probable
}

# Clasificación textual del factor de certeza
def interpretar_fc(fc):
    if fc >= 0.75:
        return "con alta certeza"
    elif fc >= 0.25:
        return "probable"
    elif fc > -0.25:
        return "incierto"
    elif fc > -0.75:
        return "poco probable"
    else:
        return "altamente dudoso"

# Mostrar resultados de evaluación
print("Evaluación de Transporte con Factores de Certeza:\n")
for medio, fc in evaluaciones.items():
    interpretacion = interpretar_fc(fc)
    print(f"{medio.capitalize():<10} → FC: {fc:+.2f} → {interpretacion}")
