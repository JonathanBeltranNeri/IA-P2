## Jonathan Beltran Neri
# Tema: Lógicas de Orden Superior

# En lógica de orden superior, las variables no solo representan objetos,
# sino también predicados y funciones.

# Simularemos un ejemplo sencillo donde tratamos predicados como datos.

# Definimos predicados sobre transporte
def es_medio_rapido(medio):
    return medio in ["tren", "metro"]

def es_medio_ecologico(medio):
    return medio in ["bicicleta", "caminar"]

# Función de orden superior que recibe un predicado y una lista de medios
def filtrar_medios(predicado, medios):
    return [medio for medio in medios if predicado(medio)]

# Lista de medios disponibles
medios = ["tren", "camión", "bicicleta", "caminar", "metro"]

# Aplicamos funciones de orden superior
medios_rapidos = filtrar_medios(es_medio_rapido, medios)
medios_ecologicos = filtrar_medios(es_medio_ecologico, medios)

# Mostrar resultados
print("Lógica de Orden Superior - Clasificación de Medios de Transporte:")
print(f"Medios rápidos: {medios_rapidos}")
print(f"Medios ecológicos: {medios_ecologicos}")
