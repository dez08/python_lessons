import seaborn as sns
import matplotlib.pyplot as plt

# Загрузим встроенный набор данных
tips = sns.load_dataset('tips')

# Установка стиля графиков
sns.set(style="whitegrid")

# Создание диаграммы рассеяния (scatter plot)
plt.figure(figsize=(12, 5))
sns.scatterplot(data=tips, x='total_bill', y='tip', hue='day', style='sex', s=100)
plt.title('График рассеяния: Чаевые против общего счета')
plt.xlabel('Общий счет')
plt.ylabel('Чаевые')

# Показать первый график
plt.tight_layout()
plt.show()

# Создание коробочного графика (box plot)
plt.figure(figsize=(12, 5))
sns.boxplot(data=tips, x='day', y='total_bill', palette='Set2')
plt.title('Коробчатый график: Общий счет по дням')
plt.xlabel('Дни недели')
plt.ylabel('Общий счет')

# Показать второй график
plt.tight_layout()
plt.show()