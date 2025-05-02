## Jonathan Beltran Neri
# Tema: Ingeniería del Conocimiento – Ontologías

# Una ontología define clases, relaciones y jerarquías entre conceptos,
# permitiendo representar formalmente el conocimiento de un dominio.

# En este ejemplo se modela una pequeña ontología del dominio transporte.

# -------------------------------
# Definición de Clases e Instancias
# -------------------------------

clases = {
    "Transporte": ["Tren", "Camión", "Bicicleta", "Metro"],
    "Persona": ["Pasajero", "Conductor"]
}

# Relaciones Ontológicas

relaciones = {
    "usa": [("Pasajero", "Tren"), ("Pasajero", "Camión"), ("Pasajero", "Bicicleta")],
    "conduce": [("Conductor", "Tren"), ("Conductor", "Camión")],
    "es_subclase_de": [("Tren", "Transporte"), ("Camión", "Transporte"), ("Bicicleta", "Transporte")]
}

# Visualización de la Ontología

def mostrar_ontologia(clases, relaciones):
    print("📚 Ontología del Dominio Transporte\n")

    print("Clases:")
    for clase, instancias in clases.items():
        print(f"  {clase}: {', '.join(instancias)}")

    print("\nRelaciones:")
    for tipo, pares in relaciones.items():
        for sujeto, objeto in pares:
            print(f"  {sujeto} {tipo.replace('_', ' ')} {objeto}")

# Ejecutar
mostrar_ontologia(clases, relaciones)
