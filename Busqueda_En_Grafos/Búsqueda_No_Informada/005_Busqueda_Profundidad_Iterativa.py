## Jonathan Beltran Neri
## 01/04/2025

# BÚSQUEDA EN PROFUNDIDAD ITERATIVA (Iterative Deepening Search)
# Combina la profundidad limitada con una estrategia de búsqueda progresiva.

def busqueda_profundidad_limitada(grafo, nodo, objetivo, limite):
    if nodo == objetivo:
        return [nodo]
    if limite <= 0:
        return None
    for vecino in grafo.get(nodo, []):
        resultado = busqueda_profundidad_limitada(grafo, vecino, objetivo, limite - 1)
        if resultado:
            return [nodo] + resultado
    return None

def busqueda_profundidad_iterativa(grafo, inicio, objetivo, limite_max):
    for limite in range(limite_max + 1):
        resultado = busqueda_profundidad_limitada(grafo, inicio, objetivo, limite)
        if resultado:
            return resultado  # Devuelve el primer resultado encontrado en alguna profundidad
    return None

# Ejemplo de grafo
grafo = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Ejecuta la búsqueda desde A hasta F con un límite máximo de profundidad de 5
camino = busqueda_profundidad_iterativa(grafo, 'A', 'F', 5)
print("Camino:", camino)
