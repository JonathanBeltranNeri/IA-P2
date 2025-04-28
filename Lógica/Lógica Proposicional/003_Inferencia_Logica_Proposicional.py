## Jonathan Beltran Neri
# Tema: Inferencia Lógica Proposicional

# La inferencia lógica permite deducir nuevos hechos a partir de otros hechos conocidos
# usando reglas de lógica formal.

# En este ejemplo, basándonos en hechos sobre transporte, inferiremos nuevas conclusiones.

# Base de conocimiento inicial
base_conocimiento = {
    'tren_llega': True,
    'camion_sale': False,
    'caminando_llegamos': None,
    'esperamos_otro_transporte': None
}

# Reglas de inferencia
def inferir(base):
    # Si el tren llega, no necesitamos esperar otro transporte
    if base['tren_llega']:
        base['esperamos_otro_transporte'] = False
    # Si el camión no sale y el tren no llega, caminamos
    if not base['tren_llega'] and not base['camion_sale']:
        base['caminando_llegamos'] = True
    else:
        base['caminando_llegamos'] = False
    return base

# Aplicamos inferencia
base_actualizada = inferir(base_conocimiento)

# Mostrar resultados
print("Inferencia Lógica Proposicional:")
for hecho, valor in base_actualizada.items():
    print(f"{hecho}: {valor}")
