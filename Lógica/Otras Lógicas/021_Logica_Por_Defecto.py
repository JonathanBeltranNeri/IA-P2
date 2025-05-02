## Jonathan Beltran Neri
# Tema: Lógica por Defecto

# La lógica por defecto permite hacer suposiciones razonables en ausencia de información completa,
# mientras se mantiene la posibilidad de retractarse si aparece información que contradiga la suposición.

# Ejemplo: suponer que todos los medios de transporte están funcionando, a menos que se indique lo contrario.

# Hechos conocidos (incompletos)
hechos = {
    "tren_funciona": True,
    # "camion_funciona" está ausente
}

# Suposición por defecto
def suponer_funcionamiento(medio, hechos):
    return hechos.get(medio, True)  # Se asume que funciona si no se dice lo contrario

# Aplicamos lógica por defecto
estado_tren = suponer_funcionamiento("tren_funciona", hechos)
estado_camion = suponer_funcionamiento("camion_funciona", hechos)

# Mostrar resultados
print("Lógica por Defecto aplicada al Transporte:")
print(f"¿El tren funciona? {'Sí' if estado_tren else 'No'}")
print(f"¿El camión funciona? {'Sí' if estado_camion else 'No'} (asumido por defecto)")
