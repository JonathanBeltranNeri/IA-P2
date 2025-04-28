## Jonathan Beltran Neri
# Tema: Base de Conocimiento

# Una base de conocimiento (KB) contiene hechos y reglas lógicas que describen
# lo que sabemos sobre un dominio específico.

# En este ejemplo, simulamos una base de conocimiento relacionada con transporte:
# - Sabemos si el tren llega
# - Sabemos si el camión sale
# - Sabemos si caminando llegamos

# La inferencia es muy simple en este ejemplo: si el tren no llega, pero el camión sale, entonces caminamos.

# Base de conocimiento inicial (hechos)
base_conocimiento = {
    'tren_llega': False,
    'camion_sale': True,
    'caminando_llegamos': None  # Desconocido inicialmente
}

# Reglas de inferencia
def inferir(base):
    if not base['tren_llega'] and base['camion_sale']:
        base['caminando_llegamos'] = True
    else:
        base['caminando_llegamos'] = False
    return base

# Aplicamos la inferencia
base_actualizada = inferir(base_conocimiento)

# Mostramos la base de conocimiento resultante
print("Base de Conocimiento Actualizada:")
for hecho, valor in base_actualizada.items():
    print(f"{hecho}: {valor}")
