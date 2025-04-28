## Jonathan Beltran Neri
# Tema: Encadenamiento Hacia Delante y Hacia Atrás - Lógica de 1 Orden

# El encadenamiento en lógica de primer orden permite razonar aplicando reglas
# que contienen variables, y no solo hechos concretos.

# Simularemos un ejemplo sencillo basado en transporte.

# Base de conocimiento (hechos y reglas)
hechos = [
    ("en", "persona1", "estacion"),
    ("cerca", "estacion", "parada_camion")
]

reglas = [
    {"antecedentes": [("en", "X", "estacion"), ("cerca", "estacion", "parada_camion")],
     "consecuente": ("en", "X", "parada_camion")}
]

# Función de encadenamiento hacia delante
def encadenamiento_hacia_delante(hechos, reglas):
    nuevos = hechos.copy()
    while True:
        aplicado = False
        for regla in reglas:
            mapeo = {}
            posibles = True
            for ant in regla["antecedentes"]:
                encontrado = False
                for hecho in nuevos:
                    if ant[0] == hecho[0]:
                        if ant[1].startswith("X") or ant[1] == hecho[1]:
                            if ant[2] == hecho[2]:
                                mapeo[ant[1]] = hecho[1]
                                encontrado = True
                                break
                if not encontrado:
                    posibles = False
                    break
            if posibles:
                # Aplicamos sustitución
                nueva = (
                    regla["consecuente"][0],
                    mapeo.get(regla["consecuente"][1], regla["consecuente"][1]),
                    regla["consecuente"][2]
                )
                if nueva not in nuevos:
                    nuevos.append(nueva)
                    aplicado = True
        if not aplicado:
            break
    return nuevos

# Ejecutar el encadenamiento
hechos_resultantes = encadenamiento_hacia_delante(hechos, reglas)

# Mostrar resultados
print("Hechos después de Encadenamiento Hacia Delante:")
for hecho in hechos_resultantes:
    print(hecho)
