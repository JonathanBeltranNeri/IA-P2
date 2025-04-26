## Jonathan Beltran Neri
# Tema: Extracción de Información (Information Extraction)

# La extracción de información busca identificar entidades relevantes
# (personas, lugares, tiempos, objetos) en un texto no estructurado.

# Simularemos un sistema muy sencillo que reconoce "lugares" en frases.

# Corpus de frases
frases = [
    "El tren llegó a Guadalajara",
    "El camión partió de Puebla",
    "Caminando llegamos a Monterrey",
    "El tren salió rumbo a Querétaro",
    "Viajamos en camión hacia Veracruz"
]

# Lugares conocidos (diccionario de entidades)
lugares = ["Guadalajara", "Puebla", "Monterrey", "Querétaro", "Veracruz"]

# Función para extraer lugares mencionados
def extraer_lugares(frase, lista_lugares):
    encontrados = []
    for lugar in lista_lugares:
        if lugar in frase:
            encontrados.append(lugar)
    return encontrados

# Proceso de extracción
print("Extracción de Información (lugares detectados):")
for frase in frases:
    encontrados = extraer_lugares(frase, lugares)
    print(f"Frase: \"{frase}\"")
    print(f"  Lugares detectados: {encontrados}\n")
