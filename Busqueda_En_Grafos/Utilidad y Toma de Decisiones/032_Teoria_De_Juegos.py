## Jonathan Beltran Neri
# Algoritmo: Teoría de Juegos - Equilibrios y Mecanismos

# Este ejemplo representa un juego entre dos jugadores con estrategias personalizadas.
# Cada jugador elige una estrategia (X o Y para A, P o Q para B) y recibe un pago
# dependiendo de la combinación elegida. Se evalúa si existe un equilibrio de Nash puro.

# Matriz de pagos:
#
#               B
#           P       Q
#        +-------+-------+
#     X  | 4, 2  | 1, 3  |
#  A     +-------+-------+
#     Y  | 3, 4  | 2, 1  |
#        +-------+-------+
#
# Primer valor: ganancia de A
# Segundo valor: ganancia de B

# Definimos la matriz de pagos como un diccionario de estrategias
matriz_pagos = {
    ('X', 'P'): (4, 2),
    ('X', 'Q'): (1, 3),
    ('Y', 'P'): (3, 4),
    ('Y', 'Q'): (2, 1)
}

# Estrategias posibles para ambos jugadores
estrategias_a = ['X', 'Y']
estrategias_b = ['P', 'Q']

# Buscar equilibrio de Nash puro
def buscar_equilibrio_nash():
    print("Evaluación de estrategias en matriz de pagos:\n")

    for a in estrategias_a:
        for b in estrategias_b:
            pago_a, pago_b = matriz_pagos[(a, b)]

            # ¿A tiene incentivo a cambiar?
            cambiar_a = any(
                matriz_pagos[(a_alt, b)][0] > pago_a
                for a_alt in estrategias_a if a_alt != a
            )

            # ¿B tiene incentivo a cambiar?
            cambiar_b = any(
                matriz_pagos[(a, b_alt)][1] > pago_b
                for b_alt in estrategias_b if b_alt != b
            )

            print(f"  A = {a}, B = {b} → Pagos: A = {pago_a}, B = {pago_b}")
            if not cambiar_a and not cambiar_b:
                print(f"\nEquilibrio de Nash encontrado en estrategias: A = '{a}', B = '{b}'")
                print(f"  Pagos: A = {pago_a}, B = {pago_b}")
                return

    print("\nNo se encontró equilibrio puro de Nash en este juego.")

# Ejecutar análisis
print("Teoría de Juegos - Evaluación de equilibrio de Nash\n")
buscar_equilibrio_nash()
