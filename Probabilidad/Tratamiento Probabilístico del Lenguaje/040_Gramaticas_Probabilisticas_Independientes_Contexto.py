## Jonathan Beltran Neri
# Tema: Gramáticas Probabilísticas Independientes del Contexto (PCFG)

# Una Gramática Probabilística Independiente del Contexto (PCFG) asigna probabilidades
# a las reglas de producción de una gramática.
# El objetivo es modelar cómo se generan frases en un lenguaje de forma probabilística.

# Simularemos una gramática muy simple para frases de transporte.

# Definimos las reglas y sus probabilidades
gramatica = {
    "S": [("NP VP", 1.0)],
    "NP": [("el tren", 0.5), ("el camión", 0.3), ("caminando", 0.2)],
    "VP": [("llegó tarde", 0.4), ("salió puntual", 0.6)]
}

# Función para expandir una regla
import random

def expandir(simbolo):
    if simbolo not in gramatica:
        return simbolo
    producciones = gramatica[simbolo]
    opciones, probabilidades = zip(*producciones)
    seleccion = random.choices(opciones, weights=probabilidades)[0]
    return " ".join(expandir(p) for p in seleccion.split())

# Generamos varias frases
print("Generación de frases usando una PCFG:")
for _ in range(5):
    frase = expandir("S")
    print(f"- {frase}")
