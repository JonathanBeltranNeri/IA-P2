## Jonathan Beltran Neri
# Tema: Separabilidad Lineal

# Un conjunto de datos es linealmente separable si existe una línea (o un hiperplano en dimensiones mayores)
# que puede dividir perfectamente las clases sin errores.

# En este ejemplo, mostramos un conjunto separable y otro no separable.

import matplotlib.pyplot as plt

# Datos separables (ejemplo sencillo)
X_separable = [
    [1, 7], [2, 8], [3, 8],   # Clase 0
    [5, 1], [6, 2], [7, 3]    # Clase 1
]
y_separable = [0, 0, 0, 1, 1, 1]

# Datos no separables (con traslape)
X_no_separable = [
    [1, 7], [2, 8], [5, 5],    # Clase 0
    [5, 1], [6, 2], [5, 5]     # Clase 1
]
y_no_separable = [0, 0, 0, 1, 1, 1]

# Graficar datos separables
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
for punto, clase in zip(X_separable, y_separable):
    if clase == 0:
        plt.scatter(punto[0], punto[1], color='blue')
    else:
        plt.scatter(punto[0], punto[1], color='red')
plt.title('Datos Linealmente Separables')
plt.xlabel('x1')
plt.ylabel('x2')

# Graficar datos no separables
plt.subplot(1, 2, 2)
for punto, clase in zip(X_no_separable, y_no_separable):
    if clase == 0:
        plt.scatter(punto[0], punto[1], color='blue')
    else:
        plt.scatter(punto[0], punto[1], color='red')
plt.title('Datos NO Linealmente Separables')
plt.xlabel('x1')
plt.ylabel('x2')

plt.tight_layout()
plt.show()
