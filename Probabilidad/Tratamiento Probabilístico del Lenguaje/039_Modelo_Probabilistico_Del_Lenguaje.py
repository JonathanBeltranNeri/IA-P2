## Jonathan Beltran Neri
# Tema: Modelo Probabilístico del Lenguaje - Corpus

# En procesamiento de lenguaje natural, un modelo probabilístico de lenguaje
# asigna probabilidades a secuencias de palabras basándose en un corpus de texto.

# Simularemos un pequeño corpus y construiremos un modelo de probabilidad unigramas (palabra por palabra).
import matplotlib.pyplot as plt
from collections import Counter

# Simulamos un corpus simple
corpus = [
    "el tren llegó tarde",
    "el camión llegó temprano",
    "caminando llegamos rápido",
    "el tren salió puntual",
    "el camión salió tarde",
    "caminando llegamos tarde"
]

# Construimos la lista de todas las palabras
palabras = " ".join(corpus).split()

# Contamos las palabras
conteo = Counter(palabras)
total_palabras = sum(conteo.values())

# Calculamos la probabilidad de cada palabra
modelo_unigrama = {palabra: conteo[palabra] / total_palabras for palabra in conteo}

# Mostrar resultados
print("Modelo Probabilístico de Lenguaje (Unigramas):")
for palabra, prob in modelo_unigrama.items():
    print(f"P({palabra}) = {prob:.4f}")
# Graficar las probabilidades
palabras = list(modelo_unigrama.keys())
probabilidades = list(modelo_unigrama.values())

plt.figure(figsize=(10, 5))
plt.bar(palabras, probabilidades, color='skyblue')
plt.title('Modelo Probabilístico del Lenguaje (Unigramas)')
plt.xlabel('Palabra')
plt.ylabel('Probabilidad')
plt.xticks(rotation=45)
plt.grid(axis='y')
plt.tight_layout()
plt.show()