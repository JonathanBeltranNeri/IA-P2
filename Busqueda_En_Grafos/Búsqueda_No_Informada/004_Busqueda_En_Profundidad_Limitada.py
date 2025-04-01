## Jonathan Beltran Neri
## 01/04/2025

# BÚSQUEDA EN PROFUNDIDAD LIMITADA (Depth-Limited Search)
# Variante de DFS que impone un límite máximo de profundidad para evitar exploraciones infinitas.

def busqueda_profundidad_limitada(grafo, nodo, objetivo, limite):
    if nodo == objetivo:
        return [nodo]  # Se encontró el objetivo, devuelve el camino

    if limite <= 0:
        return None  # Se alcanzó el límite de profundidad sin éxito

    for vecino in grafo.get(nodo, []):  # Recorre los vecinos del nodo actual
        resultado = busqueda_profundidad_limitada(grafo, vecino, objetivo, limite - 1)
        if resultado:
            return [nodo] + resultado  # Si se encontró solución, la devuelve concatenando
    return None  # No se encontró el objetivo dentro del límite

# Ejemplo de grafo
grafo = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Ejecuta la búsqueda desde A hasta F con límite de profundidad = 3
camino = busqueda_profundidad_limitada(grafo, 'A', 'F', 3)
print("Camino:", camino)
