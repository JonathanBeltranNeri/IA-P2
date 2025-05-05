## Jonathan Beltran Neri
# Tema: Gramática Causal Definida

# Este código implementa una grámatica causal simple donde ciertos eventos (causas)
# desencadenan otros eventos (efectos), usando ejemplos de transporte.

# Definimos las reglas causales
reglas = {
    "caminar": ["cansancio"],
    "camion": ["tráfico"],
    "tren": ["puntualidad"],
    "tráfico": ["retraso"],
    "cansancio": ["descanso"],
    "puntualidad": ["llegada a tiempo"]
}

def inferir_efectos(evento_inicial, reglas):
    efectos = set()
    pendientes = [evento_inicial]

    while pendientes:
        actual = pendientes.pop()
        if actual in reglas:
            for efecto in reglas[actual]:
                if efecto not in efectos:
                    efectos.add(efecto)
                    pendientes.append(efecto)
    return efectos

# Probar la inferencia causal
evento = "camion"
ef = inferir_efectos(evento, reglas)
print(f"Efectos causados por '{evento}':", ef)
