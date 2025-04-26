## Jonathan Beltran Neri
# Tema: Gramáticas Probabilísticas Lexicalizadas

# Las Gramáticas Probabilísticas Lexicalizadas asocian cada regla de producción
# no solo con una probabilidad, sino también con información léxica (palabras específicas).

# Ejemplo sencillo adaptado al tema de transporte.

# Definimos reglas lexicalizadas (cada producción está ligada a una palabra raíz)
gramatica_lexicalizada = {
    "S": [("NP[tren] VP[llegar]", 0.5), ("NP[camión] VP[salir]", 0.5)],
    "NP[tren]": [("el tren", 1.0)],
    "NP[camión]": [("el camión", 1.0)],
    "VP[llegar]": [("llegó tarde", 0.7), ("llegó temprano", 0.3)],
    "VP[salir]": [("salió puntual", 0.8), ("salió tarde", 0.2)]
}

import random

# Función para expandir una regla lexicalizada
def expandir_lexicalizado(simbolo):
    if simbolo not in gramatica_lexicalizada:
        return simbolo
    producciones = gramatica_lexicalizada[simbolo]
    opciones, probabilidades = zip(*producciones)
    seleccion = random.choices(opciones, weights=probabilidades)[0]
    partes = seleccion.split()
    return " ".join(expandir_lexicalizado(p) for p in partes)

# Generamos varias frases
print("Generación de frases usando una Gramática Probabilística Lexicalizada:")
for _ in range(5):
    frase = expandir_lexicalizado("S")
    print(f"- {frase}")
