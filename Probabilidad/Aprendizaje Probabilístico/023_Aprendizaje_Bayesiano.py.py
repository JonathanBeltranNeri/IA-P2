## Jonathan Beltran Neri
# Tema: Aprendizaje Bayesiano

# El aprendizaje bayesiano permite actualizar nuestras creencias sobre un modelo o hipótesis
# conforme observamos más datos, usando la Regla de Bayes.

# Este ejemplo simple ilustra cómo un sistema ajusta su creencia sobre la probabilidad de que
# un cliente compre un producto dado que visita una tienda, basándose en los datos observados.

# Hipótesis: H = "El cliente comprará"
# Datos: visitas donde se observa si compró o no

# Suposición inicial (a priori): 50% de probabilidad de que un cliente compre
P_compra_apriori = 0.5
P_no_compra_apriori = 0.5

# Verosimilitud basada en datos previos
# Supón que de 10 personas que compraron, 7 habían dicho que "sí me interesa"
# y de 10 que no compraron, solo 2 dijeron "sí me interesa"

# P(respuesta="sí" | compra)
P_si_dado_compra = 0.7
# P(respuesta="sí" | no compra)
P_si_dado_no_compra = 0.2

# Observamos un nuevo cliente que dice "sí me interesa"
# Usamos Bayes para calcular P(compra | sí)

# P(respuesta="sí") = P(sí | compra) * P(compra) + P(sí | no compra) * P(no compra)
P_si = (P_si_dado_compra * P_compra_apriori) + (P_si_dado_no_compra * P_no_compra_apriori)

# Aplicamos Bayes:
P_compra_dado_si = (P_si_dado_compra * P_compra_apriori) / P_si

# Mostramos el resultado
print("Aprendizaje Bayesiano - Actualización de creencias:")
print(f"P(compra | sí me interesa) = {P_compra_dado_si:.4f}")
