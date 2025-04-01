## Jonathan Beltran Neri
## 01/04/2025
# Algoritmo de Búsqueda de Costo Uniforme
import heapq  # Importa heapq para manejar la cola de prioridad

def busqueda_costo_uniforme(grafo, inicio, objetivo):
    # La cola contiene tuplas (costo_acumulado, camino_actual)
    cola = [(0, [inicio])]
    visitados = set()  # Conjunto para evitar repetir nodos

    while cola:
        costo, camino = heapq.heappop(cola)  # Extrae el camino con menor costo
        nodo = camino[-1]  # Último nodo del camino actual

        if nodo == objetivo:
            return camino, costo  # Devuelve el camino y su costo total

        if nodo not in visitados:
            visitados.add(nodo)
            for vecino, peso in grafo.get(nodo, []):  # Vecinos con sus pesos
                nuevo_costo = costo + peso
                nueva_ruta = camino + [vecino]
                heapq.heappush(cola, (nuevo_costo, nueva_ruta))  # Agrega el nuevo camino
    return None  # Si no se encuentra solución

# Ejemplo de grafo ponderado
grafo = {
    'A': [('B', 1), ('C', 5)],
    'B': [('D', 3), ('E', 1)],
    'C': [('F', 2)],
    'D': [],
    'E': [('F', 1)],
    'F': []
}

# Ejecuta la búsqueda desde A hasta F
camino, costo = busqueda_costo_uniforme(grafo, 'A', 'F')
print("Camino:", camino)
print("Costo total:", costo)
