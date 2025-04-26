## Jonathan Beltran Neri
# Tema: Traducción Automática Estadística (Statistical Machine Translation - SMT)

# La traducción automática estadística se basa en modelos probabilísticos
# que predicen la traducción más probable de una oración de un idioma a otro.

# Simulamos un modelo muy simple de traducción de frases cortas.

# Diccionario bilingüe con probabilidades (simuladas)
modelo_traduccion = {
    "el tren": {"the train": 0.9},
    "el camión": {"the bus": 0.85},
    "caminando": {"walking": 0.95},
    "llegó tarde": {"arrived late": 0.8},
    "salió puntual": {"departed on time": 0.9}
}

# Frases de entrada en español
frases = [
    "el tren llegó tarde",
    "el camión salió puntual",
    "caminando llegó tarde"
]

# Función para traducir frase palabra por palabra
def traducir(frase, modelo):
    palabras = frase.split()
    traduccion = []
    i = 0
    while i < len(palabras):
        # Intentar combinar 2 palabras
        if i+1 < len(palabras):
            combinacion = palabras[i] + " " + palabras[i+1]
            if combinacion in modelo:
                mejor_traduccion = max(modelo[combinacion], key=modelo[combinacion].get)
                traduccion.append(mejor_traduccion)
                i += 2
                continue
        # Si no, traducir palabra sola (si existe)
        if palabras[i] in modelo:
            mejor_traduccion = max(modelo[palabras[i]], key=modelo[palabras[i]].get)
            traduccion.append(mejor_traduccion)
        else:
            traduccion.append(palabras[i])  # Dejar palabra tal cual si no se conoce
        i += 1
    return " ".join(traduccion)

# Proceso de traducción
print("Traducción Automática Estadística:")
for frase in frases:
    traduccion = traducir(frase, modelo_traduccion)
    print(f"Español: {frase}")
    print(f"Inglés: {traduccion}\n")
