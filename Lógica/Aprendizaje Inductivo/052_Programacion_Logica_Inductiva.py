## Jonathan Beltran Neri
# Tema: Programación Lógica Inductiva: FOIL

# En este ejemplo implementamos una versión simplificada del algoritmo FOIL,
# el cual aprende reglas lógicas a partir de ejemplos positivos y negativos.
# FOIL se usa para generar hipótesis expresadas como reglas lógicas de implicación.

# Definimos ejemplos positivos y negativos de un concepto (por ejemplo, "viajar_rapido")
positivos = [
    {"transporte": "tren", "rapido": True},
    {"transporte": "avion", "rapido": True}
]

negativos = [
    {"transporte": "caminar", "rapido": False},
    {"transporte": "camion", "rapido": False}
]

# FOIL simplificado: busca una regla que cubra todos los positivos sin cubrir negativos
def aprender_regla(positivos, negativos):
    atributos = positivos[0].keys()
    reglas = []

    for atributo in atributos:
        valores = set(ej[atributo] for ej in positivos)
        for valor in valores:
            regla = lambda x, a=atributo, v=valor: x[a] == v
            cubre_positivos = all(regla(ej) for ej in positivos)
            cubre_negativos = any(regla(ej) for ej in negativos)
            if cubre_positivos and not cubre_negativos:
                reglas.append((atributo, valor))

    return reglas

# Aplicamos el algoritmo FOIL simplificado
reglas_aprendidas = aprender_regla(positivos, negativos)

# Mostramos las reglas
print("Reglas aprendidas para el concepto 'viajar_rapido':")
for atributo, valor in reglas_aprendidas:
    print(f"Si {atributo} == '{valor}', entonces viajar_rapido = True")
