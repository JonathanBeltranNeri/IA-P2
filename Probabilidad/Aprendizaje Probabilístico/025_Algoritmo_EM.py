## Jonathan Beltran Neri
# Tema: Algoritmo EM (Expectation-Maximization) - Transporte

# El algoritmo EM se utiliza cuando hay variables ocultas.
# En este caso, no sabemos el medio de transporte real (estado oculto),
# pero observamos "ruido", "motor", "silencio".

# Inicializamos las probabilidades de observación y transición
estados = ['Tren', 'Camión', 'Caminando']
observaciones_posibles = ['ruido', 'motor', 'silencio']

# Inicialización aleatoria de probabilidades (sujetas a cambio por EM)
P_estado = {'Tren': 1/3, 'Camión': 1/3, 'Caminando': 1/3}
P_observacion = {
    'Tren':      {'ruido': 0.6, 'motor': 0.3, 'silencio': 0.1},
    'Camión':    {'ruido': 0.3, 'motor': 0.5, 'silencio': 0.2},
    'Caminando': {'ruido': 0.1, 'motor': 0.2, 'silencio': 0.7}
}

# Datos observados (sin conocer el estado real)
datos = ['ruido', 'motor', 'silencio', 'motor', 'ruido']

# Algoritmo EM: 10 iteraciones
for iteracion in range(10):
    # E-step: calcular responsabilidades (probabilidades de cada estado dado la observación)
    responsabilidades = []
    for obs in datos:
        ponderado = {}
        for estado in estados:
            ponderado[estado] = P_estado[estado] * P_observacion[estado][obs]
        total = sum(ponderado.values())
        responsabilidades.append({k: v / total for k, v in ponderado.items()})

    # M-step: actualizar P_estado y P_observacion
    # Contar veces que cada estado "explicó" una observación
    conteo_estado = {e: 0.0 for e in estados}
    conteo_obs = {e: {o: 0.0 for o in observaciones_posibles} for e in estados}

    for i, obs in enumerate(datos):
        for estado in estados:
            r = responsabilidades[i][estado]
            conteo_estado[estado] += r
            conteo_obs[estado][obs] += r

    # Actualizar P_estado y P_observacion
    total_responsabilidad = sum(conteo_estado.values())
    for estado in estados:
        P_estado[estado] = conteo_estado[estado] / total_responsabilidad
        total_obs = sum(conteo_obs[estado].values())
        for obs in observaciones_posibles:
            P_observacion[estado][obs] = conteo_obs[estado][obs] / total_obs

# Mostrar resultados
print("Estimación después de EM:")
print("Distribución de estados:")
for estado in estados:
    print(f"  P({estado}) = {P_estado[estado]:.4f}")

print("\nDistribución de observaciones por estado:")
for estado in estados:
    print(f"  Estado: {estado}")
    for obs in observaciones_posibles:
        print(f"    P({obs} | {estado}) = {P_observacion[estado][obs]:.4f}")
