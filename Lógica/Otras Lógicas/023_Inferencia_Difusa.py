## Jonathan Beltran Neri
# Tema: Lógica Difusa – Inferencia Difusa

# La inferencia difusa aplica reglas con grados de pertenencia
# para tomar decisiones aproximadas y no binarias.

# Entrada: grado de lentitud (por ejemplo, calculado con conjunto difuso)
# Salida: nivel de confort estimado

# Función de inferencia difusa basada en la lentitud
def clasificar_confort(lentitud):
    if lentitud >= 0.7:
        return "muy cómodo"
    elif lentitud >= 0.4:
        return "cómodo"
    elif lentitud > 0:
        return "poco cómodo"
    else:
        return "incómodo"

# Valores de lentitud simulados (por ejemplo, salidos de un conjunto difuso)
grados_lentitud = {
    "caminar": 1.0,
    "bicicleta": 0.75,
    "camion": 0.0,
    "tren": 0.0
}

# Aplicar inferencia difusa
print("Inferencia Difusa – Confort según Lentitud:\n")
for medio, grado in grados_lentitud.items():
    resultado = clasificar_confort(grado)
    print(f"{medio:<10} → grado de lentitud: {grado} → confort estimado: {resultado}")
