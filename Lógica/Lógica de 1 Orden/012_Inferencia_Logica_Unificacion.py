## Jonathan Beltran Neri
# Tema: Inferencia Lógica - Unificación

# La unificación es el proceso de hacer que dos expresiones lógicas sean idénticas
# mediante la sustitución adecuada de variables.

# Simularemos un ejemplo sencillo de transporte.

# Expresiones a unificar
expresion1 = ("viaja", "X", "tren")
expresion2 = ("viaja", "persona1", "Y")

# Función para intentar unificar dos expresiones
def unificar(expr1, expr2):
    sustituciones = {}
    if expr1[0] != expr2[0]:
        return None  # Predicados diferentes, no se puede unificar
    
    for t1, t2 in zip(expr1[1:], expr2[1:]):
        if t1 == t2:
            continue
        elif t1.startswith("X") and not t2.startswith("X"):
            sustituciones[t1] = t2
        elif t2.startswith("X") and not t1.startswith("X"):
            sustituciones[t2] = t1
        elif t1.startswith("Y") and not t2.startswith("Y"):
            sustituciones[t1] = t2
        elif t2.startswith("Y") and not t1.startswith("Y"):
            sustituciones[t2] = t1
        else:
            return None  # Conflicto, no se puede unificar
    return sustituciones

# Ejecutar unificación
resultado = unificar(expresion1, expresion2)

# Mostrar resultados
print("Resultado de la Unificación:")
if resultado:
    for variable, valor in resultado.items():
        print(f"{variable} = {valor}")
else:
    print("No fue posible unificar las expresiones.")
