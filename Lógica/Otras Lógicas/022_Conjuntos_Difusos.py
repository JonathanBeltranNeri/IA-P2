## Jonathan Beltran Neri
# Tema: Lógica Difusa – Conjuntos Difusos

# En un conjunto difuso, los elementos pueden pertenecer con un grado entre 0 y 1.
# Este ejemplo aplica lógica difusa al concepto de “lentitud” en medios de transporte.

# Velocidades en km/h
velocidades = {
    "caminar": 5,
    "bicicleta": 15,
    "camion": 40,
    "tren": 80
}

# Función de pertenencia para el conjunto difuso "lento"
def pertenencia_lento(vel):
    if vel <= 10:
        return 1.0
    elif vel >= 30:
        return 0.0
    else:
        return round((30 - vel) / 20, 2)

# Evaluar cada medio
print("Conjunto Difuso – Grado de Lentitud:\n")
for medio, vel in velocidades.items():
    grado = pertenencia_lento(vel)
    print(f"{medio:<10} → velocidad: {vel} km/h → grado de lentitud: {grado}")
