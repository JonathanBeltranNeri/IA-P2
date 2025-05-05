## Jonathan Beltran Neri
# Tema: Ambigüedad en el Lenguaje

# Este código muestra un ejemplo de ambigüedad sintáctica y semántica usando frases sencillas.
# Se analiza el doble significado de la frase y se imprime cada interpretación por separado.

# Frase ambigua
frase = "Fui al banco con el palo"

# Interpretaciones posibles
interpretaciones = [
    "Fui a la institución financiera llevando un palo.",
    "Fui a sentarme al banco del parque con un palo en la mano."
]

# Mostrar frase original y sus posibles significados
print("Frase ambigua:", frase)
print("\nInterpretaciones posibles:")
for i, interpretacion in enumerate(interpretaciones, 1):
    print(f"{i}. {interpretacion}")
