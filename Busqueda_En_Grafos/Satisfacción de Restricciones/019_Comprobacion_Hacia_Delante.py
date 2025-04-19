## Jonathan Beltran Neri
# Algoritmo: Comprobación Hacia Delante (Forward Checking)

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
# Este algoritmo intenta asignar valores a variables asegurándose en cada paso
# que los dominios de los vecinos se mantengan consistentes, reduciendo las posibilidades
# antes de cometer errores más adelante.

# Grafo bidireccional que representa restricciones entre variables
grafo = {
    'M': ['N', 'O'],
    'N': ['M', 'P', 'Q'],
    'O': ['M', 'R'],
    'P': ['N', 'T'],
    'Q': ['N', 'T'],
    'R': ['O', 'S'],
    'S': ['R', 'T'],
    'T': ['P', 'Q', 'S']
}

# Valores posibles para cada variable
valores = ['Rojo', 'Verde', 'Azul']

# Algoritmo de Comprobación Hacia Delante
def comprobacion_hacia_adelante(asignacion, dominios, grafo, nodo_actual):
    if nodo_actual == len(grafo):
        return asignacion  # Todas las variables asignadas exitosamente

    nodos = list(grafo.keys())
    nodo = nodos[nodo_actual]

    for valor in dominios[nodo]:
        # Verificar si el valor es válido respecto a los vecinos asignados
        valido = True
        for vecino in grafo[nodo]:
            if asignacion.get(vecino) == valor:
                valido = False
                break

        if valido:
            asignacion[nodo] = valor
            # Copiar dominios para evitar modificar los originales
            nuevos_dominios = {v: list(d) for v, d in dominios.items()}
            # Eliminar este valor del dominio de los vecinos no asignados
            for vecino in grafo[nodo]:
                if vecino not in asignacion and valor in nuevos_dominios[vecino]:
                    nuevos_dominios[vecino].remove(valor)
                    if not nuevos_dominios[vecino]:  # Si un dominio queda vacío, se descarta este camino
                        break
            else:
                resultado = comprobacion_hacia_adelante(asignacion.copy(), nuevos_dominios, grafo, nodo_actual + 1)
                if resultado:
                    return resultado

    return None  # No se pudo asignar consistentemente

# Crear dominios iniciales
dominios_iniciales = {nodo: list(valores) for nodo in grafo}

# Ejecutar algoritmo
solucion = comprobacion_hacia_adelante({}, dominios_iniciales, grafo, 0)

# Mostrar resultado
print("Comprobación Hacia Delante (Forward Checking)")
if solucion:
    print("Solución encontrada:")
    for nodo, valor in solucion.items():
        print(f"  {nodo}: {valor}")
else:
    print("No se encontró una solución válida.")
