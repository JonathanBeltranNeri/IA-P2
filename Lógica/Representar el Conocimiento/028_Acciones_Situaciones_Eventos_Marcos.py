## Jonathan Beltran Neri
# Tema: Acciones, Situaciones y Eventos – Marcos

# En IA, los marcos son estructuras de representación que describen objetos o situaciones
# mediante atributos ("slots") y sus valores posibles ("fillers").

# Este ejemplo representa una situación de transporte mediante un marco:
# una persona viajando desde un lugar a otro usando un medio de transporte.

# Definimos un marco llamado "viaje"
marco_viaje = {
    "actor": "persona1",                # Quién realiza la acción
    "origen": "Guadalajara",           # Punto de partida
    "destino": "Puebla",               # Lugar de llegada
    "medio_transporte": "camión",      # Medio utilizado
    "hora_salida": "08:00 AM",         # Hora de salida
    "duracion_aproximada": "5 horas"   # Estimación del viaje
}

# Función para mostrar el contenido del marco de manera ordenada
def mostrar_marco(marco):
    print("Representación de un Viaje (Marco):\n")
    for slot, valor in marco.items():
        print(f"{slot.replace('_', ' ').capitalize()}: {valor}")

# Ejecutar función de visualización
mostrar_marco(marco_viaje)
