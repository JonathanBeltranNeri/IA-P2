## Jonathan Beltran Neri
## 01/04/2025
# Algoritmo de Búsqueda en Profundidad

# Este algoritmo explora un camino lo más profundo posible antes de retroceder y probar otros.

def busqueda_profundidad(grafo, inicio, objetivo, visitados=None, camino=None):
    if visitados is None:
        visitados = set()  # Conjunto para registrar nodos visitados
    if camino is None:
        camino = [inicio]  # Lista para guardar el camino actual

    visitados.add(inicio)  # Marca el nodo como visitado

    if inicio == objetivo:
        return camino  # Si se llegó al objetivo, devuelve el camino

    for vecino in grafo.get(inicio, []):  # Recorre vecinos del nodo actual
        if vecino not in visitados:  # Solo visita si no ha sido visitado
            resultado = busqueda_profundidad(grafo, vecino, objetivo, visitados, camino + [vecino])
            if resultado:
                return resultado  # Si encuentra una solución, la retorna
    return None  # Si no encuentra el objetivo desde este camino

# Ejemplo de grafo
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Ejecuta la búsqueda desde A hasta F
resultado = busqueda_profundidad(grafo, 'A', 'F')
print("Camino:", resultado)
