## Jonathan Beltran Neri
# Tema: Espacio de Versiones (Version Space)

# Este algoritmo representa el proceso de generalización y especialización de hipótesis
# utilizando el enfoque del espacio de versiones de Mitchell. Se inicia con una hipótesis
# más general (G) y una más específica (S), ajustándolas en función de los ejemplos.

# Se utiliza un conjunto de ejemplos con atributos sobre el tipo de transporte y su destino deseado.

# Cada hipótesis es una lista de atributos, y los valores posibles son:
# - Valor específico (como "Camión", "Querétaro")
# - El comodín "?" para representar cualquier valor

# Función para verificar si una hipótesis coincide con un ejemplo

def coincide(hipotesis, ejemplo):
    return all(h == e or h == '?' for h, e in zip(hipotesis, ejemplo))

# Función para generalizar una hipótesis específica con un ejemplo positivo

def generalizar(s, ejemplo):
    return [si if si == ei else '?' for si, ei in zip(s, ejemplo)]

# Función para especializar una hipótesis general con un ejemplo negativo

def especializar(g, ejemplo):
    especializaciones = []
    for i in range(len(g)):
        if g[i] == '?':
            valores = set(e[i] for e in ejemplos if e != ejemplo)
            for val in valores:
                if val != ejemplo[i]:
                    nueva = g[:]
                    nueva[i] = val
                    especializaciones.append(nueva)
    return especializaciones

# Conjunto de ejemplos: ([Tipo de transporte, Destino], Clase)
ejemplos = [
    (("Camión", "Querétaro"), "Sí"),
    (("Tren", "Querétaro"), "Sí"),
    (("Caminar", "Puebla"), "No"),
    (("Camión", "Veracruz"), "Sí"),
    (("Caminar", "San Luis"), "No")
]

# Inicialización
S = ["Camión", "Querétaro"]  # Hipótesis específica
G = [["?", "?"]]             # Conjunto de hipótesis generales

for ejemplo, clase in ejemplos:
    if clase == "Sí":
        if not coincide(S, ejemplo):
            S = generalizar(S, ejemplo)
        G = [g for g in G if coincide(g, ejemplo)]
    else:
        Gnueva = []
        for g in G:
            if coincide(g, ejemplo):
                Gnueva.extend(especializar(g, ejemplo))
            else:
                Gnueva.append(g)
        G = Gnueva

# Resultados finales
print("Hipótesis específica (S):", S)
print("Hipótesis generales (G):", G)
