## Jonathan Beltran Neri
# Tema: Análisis Léxico

# Este código realiza un análisis léxico simple, separando una cadena de texto en
# tokens (identificadores, números, palabras clave y símbolos). Es el primer paso
# en la compilación, donde se reconocen los componentes básicos del lenguaje fuente.

import re

# Definición de expresiones regulares para diferentes tipos de tokens
palabras_clave = {"if", "else", "while", "return", "int", "float"}
identificador = r"[a-zA-Z_][a-zA-Z_0-9]*"
numero = r"\d+(\.\d+)?"
simbolo = r"[+\-*/=(){};]"

# Cadena de entrada para analizar
entrada = "int contador = 10; while (contador > 0) { contador = contador - 1; }"

# Tokenización usando expresiones regulares combinadas
tokens = re.findall(f"{numero}|{identificador}|{simbolo}", entrada)

# Clasificación de tokens
print("Tokens encontrados:")
for token in tokens:
    if token in palabras_clave:
        tipo = "Palabra clave"
    elif re.fullmatch(numero, token):
        tipo = "Número"
    elif re.fullmatch(simbolo, token):
        tipo = "Símbolo"
    else:
        tipo = "Identificador"
    print(f"{token} → {tipo}")
