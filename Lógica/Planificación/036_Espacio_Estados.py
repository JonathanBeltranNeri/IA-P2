## Jonathan Beltran Neri
# Algoritmo: Espacio de Estados

# Estructura del grafo utilizado:
#
#         Caminar
#         /     \
#     Camión   Tren
#       |        |
#     Taxi     Avión
#       \       /
#       Destino

# Este algoritmo representa un espacio de estados donde cada nodo es un estado
# alcanzable desde otro mediante acciones. Se busca llegar desde un estado inicial
# hasta un estado objetivo usando búsqueda.

# Grafo de estados
grafo = {
    'Caminar': ['Camión', 'Tren'],
    'Camión': ['Taxi'],
    'Tren': ['Avión'],
    'Taxi': ['Destino'],
    'Avión': ['Destino'],
    'Destino': []
}

# Búsqueda en profundidad para simular recorrido por el espacio de estados
def buscar_camino(estado_inicial, objetivo, grafo, camino=[]):
    camino = camino + [estado_inicial]
    if estado_inicial == objetivo:
        return camino
    if estado_inicial not in grafo:
        return None
    for vecino in grafo[estado_inicial]:
        if vecino not in camino:
            nuevo_camino = buscar_camino(vecino, objetivo, grafo, camino)
            if nuevo_camino:
                return nuevo_camino
    return None

# Ejecutar búsqueda
camino = buscar_camino('Caminar', 'Destino', grafo)

# Mostrar resultado
print("Espacio de Estados:")
if camino:
    print(" → ".join(camino))
else:
    print("No se encontró un camino al destino.")
