## Jonathan Beltran Neri
# Tema: Resolución y Forma Normal Conjuntiva (FNC)

# La Forma Normal Conjuntiva (FNC) convierte una fórmula lógica
# en una conjunción de cláusulas (disyunciones de literales).

# La resolución es un método de inferencia que prueba la insatisfacibilidad
# tratando de derivar una contradicción.

# Ejemplo adaptado: transporte

# Base de cláusulas (cada cláusula es un conjunto de literales)
# Simulamos el conocimiento:
# - ¬tren_llega ∨ camion_sale
# - tren_llega ∨ caminando_llegamos
# - ¬camion_sale ∨ caminando_llegamos

clausulas = [
    {"¬tren_llega", "camion_sale"},
    {"tren_llega", "caminando_llegamos"},
    {"¬camion_sale", "caminando_llegamos"}
]

# Consulta: ¿Es posible inferir "caminando_llegamos"?

# Función para resolver dos cláusulas
def resolver(c1, c2):
    resolventes = []
    for literal in c1:
        complemento = literal[1:] if literal.startswith('¬') else '¬' + literal
        if complemento in c2:
            nueva = (c1.union(c2)) - {literal, complemento}
            resolventes.append(nueva)
    return resolventes

# Aplicación de resolución
def busqueda_resolucion(clausulas, objetivo):
    clausulas = clausulas + [{f"¬{objetivo}"}]  # Negamos el objetivo
    nuevas = set()

    while True:
        n = len(clausulas)
        pares = [(clausulas[i], clausulas[j]) for i in range(n) for j in range(i+1, n)]
        for (c1, c2) in pares:
            resolventes = resolver(c1, c2)
            for r in resolventes:
                if not r:  # Si hay una cláusula vacía, éxito
                    return True
                nuevas.add(frozenset(r))
        if nuevas.issubset(map(frozenset, clausulas)):
            return False  # No se pudo derivar contradicción
        for nuevo in nuevas:
            if set(nuevo) not in clausulas:
                clausulas.append(set(nuevo))

# Proceso de inferencia
resultado = busqueda_resolucion(clausulas, "caminando_llegamos")

# Mostrar resultado
print("¿Podemos inferir 'caminando_llegamos' usando resolución?")
print("Sí" if resultado else "No")
