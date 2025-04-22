## Jonathan Beltran Neri
# Tema: Independencia Condicional

# Dos eventos A y B son independientes condicionalmente dado C si:
#     P(A ∩ B | C) = P(A | C) * P(B | C)
#
# En IA, esta propiedad permite simplificar modelos de probabilidad complejos.
# Se usa en redes bayesianas para representar dependencias entre variables.

# En este ejemplo, modelamos tres eventos:
# - A = que haya tráfico
# - B = que llegue tarde a clase
# - C = que llueva

# Suponemos que tráfico y llegar tarde están relacionados,
# pero si sabemos que llovió, entonces el tráfico y la tardanza
# dependen solamente de la lluvia, no entre sí.

# Probabilidades condicionadas dadas
P_trafico_dado_lluvia = 0.9
P_tarde_dado_lluvia = 0.8

# Probabilidad conjunta si son independientes condicionales dado que llueve:
P_trafico_y_tarde_dado_lluvia = P_trafico_dado_lluvia * P_tarde_dado_lluvia

# Probabilidad real conjunta medida (simulada):
P_real = 0.72  # Por ejemplo, recogida de datos

# Mostrar resultados
print("Independencia Condicional:")
print(f"  P(tráfico | lluvia) = {P_trafico_dado_lluvia}")
print(f"  P(tarde | lluvia)   = {P_tarde_dado_lluvia}")
print(f"  P(tráfico ∩ tarde | lluvia) (si independientes): {P_trafico_y_tarde_dado_lluvia:.4f}")
print(f"  P(tráfico ∩ tarde | lluvia) (observado):         {P_real:.4f}")

# Conclusión simple
if abs(P_trafico_y_tarde_dado_lluvia - P_real) < 0.01:
    print("\nLos eventos son aproximadamente independientes condicionalmente dado lluvia.")
else:
    print("\nLos eventos NO son independientes condicionalmente dado lluvia.")
