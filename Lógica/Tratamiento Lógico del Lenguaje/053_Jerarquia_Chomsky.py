## Jonathan Beltran Neri
# Tema: Gramáticas - Jerarquía de Chomsky

# Este código presenta ejemplos ilustrativos de cada tipo de gramática 
# en la jerarquía de Chomsky: Tipo 0 (no restringida), Tipo 1 (sensibles al contexto),
# Tipo 2 (libres de contexto) y Tipo 3 (regulares).

# Tipo 0: Gramática No Restringida
# No tiene limitaciones sobre el lado izquierdo o derecho de las reglas
gramatica_tipo_0 = [
    "A B C → a B",
    "B A → b C",
]

# Tipo 1: Gramática Sensible al Contexto
# Las reglas tienen forma αAβ → αγβ (misma longitud o mayor del lado derecho)
gramatica_tipo_1 = [
    "A B → B A",
    "a A b → a b B",
]

# Tipo 2: Gramática Libre de Contexto
# Las reglas son de la forma A → γ (A es una variable, γ puede ser cualquier cadena)
gramatica_tipo_2 = [
    "S → aSb",
    "S → ab",
]

# Tipo 3: Gramática Regular
# Las reglas son de la forma A → aB o A → a (terminal seguido opcionalmente por una variable)
gramatica_tipo_3 = [
    "A → aB",
    "B → b",
]

# Mostrar cada tipo de gramática
print("Gramática Tipo 0: No Restringida")
for regla in gramatica_tipo_0:
    print(" ", regla)

print("\nGramática Tipo 1: Sensible al Contexto")
for regla in gramatica_tipo_1:
    print(" ", regla)

print("\nGramática Tipo 2: Libre de Contexto")
for regla in gramatica_tipo_2:
    print(" ", regla)

print("\nGramática Tipo 3: Regular")
for regla in gramatica_tipo_3:
    print(" ", regla)
