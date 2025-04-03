## Jonathan Beltran Neri
## 03/04/2025

from collections import deque

def busqueda_bidireccional(grafo, inicio, fin):
    if inicio == fin:
        return [inicio]

    # Caminos que vamos explorando desde cada lado
    desde_inicio = deque([[inicio]])
    desde_fin = deque([[fin]])

    # Lo que ya hemos visitado
    visitados_inicio = {inicio: [inicio]}
    visitados_fin = {fin: [fin]}

    while desde_inicio and desde_fin:
        # Expandimos desde el inicio
        camino1 = desde_inicio.popleft()
        nodo1 = camino1[-1]

        if nodo1 in visitados_fin:
            camino2 = visitados_fin[nodo1]
            return camino1 + camino2[-2::-1]

        for vecino in grafo.get(nodo1, []):
            if vecino not in visitados_inicio:
                visitados_inicio[vecino] = camino1 + [vecino]
                desde_inicio.append(camino1 + [vecino])

        # Expandimos desde el fin
        camino2 = desde_fin.popleft()
        nodo2 = camino2[-1]

        if nodo2 in visitados_inicio:
            camino1 = visitados_inicio[nodo2]
            return camino1 + camino2[-2::-1]

        for vecino in grafo.get(nodo2, []):
            if vecino not in visitados_fin:
                visitados_fin[vecino] = camino2 + [vecino]
                desde_fin.append(camino2 + [vecino])

    return None  # No hay forma de llegar

# Grafo básico
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'E'],
    'D': ['B'],
    'E': ['C', 'F'],
    'F': ['E']
}

camino = busqueda_bidireccional(grafo, 'A', 'F')
print("Camino encontrado:", camino)
