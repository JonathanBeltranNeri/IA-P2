## Jonathan Beltran Neri
# Tema: Equivalencia, Validez y Satisfacibilidad

# En Lógica Proposicional, verificamos si dos fórmulas son equivalentes,
# si una fórmula es válida (siempre verdadera) o si es satisfacible (verdadera en al menos un caso).

import itertools

# Definimos las variables
variables = ['tren_llega', 'camion_sale']

# Fórmulas a comparar:
# Fórmula 1: (tren_llega ∨ camion_sale)
# Fórmula 2: ¬(¬tren_llega ∧ ¬camion_sale) (ley de De Morgan)

def formula1(tren_llega, camion_sale):
    return tren_llega or camion_sale

def formula2(tren_llega, camion_sale):
    return not (not tren_llega and not camion_sale)

# Generamos todas las combinaciones posibles de valores de verdad
combinaciones = list(itertools.product([True, False], repeat=len(variables)))

# Verificamos equivalencia
equivalente = True
print("Evaluación de Equivalencia:")
print(f"{'tren_llega':<12}{'camion_sale':<14}{'Fórmula1':<10}{'Fórmula2'}")
print("-" * 50)
for valores in combinaciones:
    tren_llega, camion_sale = valores
    f1 = formula1(tren_llega, camion_sale)
    f2 = formula2(tren_llega, camion_sale)
    print(f"{str(tren_llega):<12}{str(camion_sale):<14}{str(f1):<10}{str(f2)}")
    if f1 != f2:
        equivalente = False

# Evaluación de validez y satisfacibilidad
todos_verdaderos = all(formula1(*comb) for comb in combinaciones)
alguno_verdadero = any(formula1(*comb) for comb in combinaciones)

print("\nResultados:")
print(f"¿Son equivalentes las fórmulas? {'Sí' if equivalente else 'No'}")
print(f"¿Fórmula 1 es válida (siempre verdadera)? {'Sí' if todos_verdaderos else 'No'}")
print(f"¿Fórmula 1 es satisfacible (verdadera al menos una vez)? {'Sí' if alguno_verdadero else 'No'}")
