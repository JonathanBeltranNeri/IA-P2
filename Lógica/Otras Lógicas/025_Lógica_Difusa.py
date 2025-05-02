## Jonathan Beltran Neri
# Tema: Lógica Difusa – Conjuntos Difusos, Inferencia Difusa y Simulación de Fuzzy CLIPS

# Este archivo combina los tres pilares básicos de la lógica difusa:
# 1. Conjuntos Difusos
# 2. Inferencia Difusa
# 3. Simulación de un sistema tipo Fuzzy CLIPS

# -------------------------------
# 1. Conjuntos Difusos – Lentitud
# -------------------------------

velocidades = {
    "caminar": 5,
    "bicicleta": 15,
    "camion": 40,
    "tren": 80
}

def pertenencia_lento(vel):
    if vel <= 10:
        return 1.0
    elif vel >= 30:
        return 0.0
    else:
        return round((30 - vel) / 20, 2)

# -------------------------------
# 2. Inferencia Difusa – Confort
# -------------------------------

def clasificar_confort(lentitud):
    if lentitud >= 0.7:
        return "muy cómodo"
    elif lentitud >= 0.4:
        return "cómodo"
    elif lentitud > 0:
        return "poco cómodo"
    else:
        return "incómodo"

# -------------------------------
# 3. Simulación de Fuzzy CLIPS – Reglas
# -------------------------------

def reglas_fuzzy(medio, grado):
    if grado >= 0.7:
        return f"{medio} → recomendado para trayectos relajados"
    elif 0.3 < grado < 0.7:
        return f"{medio} → aceptable si no hay prisa"
    else:
        return f"{medio} → no recomendable para descanso"

# -------------------------------
# Ejecución del sistema difuso completo
# -------------------------------

print("Lógica Difusa – Sistema Completo:\n")
for medio, vel in velocidades.items():
    grado = pertenencia_lento(vel)
    confort = clasificar_confort(grado)
    resultado = reglas_fuzzy(medio, grado)
    print(f"{medio:<10} → velocidad: {vel} km/h → lentitud: {grado} → confort: {confort} → regla: {resultado}")
