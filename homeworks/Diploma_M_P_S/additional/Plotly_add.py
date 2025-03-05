import numpy as np
import plotly.graph_objects as go

# Данные для диаграммы рассеяния
x_scatter = np.random.uniform(-10, 10, 100)
y_scatter = np.random.uniform(-10, 10, 100)

# Создание интерактивной диаграммы рассеяния
scatter_fig = go.Figure(data=go.Scatter(x=x_scatter, y=y_scatter, mode='markers', marker=dict(color='blue', size=10, opacity=0.5)))
scatter_fig.update_layout(title='Интерактивная диаграмма рассеяния', xaxis_title='Ось X', yaxis_title='Ось Y')
scatter_fig.show()

# Параметры эллипсоида
a = 10  # Полуось по X
b = 5   # Полуось по Y
c = 3   # Полуось по Z (глубина)

# Параметры для построения
u = np.linspace(0, 2 * np.pi, 400)  # Углы для эллипсоида
v = np.linspace(0, np.pi, 200)       # Углы для глубины

# Параметрическая форма эллипсоида
X = a * np.outer(np.cos(u), np.sin(v))
Y = b * np.outer(np.sin(u), np.sin(v))
Z = c * np.outer(np.ones(np.size(u)), np.cos(v))

# Создание 3D-графика
fig = go.Figure(data=[go.Surface(x=X, y=Y, z=Z, colorscale='Viridis', showlegend=False)])

# Настройка заголовка и подписей осей
fig.update_layout(title='3D график эллипсоида', scene=dict(
    xaxis_title='Ось X',
    yaxis_title='Ось Y',
    zaxis_title='Ось Z'
))

# Показываем график
fig.show()