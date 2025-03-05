import numpy as np
import matplotlib.pyplot as plt

# Данные для диаграммы рассеяния
x_scatter = np.random.uniform(-10, 10, 100)
y_scatter = np.random.uniform(-10, 10, 100)
plt.figure(figsize=(10, 5))
plt.scatter(x_scatter, y_scatter, c='blue', alpha=0.5)
plt.title('Диаграмма рассеяния')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.axhline(0, color='gray', lw=0.5, ls='--')
plt.axvline(0, color='gray', lw=0.5, ls='--')
plt.grid()
plt.show()

# Данные для 3D-графика параболы (Z = x^2 + y^2)
X = np.linspace(-10, 10, 400)
Y = np.linspace(-10, 10, 400)
X, Y = np.meshgrid(X, Y)
Z = X**2 + Y**2  # Формула параболы: z = x^2 + y^2

# Создание 3D-графика
fig = plt.figure(figsize=(10, 7))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
ax.set_title('3D график параболы')
ax.set_xlabel('Ось X')
ax.set_ylabel('Ось Y')
ax.set_zlabel('Ось Z')
plt.show()