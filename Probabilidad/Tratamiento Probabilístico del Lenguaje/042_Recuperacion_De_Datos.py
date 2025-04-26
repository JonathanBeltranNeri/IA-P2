## Jonathan Beltran Neri
# Tema: Recuperación de Datos (Information Retrieval)

# La Recuperación de Datos se refiere a encontrar información relevante
# dentro de grandes volúmenes de datos basándose en una consulta.

# Simulamos un pequeño motor de búsqueda basado en conteo de palabras.

# Corpus de documentos
documentos = {
    "doc1": "el tren llegó tarde pero salió puntual",
    "doc2": "el camión llegó temprano pero tardó en salir",
    "doc3": "caminando llegamos muy rápido",
    "doc4": "el tren y el camión llegaron juntos",
    "doc5": "caminando se disfruta más el trayecto"
}

# Consulta de búsqueda
consulta = "llegó tren"

# Procesamos la consulta
consulta_palabras = consulta.split()

# Buscamos documentos que contengan las palabras
ranking = {}

for doc, texto in documentos.items():
    palabras_doc = texto.split()
    score = sum(palabras_doc.count(p) for p in consulta_palabras)
    if score > 0:
        ranking[doc] = score

# Ordenamos documentos por relevancia
ranking_ordenado = sorted(ranking.items(), key=lambda item: item[1], reverse=True)

# Mostrar resultados
print("Resultados de recuperación de datos:")
for doc, score in ranking_ordenado:
    print(f"{doc}: relevancia {score}")
