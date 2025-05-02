## Jonathan Beltran Neri
# Tema: Razonamiento por Defecto y No Monotónico

# En el razonamiento por defecto, un sistema puede suponer que algo es verdadero
# mientras no haya evidencia en contra. Si aparece nueva información, la conclusión puede cambiar.

# Simulamos un sistema que supone que todos los medios de transporte funcionan,
# a menos que se indique lo contrario.

# Conjunto de hechos conocidos (parciales)
hechos = {
    "tren_funciona": True,
    # "camion_funciona" no ha sido especificado
    "bicicleta_funciona": False
}

# Suposiciones por defecto
def funciona(medio, hechos):
    clave = f"{medio}_funciona"
    return hechos.get(clave, True)  # Si no se sabe, se asume que funciona

# Evaluar funcionamiento de varios medios
medios = ["tren", "camion", "bicicleta", "patineta"]

# Mostrar evaluación con razonamiento no monotónico
print("Evaluación de funcionamiento (razonamiento por defecto):\n")
for medio in medios:
    estado = funciona(medio, hechos)
    fuente = "hecho" if f"{medio}_funciona" in hechos else "asumido por defecto"
    print(f"{medio.capitalize():<10} → funciona: {'Sí' if estado else 'No'} ({fuente})")
