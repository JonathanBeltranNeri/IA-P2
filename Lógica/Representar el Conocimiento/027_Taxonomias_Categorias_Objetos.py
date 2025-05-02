## Jonathan Beltran Neri
# Tema: Taxonomías – Categorías y Objetos

# En inteligencia artificial, una taxonomía es una jerarquía estructurada
# que permite clasificar conceptos y objetos desde los más generales hasta los más específicos.

# Esta taxonomía está basada en el dominio del transporte.

# Se define como una estructura jerárquica usando diccionarios anidados.
taxonomia = {
    "Transporte": {
        "Terrestre": {
            "Motorizado": ["Tren", "Camión", "Automóvil"],
            "No Motorizado": ["Bicicleta", "Caminar"]
        },
        "Aéreo": ["Avión", "Helicóptero"]
    }
}

# Función recursiva para imprimir visualmente la jerarquía
# Cada nivel de anidación se representa con indentación.
def imprimir_taxonomia(nodo, nivel=0):
    if isinstance(nodo, dict):
        for categoria, subnodo in nodo.items():
            print("  " * nivel + f"- {categoria}")
            imprimir_taxonomia(subnodo, nivel + 1)
    elif isinstance(nodo, list):
        for item in nodo:
            print("  " * nivel + f"- {item}")

# Mostrar la taxonomía completa
print("Taxonomía del Transporte:\n")
imprimir_taxonomia(taxonomia)

