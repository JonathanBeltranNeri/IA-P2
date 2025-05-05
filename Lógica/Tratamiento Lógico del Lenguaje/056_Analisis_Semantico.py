## Jonathan Beltran Neri
# Tema: Análisis Semántico

# Este código verifica si la asignación de una variable es coherente con su tipo declarado,
# usando un ejemplo de transporte con "tren", "camión" y "caminar" como variables.

# Tabla de símbolos (variables declaradas con tipo)
tabla_simbolos = {
    "tren": "int",
    "camion": "str",
    "caminar": "float"
}

def es_valor_valido(tipo, valor):
    # Verifica si el valor es compatible con el tipo declarado
    try:
        if tipo == "int":
            int(valor)
        elif tipo == "float":
            float(valor)
        elif tipo == "str":
            if not (valor.startswith('"') and valor.endswith('"')):
                return False
        else:
            return False
        return True
    except ValueError:
        return False

def analisis_semantico(instruccion):
    tokens = instruccion.strip().split()

    if len(tokens) != 3 or tokens[1] != "=":
        print("Error de sintaxis.")
        return

    variable, _, valor = tokens

    if variable not in tabla_simbolos:
        print(f"Variable '{variable}' no declarada.")
        return

    tipo_esperado = tabla_simbolos[variable]

    if es_valor_valido(tipo_esperado, valor):
        print("Asignación semánticamente válida.")
    else:
        print(f"Tipo incompatible. Se esperaba {tipo_esperado}.")

# Pruebas de ejemplo
instrucciones = [
    'tren = 5',
    'camion = "Weg"',
    'caminar = 2.3',
    'caminar = "rápido"'
]

for instr in instrucciones:
    print(f"Instrucción: {instr}")
    analisis_semantico(instr)
    print()
