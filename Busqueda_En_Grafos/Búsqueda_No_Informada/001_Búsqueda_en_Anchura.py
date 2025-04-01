from collections import deque  # Importa una cola doble para manejar los caminos a explorar

# Definición de la función de búsqueda en anchura
def busqueda_anchura(grafo, inicio, objetivo):
    visitados = set()                 # Conjunto para guardar nodos ya visitados
    cola = deque([[inicio]])         # Cola con caminos; inicia con una lista que contiene el nodo inicial

    while cola:                      # Mientras haya caminos por explorar
        camino = cola.popleft()      # Toma el primer camino (FIFO)
        nodo = camino[-1]            # El nodo actual es el último del camino

        if nodo == objetivo:         # Si es el nodo objetivo, retorna el camino completo
            return camino

        if nodo not in visitados:    # Si el nodo aún no se ha visitado
            visitados.add(nodo)      # Se marca como visitado
            for vecino in grafo.get(nodo, []):  # Recorre todos los vecinos del nodo actual
                nueva_ruta = list(camino)       # Copia el camino actual
                nueva_ruta.append(vecino)       # Agrega el vecino al nuevo camino
                cola.append(nueva_ruta)         # Agrega el nuevo camino a la cola
    return None  # Si no se encuentra el objetivo, retorna None

# Ejemplo de uso
grafo = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

print(busqueda_anchura(grafo, 'A', 'F'))  # Imprime el camino desde 'A' hasta 'F' si existe
