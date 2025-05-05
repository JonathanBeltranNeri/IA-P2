## Jonathan Beltran Neri
# Tema: Inducción Gramatical

# Este código simula un proceso básico de inducción gramatical:
# A partir de una serie de frases, intenta identificar patrones comunes en su estructura.

# Frases de entrenamiento
frases = [
    "El tren llega",
    "El camión parte",
    "La gente camina",
    "El tren parte",
    "La gente llega"
]

# Extraer estructuras gramaticales simples (sujeto + verbo)
def inducir_gramatica(frases):
    estructuras = set()
    for frase in frases:
        palabras = frase.lower().split()
        if len(palabras) == 3:
            sujeto = palabras[0] + " " + palabras[1]
            verbo = palabras[2]
            estructuras.add(("Sujeto:", sujeto, "Verbo:", verbo))
    return estructuras

# Ejecutar inducción gramatical
patrones = inducir_gramatica(frases)

# Mostrar patrones identificados
print("Patrones gramaticales inducidos:")
for patron in patrones:
    print(patron)
