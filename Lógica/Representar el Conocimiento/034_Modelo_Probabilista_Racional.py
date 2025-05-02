## Jonathan Beltran Neri
# Tema: Modelo Probabilista Racional

# Este modelo combina probabilidad y utilidad para tomar decisiones racionales bajo incertidumbre.
# Se basa en elegir la acción con la mayor utilidad esperada.

# Definimos posibles acciones y sus probabilidades de éxito
acciones = {
    "Tomar el tren": {"prob_exito": 0.9, "utilidad": 8},
    "Tomar el camión": {"prob_exito": 0.7, "utilidad": 6},
    "Caminar": {"prob_exito": 0.4, "utilidad": 4}
}

# Función para calcular utilidad esperada
def utilidad_esperada(prob, utilidad):
    return prob * utilidad

# Evaluar cada acción
print("Modelo Probabilista Racional")
mejor_accion = None
mayor_utilidad = -1

for accion, datos in acciones.items():
    ue = utilidad_esperada(datos["prob_exito"], datos["utilidad"])
    print(f"{accion}: Utilidad Esperada = {ue}")
    if ue > mayor_utilidad:
        mayor_utilidad = ue
        mejor_accion = accion

# Mostrar la mejor decisión
print(f"\nMejor acción según la utilidad esperada: {mejor_accion}")
