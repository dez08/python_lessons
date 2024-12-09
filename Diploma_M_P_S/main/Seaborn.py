import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

url = "https://raw.githubusercontent.com/dez08/python_lessons/refs/heads/main/MSFT.csv"
df = pd.read_csv(url)

# Назначение переменных данным из CSV файла
years = df['year']  # Год
earnings = df['earnings']  # Выручка
net_profit = df['revenue']  # Чистая прибыль
gross_profit = df['gross_profit']  # Валовая прибыль

# Создание линейного графика
plt.figure(figsize=(10, 8))
sns.set_style('darkgrid')
sns.lineplot(x=years, y=net_profit, color='green', marker='^', markersize=7, label='Чистая прибыль')
sns.lineplot(x=years, y=earnings, color='blue', marker='d', markersize=7, label='Выручка')
sns.lineplot(x=years, y=gross_profit, color='red', marker='h', markersize=7, label='Валовая прибыль')
plt.title('Финансовые показатели Microsoft Corporation с 2011 по 2024 гг.', fontsize=16)
plt.xlabel('Год', color='gray')
plt.ylabel('Млрд. $', color='gray')
plt.legend(title='Условные обозначения:')
plt.show()

# Создание столбчатой диаграммы
plt.figure(figsize=(14, 8))
colors = ['blue', 'green', 'red']
data = pd.DataFrame({
    'Год': years,
    'Выручка': earnings,
    'Валовая прибыль': gross_profit,
    'Чистая прибыль': net_profit
})
data = data.melt(id_vars='Год', var_name='Показатель', value_name='Значение')
sns.barplot(data=data, x='Год', y='Значение', hue='Показатель', palette=colors)
plt.title('Финансовые показатели Microsoft Corporation с 2011 по 2024 гг.', fontsize=20)
plt.xlabel('Год', fontsize=14)
plt.ylabel('Млрд. $', fontsize=14)
plt.legend(title='Условные обозначения:')
plt.show()

# Создание круговой диаграммы
plt.figure(figsize=(10, 10))
colors = sns.color_palette('deep')[0:3]
df[['earnings', 'revenue', 'gross_profit']].sum().plot.pie(autopct='%1.1f%%', labels=None, colors=colors,
                                                           explode=[0.1, 0.1, 0], shadow=True)
plt.legend(['Чистая прибыль', 'Выручка', 'Валовая прибыль'], title='Условные обозначения:', loc='upper left')
plt.title('Общие финансовые показатели Microsoft Corporation с 2011 по 2024 гг.', fontsize=16)
plt.ylabel('')
plt.show()
