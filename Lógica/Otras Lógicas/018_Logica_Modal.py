## Jonathan Beltran Neri
# Tema: Lógica Modal

# La lógica modal introduce operadores para expresar posibilidades y necesidades,
# usando conceptos como "es posible que" (◇) y "es necesario que" (□).

# Simularemos un ejemplo sencillo en el contexto de transporte.

# Base de hechos
hechos = {
    "tren_disponible": True,
    "camion_disponible": False
}

# Operadores modales
def necesario(condicion):
    """Expresa que la condición es necesariamente verdadera."""
    return condicion

def posible(condicion):
    """Expresa que la condición puede ser verdadera (no necesariamente)."""
    return condicion or False  # En este caso simple, tomamos lo que se sabe

# Aplicación de operadores
es_necesario_tren = necesario(hechos["tren_disponible"])
es_posible_camion = posible(hechos["camion_disponible"])

# Mostrar resultados
print("Lógica Modal aplicada al Transporte:")
print(f"¿Es necesario que haya tren disponible? {'Sí' if es_necesario_tren else 'No'}")
print(f"¿Es posible que haya camión disponible? {'Sí' if es_posible_camion else 'No'}")
