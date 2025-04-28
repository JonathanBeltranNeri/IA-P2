## Jonathan Beltran Neri
# Tema: Backtracking

# El backtracking es una técnica de búsqueda que explora todas las posibles soluciones
# volviendo atrás cuando una opción no lleva a una solución válida.

# Ejemplo adaptado: buscar una ruta correcta usando transporte.

# Grafo simple de transporte
grafo = {
    "inicio": ["tren", "camion"],
    "tren": ["estacion_tren"],
    "camion": ["terminal_camion"],
    "estacion_tren": ["destino"],
    "terminal_camion": ["destino"],
    "destino": []
}

# Función de búsqueda por backtracking
def buscar_camino(estado_actual, objetivo, camino=[]):
    camino = camino + [estado_actual]
    if estado_actual == objetivo:
        return camino
    if estado_actual not in grafo:
        return None
    for siguiente in grafo[estado_actual]:
        if siguiente not in camino:
            nuevo_camino = buscar_camino(siguiente, objetivo, camino)
            if nuevo_camino:
                return nuevo_camino
    return None

# Buscamos un camino de "inicio" a "destino"
camino_encontrado = buscar_camino("inicio", "destino")

# Mostrar resultado
print("Camino encontrado usando Backtracking:")
print(camino_encontrado if camino_encontrado else "No se encontró un camino.")
