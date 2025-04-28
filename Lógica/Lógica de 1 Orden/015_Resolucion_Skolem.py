## Jonathan Beltran Neri
# Tema: Resolución - Skolemización

# La Skolemización es un proceso que elimina cuantificadores existenciales
# en lógica de primer orden, reemplazándolos por funciones o constantes de Skolem.

# Ejemplo aplicado a transporte:

# Fórmula original (informal):
# ∀X ∃Y (viaja(X, Y))   → Para toda persona X existe un medio Y tal que X viaja en Y.

# Tras skolemizar:
# ∀X (viaja(X, f(X)))   → Cada persona X viaja en un medio dependiente de X (f(X)).

# Vamos a simular este razonamiento.

# Base de hechos: conjunto de personas
personas = ["persona1", "persona2", "persona3"]

# Función de Skolem (asigna un transporte a cada persona)
def f_skolem(x):
    asignaciones = {
        "persona1": "tren",
        "persona2": "camión",
        "persona3": "bicicleta"
    }
    return asignaciones.get(x, "caminar")

# Simulación de viaje
def viajes(personas):
    resultado = []
    for persona in personas:
        medio = f_skolem(persona)
        resultado.append((persona, medio))
    return resultado

# Ejecutar
viajes_resultantes = viajes(personas)

# Mostrar resultados
print("Resultados después de Skolemización:")
for persona, medio in viajes_resultantes:
    print(f"{persona} viaja en {medio}")
