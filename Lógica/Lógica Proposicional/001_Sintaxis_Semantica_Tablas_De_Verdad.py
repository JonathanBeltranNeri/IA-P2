## Jonathan Beltran Neri
# Tema: Sintaxis y Semántica - Tablas de Verdad

# - tren_llega
# - camion_sale
# La fórmula a analizar será: (tren_llega ∧ camion_sale) → tren_llega

import itertools

# Definimos las variables proposicionales
variables = ['tren_llega', 'camion_sale']

# Definimos la fórmula que queremos evaluar: (tren_llega ∧ camion_sale) → tren_llega
def formula(tren_llega, camion_sale):
    return (tren_llega and camion_sale) <= tren_llega  # (tren_llega ∧ camion_sale) implica tren_llega

# Generamos todas las combinaciones de valores posibles (True/False)
combinaciones = list(itertools.product([True, False], repeat=len(variables)))

# Mostrar la tabla de verdad
print("Tabla de Verdad para (tren_llega ∧ camion_sale) → tren_llega\n")
print(f"{'tren_llega':<12}{'camion_sale':<14}{'Resultado'}")
print("-" * 40)
for valores in combinaciones:
    tren_llega, camion_sale = valores
    resultado = formula(tren_llega, camion_sale)
    print(f"{str(tren_llega):<12}{str(camion_sale):<14}{str(resultado)}")
