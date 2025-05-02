## Jonathan Beltran Neri
# Algoritmo: Algoritmos de Planificación (STRIPS y ADL)

# Estructura del grafo utilizado:
#
#         México
#        /      \
#   Querétaro   Puebla
#      |           |
#  San Luis     Veracruz
#      \         /
#      Monterrey

# Este algoritmo simula un planificador simple usando STRIPS.
# Se definen acciones con precondiciones y efectos para alcanzar el objetivo.

# Diccionario del grafo
grafo = {
    'México': ['Querétaro', 'Puebla'],
    'Querétaro': ['San Luis'],
    'Puebla': ['Veracruz'],
    'San Luis': ['Monterrey'],
    'Veracruz': ['Monterrey'],
    'Monterrey': []
}

# Definición de acción tipo STRIPS
class Accion:
    def __init__(self, nombre, precondiciones, efectos):
        self.nombre = nombre
        self.precondiciones = precondiciones
        self.efectos = efectos

# Acciones posibles con precondiciones y efectos
acciones = [
    Accion('Ir de México a Querétaro (tren)', ['en(México)'], ['en(Querétaro)', 'no(en(México))']),
    Accion('Ir de México a Puebla (camión)', ['en(México)'], ['en(Puebla)', 'no(en(México))']),
    Accion('Ir de Querétaro a San Luis (camión)', ['en(Querétaro)'], ['en(San Luis)', 'no(en(Querétaro))']),
    Accion('Ir de Puebla a Veracruz (caminando)', ['en(Puebla)'], ['en(Veracruz)', 'no(en(Puebla))']),
    Accion('Ir de San Luis a Monterrey (tren)', ['en(San Luis)'], ['en(Monterrey)', 'no(en(San Luis))']),
    Accion('Ir de Veracruz a Monterrey (camión)', ['en(Veracruz)'], ['en(Monterrey)', 'no(en(Veracruz))'])
]

# Estado inicial y meta
estado = ['en(México)']
meta = 'en(Monterrey)'

# Función para aplicar una acción
def aplicar_accion(accion, estado_actual):
    if all(p in estado_actual for p in accion.precondiciones):
        nuevo_estado = estado_actual.copy()
        for efecto in accion.efectos:
            if efecto.startswith('no('):
                sin = efecto[3:-1]
                if sin in nuevo_estado:
                    nuevo_estado.remove(sin)
            else:
                if efecto not in nuevo_estado:
                    nuevo_estado.append(efecto)
        return nuevo_estado
    return None

# Planificación simple hacia adelante
def planificar(estado_inicial, acciones, meta):
    estado_actual = estado_inicial.copy()
    plan = []

    while meta not in estado_actual:
        accion_aplicada = False
        for accion in acciones:
            nuevo_estado = aplicar_accion(accion, estado_actual)
            if nuevo_estado:
                estado_actual = nuevo_estado
                plan.append(accion.nombre)
                accion_aplicada = True
                break
        if not accion_aplicada:
            break
    return plan if meta in estado_actual else None

# Ejecutar planificación
plan = planificar(estado, acciones, meta)

# Mostrar resultado
print("Algoritmo de Planificación (STRIPS)")
if plan:
    print("Plan encontrado:")
    for paso in plan:
        print("-", paso)
else:
    print("No se encontró un plan para alcanzar la meta.")
