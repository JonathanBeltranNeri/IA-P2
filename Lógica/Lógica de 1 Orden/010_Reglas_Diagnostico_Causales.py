## Jonathan Beltran Neri
# Tema: Reglas de Diagnóstico y Causales

# En Lógica de Primer Orden, las reglas de diagnóstico permiten identificar causas
# a partir de síntomas, y las reglas causales describen cómo un evento genera otro.

# Ejemplo de transporte:

# Base de conocimiento: hechos
hechos = {
    "retraso_tren": True,
    "lluvia": True,
    "accidente_en_ruta": False
}

# Reglas causales y de diagnóstico
def diagnostico(hechos):
    resultados = {}

    # Diagnóstico: si hay retraso del tren y llueve, entonces causa probable = lluvia
    if hechos["retraso_tren"] and hechos["lluvia"]:
        resultados["causa_retraso"] = "lluvia"
    
    # Diagnóstico alternativo: si hay retraso y accidente en ruta
    elif hechos["retraso_tren"] and hechos["accidente_en_ruta"]:
        resultados["causa_retraso"] = "accidente en ruta"
    
    else:
        resultados["causa_retraso"] = "causa desconocida"

    return resultados

# Ejecutar diagnóstico
resultado_diagnostico = diagnostico(hechos)

# Mostrar resultados
print("Diagnóstico de Causas en Transporte:")
for clave, valor in resultado_diagnostico.items():
    print(f"{clave}: {valor}")
