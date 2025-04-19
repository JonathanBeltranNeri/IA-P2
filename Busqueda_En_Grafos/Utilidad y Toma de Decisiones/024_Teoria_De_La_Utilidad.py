## Jonathan Beltran Neri
# Algoritmo: Teoría de la Utilidad: Función de Utilidad

# Estructura del grafo utilizado:
#
#         M
#        / \
#       N   O
#      / \    \
#     P   Q    R
#      \  |     \
#       T T      S
#                |
#                T
#
# Este ejemplo no usa el grafo directamente, sino que aplica el concepto de utilidad,
# que representa la satisfacción o valor que un agente recibe al tomar una decisión.

# Opciones de decisión con sus utilidades esperadas
opciones = {
    'Comprar barato': 0.6,       # Bajo costo, bajo beneficio
    'Comprar seguro': 0.8,       # Precio razonable, beneficio seguro
    'Invertir agresivo': 0.4,    # Alta ganancia potencial, alto riesgo
    'No hacer nada': 0.2         # Sin riesgo, sin beneficio
}

# Elegir la opción con mayor utilidad
def elegir_con_mayor_utilidad(opciones):
    mejor_opcion = max(opciones, key=opciones.get)
    return mejor_opcion, opciones[mejor_opcion]

# Mostrar resultados
print("Teoría de la Utilidad: Función de Utilidad")
print("Opciones y sus utilidades esperadas:")
for opcion, utilidad in opciones.items():
    print(f"  {opcion}: {utilidad}")

mejor, valor = elegir_con_mayor_utilidad(opciones)
print(f"\nMejor decisión según la utilidad: '{mejor}' con utilidad {valor}")
