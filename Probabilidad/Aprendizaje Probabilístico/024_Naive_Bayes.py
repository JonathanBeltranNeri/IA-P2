## Jonathan Beltran Neri
# Tema: Naïve Bayes - Clasificación basada en observaciones de transporte

# En este ejemplo, el sistema intenta predecir el medio de transporte usado (Tren, Camión, Caminando)
# basándose en observaciones ruidosas como "motor", "ruido" o "silencio",
# usando el clasificador Naïve Bayes.

# P(transporte)
P_tren = 1/3
P_camion = 1/3
P_caminando = 1/3

# P(observación | transporte)
P_ruido = {
    'Tren': 0.7,
    'Camión': 0.3,
    'Caminando': 0.1
}

P_motor = {
    'Tren': 0.2,
    'Camión': 0.6,
    'Caminando': 0.2
}

P_silencio = {
    'Tren': 0.1,
    'Camión': 0.1,
    'Caminando': 0.7
}

# Observaciones recibidas
observaciones = ['ruido', 'motor', 'silencio']

# Cálculo de probabilidades (Naïve Bayes: se asume independencia condicional)
P_dado_tren = P_ruido['Tren'] * P_motor['Tren'] * P_silencio['Tren'] * P_tren
P_dado_camion = P_ruido['Camión'] * P_motor['Camión'] * P_silencio['Camión'] * P_camion
P_dado_caminando = P_ruido['Caminando'] * P_motor['Caminando'] * P_silencio['Caminando'] * P_caminando

# Normalización
total = P_dado_tren + P_dado_camion + P_dado_caminando

P_tren_final = P_dado_tren / total
P_camion_final = P_dado_camion / total
P_caminando_final = P_dado_caminando / total

# Mostrar resultados
print("Clasificación con Naïve Bayes (basado en observaciones acústicas):")
print(f"P(Tren | observaciones)      = {P_tren_final:.4f}")
print(f"P(Camión | observaciones)    = {P_camion_final:.4f}")
print(f"P(Caminando | observaciones) = {P_caminando_final:.4f}")
