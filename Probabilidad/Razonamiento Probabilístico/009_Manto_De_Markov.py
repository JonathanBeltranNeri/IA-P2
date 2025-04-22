## Jonathan Beltran Neri
# Tema: Manto de Markov (Markov Blanket)

# El manto de Markov de un nodo en una red bayesiana es el conjunto mínimo de nodos
# que, al ser conocidos, hacen que el nodo sea independiente del resto de la red.

# El Manto de Markov de un nodo incluye:
#  - Sus padres
#  - Sus hijos
#  - Los otros padres de sus hijos

# Grafo utilizado como Red Bayesiana:
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

# Definimos estructura de la red bayesiana
red_bayesiana = {
    'M': [],
    'N': ['M'],
    'O': ['M'],
    'P': ['N'],
    'Q': ['N'],
    'R': ['O'],
    'S': ['R'],
    'T': ['P', 'Q', 'S']
}

# Función para obtener el manto de Markov de un nodo
def manto_de_markov(nodo, red):
    padres = set(red[nodo])
    hijos = {hijos for h, ps in red.items() if nodo in ps}
    padres_de_hijos = {
        p for h in hijos for p in red[h] if p != nodo
    }
    return padres.union(hijos).union(padres_de_hijos)

# Nodo a analizar
nodo_objetivo = 'T'

# Calcular manto de Markov
manto = manto_de_markov(nodo_objetivo, red_bayesiana)

# Mostrar resultados
print(f"Manto de Markov del nodo '{nodo_objetivo}':")
print("  " + ", ".join(sorted(manto)))
