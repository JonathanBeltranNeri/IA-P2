## Jonathan Beltran Neri
# Tema: Análisis Sintáctico

# Este código realiza un análisis sintáctico muy básico para verificar si una instrucción
# sigue la estructura de una asignación: identificador = número.

def es_identificador(token):
    # Verifica si el token es un identificador válido (alfabético y no una palabra reservada)
    return token.isidentifier() and token not in ["if", "else", "while", "for"]

def es_numero(token):
    # Verifica si el token es un número (entero o decimal)
    try:
        float(token)
        return True
    except ValueError:
        return False

def analisis_sintactico(entrada):
    tokens = entrada.strip().split()
    
    if len(tokens) == 3:
        identificador, igual, valor = tokens
        if es_identificador(identificador) and igual == "=" and es_numero(valor):
            print("Sintaxis válida.")
        else:
            print("Error de sintaxis.")
    else:
        print("Error: la instrucción no tiene la estructura esperada.")

# Prueba de ejemplo
entrada = "precio = 250"
print(f"Instrucción: {entrada}")
analisis_sintactico(entrada)
