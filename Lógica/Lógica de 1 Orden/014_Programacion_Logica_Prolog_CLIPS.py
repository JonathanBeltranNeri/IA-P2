## Jonathan Beltran Neri
# Tema: Programación Lógica - Prolog y CLIPS

# La programación lógica permite definir hechos y reglas,
# y realizar consultas automáticas para deducir información.

# Aquí simulamos una pequeña base de hechos y reglas
# como si estuviéramos en un entorno tipo Prolog o CLIPS.

# Hechos
hechos = [
    ("medio_transporte", "tren"),
    ("medio_transporte", "camión"),
    ("viaja", "persona1", "tren"),
    ("viaja", "persona2", "camión")
]

# Reglas simuladas
def regla_rapido(medio):
    return medio == "tren"

def regla_barato(medio):
    return medio == "camión"

# Consultas simuladas
def consulta(medio):
    if regla_rapido(medio):
        return "es rápido"
    elif regla_barato(medio):
        return "es barato"
    else:
        return "características desconocidas"

# Ejecutar consultas sobre los medios
print("Consultas Simuladas en Programación Lógica:")
for hecho in hechos:
    if hecho[0] == "medio_transporte":
        medio = hecho[1]
        resultado = consulta(medio)
        print(f"{medio.capitalize()}: {resultado}")
