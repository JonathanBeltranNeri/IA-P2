## Jonathan Beltran Neri
# Tema: Listas de Decisión - K-DL y K-DT

# Este código simula una lista de decisiones para elegir el transporte ideal.
# Usamos condiciones encadenadas (tipo if-elif) para decidir qué medio utilizar según el tiempo, distancia y presupuesto.

# Estructura del grafo utilizado:
#
#         Caminar
#         /     \
#     Camión   Tren
#       |        |
#   Bicicleta   Avión
#       \       /
#       Destino

def elegir_transporte(distancia_km, tiempo_disp_min, presupuesto):
    if distancia_km <= 1 and tiempo_disp_min >= 30:
        return "Caminar"
    elif distancia_km <= 5 and presupuesto < 20:
        return "Bicicleta"
    elif distancia_km <= 10 and presupuesto < 50:
        return "Camión"
    elif distancia_km > 10 and presupuesto >= 100:
        return "Tren"
    elif distancia_km > 20 and presupuesto >= 300:
        return "Avión"
    else:
        return "No hay transporte adecuado"

# Pruebas de ejemplo
casos = [
    {"distancia": 0.5, "tiempo": 40, "presupuesto": 10},
    {"distancia": 3, "tiempo": 25, "presupuesto": 15},
    {"distancia": 8, "tiempo": 15, "presupuesto": 40},
    {"distancia": 15, "tiempo": 20, "presupuesto": 120},
    {"distancia": 30, "tiempo": 60, "presupuesto": 400}
]

for caso in casos:
    transporte = elegir_transporte(caso["distancia"], caso["tiempo"], caso["presupuesto"])
    print(f"Distancia: {caso['distancia']} km, Tiempo: {caso['tiempo']} min, Presupuesto: ${caso['presupuesto']} → Transporte: {transporte}")
