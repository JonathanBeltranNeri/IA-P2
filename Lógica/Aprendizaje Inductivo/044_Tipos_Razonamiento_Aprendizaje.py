# Jonathan Beltran Neri
# Tema: Aprendizaje Inductivo - Tipos de Razonamiento y Aprendizaje

# Este código explica los tipos principales de razonamiento utilizados en IA: 
# Deductivo, Inductivo y Abductivo. También muestra ejemplos simples de cada uno.

# Razonamiento Deductivo: parte de reglas generales para llegar a conclusiones específicas.
def razonamiento_deductivo():
    regla_general = "Todos los trenes llegan a tiempo"
    caso_especifico = "El tren de Guadalajara"
    conclusion = "El tren de Guadalajara llega a tiempo"
    return f"Deductivo:\n  Regla: {regla_general}\n  Caso: {caso_especifico}\n  Conclusión: {conclusion}"

# Razonamiento Inductivo: parte de casos específicos para formar una regla general.
def razonamiento_inductivo():
    observaciones = [
        "El tren de México llegó a tiempo",
        "El tren de Querétaro llegó a tiempo",
        "El tren de Puebla llegó a tiempo"
    ]
    regla_general = "Todos los trenes llegan a tiempo"
    return f"Inductivo:\n  Observaciones: {observaciones}\n  Regla Inferida: {regla_general}"

# Razonamiento Abductivo: parte de una observación y busca la causa más probable.
def razonamiento_abductivo():
    observacion = "El tren llegó tarde"
    posible_causa = "Hubo tráfico en la vía"
    return f"Abductivo:\n  Observación: {observacion}\n  Posible causa: {posible_causa}"

# Mostrar resultados
print(razonamiento_deductivo())
print()
print(razonamiento_inductivo())
print()
print(razonamiento_abductivo())
