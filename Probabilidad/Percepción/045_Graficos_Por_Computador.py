## Jonathan Beltran Neri
# Tema: Gráficos por Computador

# Los gráficos por computador permiten crear imágenes y representaciones visuales
# de objetos o escenas usando algoritmos.

# En este ejemplo básico, dibujamos figuras geométricas simulando una escena sencilla.

import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt

# Creamos una figura
fig, ax = plt.subplots()

# Dibujamos un rectángulo (ejemplo de edificio)
edificio = plt.Rectangle((2, 1), 4, 6, edgecolor='black', facecolor='lightgray')
ax.add_patch(edificio)

# Dibujamos un círculo (ejemplo de sol)
sol = plt.Circle((8, 8), 1, edgecolor='orange', facecolor='yellow')
ax.add_patch(sol)

# Dibujamos un triángulo (ejemplo de montaña)
montaña_x = [0, 1.5, 3]
montaña_y = [1, 4, 1]
ax.fill(montaña_x, montaña_y, color='brown')

# Ajustes de la gráfica
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect('equal')
plt.title('Gráficos por Computador - Escena Simple')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()
