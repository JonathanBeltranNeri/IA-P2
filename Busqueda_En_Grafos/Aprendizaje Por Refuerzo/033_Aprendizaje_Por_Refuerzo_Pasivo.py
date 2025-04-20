## Jonathan Beltran Neri
# Algoritmo: Aprendizaje por Refuerzo Pasivo

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
# Este algoritmo aprende el valor de los estados al seguir una política fija,
# sin intentar mejorarla, utilizando el promedio de recompensas observadas.

import random

# Definición del grafo con recompensas
grafo = {
    'M': [('N', -1), ('O', -1)],
    'N': [('P', -1), ('Q', -1)],
    'O': [('R', -1)],
    'P': [('T', 10)],
    'Q': [('T', 10)],
    'R': [('S', -1)],
    'S': [('T', 10)],
    'T': []
}

# Política fija que el agente sigue
politica = {
    'M': 'N',
    'N': 'P',
    'O': 'R',
    'P': 'T',
    'Q': 'T',
    'R': 'S',
    'S': 'T',
    'T': None  # Estado terminal
}

# Inicializar valores y visitas
valores = {estado: 0.0 for estado in grafo}
visitas = {estado: 0 for estado in grafo}

# Simular episodios donde el agente sigue la política fija
def simular_episodios(n_episodios):
    for _ in range(n_episodios):
        estado = 'M'
        total_recompensa = 0
        descuento = 1.0
        trayectoria = []

        # Generar una trayectoria completa
        while estado and politica[estado]:
            siguiente = politica[estado]
            recompensa = next(r for s, r in grafo[estado] if s == siguiente)

            trayectoria.append((estado, recompensa))
            estado = siguiente

        # Aplicar retorno descontado a cada estado
        retorno = 0
        for estado, recompensa in reversed(trayectoria):
            retorno = recompensa + 0.9 * retorno
            visitas[estado] += 1
            valores[estado] += (retorno - valores[estado]) / visitas[estado]

# Ejecutar simulación
print("Aprendizaje por Refuerzo Pasivo - Política fija y evaluación de estados\n")
simular_episodios(n_episodios=1000)

# Mostrar resultados
for estado in sorted(valores.keys()):
    print(f"  Estado '{estado}': Valor estimado = {valores[estado]:.2f}")
