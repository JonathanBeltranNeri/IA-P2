## Jonathan Beltran Neri
# Tema: Lógica Difusa – Fuzzy CLIPS (simulación)

# Fuzzy CLIPS es una extensión del sistema CLIPS que permite trabajar con lógica difusa.
# Aquí simulamos un sistema basado en reglas difusas que toma decisiones con base en grados de pertenencia.

# Grados de lentitud (entrada del conjunto difuso)
lentitud = {
    "caminar": 1.0,
    "bicicleta": 0.75,
    "camion": 0.0,
    "tren": 0.0
}

# Reglas difusas simuladas (como si fueran reglas en Fuzzy CLIPS)
def reglas_fuzzy(medio, grado):
    if grado >= 0.7:
        return f"{medio} → seleccionado para trayectos relajados"
    elif 0.3 < grado < 0.7:
        return f"{medio} → uso recomendado si no hay prisa"
    else:
        return f"{medio} → no recomendable para descanso"

# Ejecutar sistema de inferencia difusa
print("Simulación de Fuzzy CLIPS – Decisión basada en Reglas Difusas:\n")
for medio, grado in lentitud.items():
    resultado = reglas_fuzzy(medio, grado)
    print(resultado)
