import pandas as pd
import matplotlib.pyplot as plt


url = "https://raw.githubusercontent.com/dez08/python_lessons/refs/heads/main/MSFT.csv"
df = pd.read_csv(url)

# Назначение переменных данным из CSV файла
years = df['year']  # Год
earnings = df['earnings']  # Выручка
net_profit = df['revenue']  # Чистая прибыль
gross_profit = df['gross_profit']  # Валовая прибыль

# Создание линейного графика
plt.figure(figsize=(12, 8))
plt.title('Финансовые показатели Microsoft Corporation с 2011 по 2024 гг.', fontsize=18)
plt.xlabel('Год', color='gray', fontsize=14)
plt.ylabel('Млрд. $', color='gray', fontsize=14)

# Построение кривых
plt.plot(years, earnings, label='Выручка', color='green', marker='^', markersize=8)
plt.plot(years, net_profit, label='Чистая прибыль', color='red', linestyle='--', linewidth=3, marker='o', markersize=8)
plt.plot(years, gross_profit, label='Валовая прибыль', color='blue', marker='*', markersize=8)

# Создание легенды
plt.legend(loc='upper left', title='Условные обозначения:', fontsize=12)
plt.grid()
plt.show()

# Создание столбчатой диаграммы
plt.figure(figsize=(12, 8))
plt.title('Финансовые показатели Microsoft Corporation с 2011 по 2024 гг.', fontsize=18)
plt.xlabel('Год', color='gray', fontsize=14)
plt.ylabel('Млрд. $', color='gray', fontsize=14)

# Построение столбчатых графиков
width = 0.25
x = range(len(years))

plt.bar([p - width for p in x], earnings, width=width, color='g', label='Выручка')
plt.bar(x, gross_profit, width=width, color='b', label='Валовая прибыль')
plt.bar([p + width for p in x], net_profit, width=width, color='r', label='Чистая прибыль')

plt.xticks(x, years)
plt.legend(loc='upper left', title='Условные обозначения:', fontsize=12)
plt.gca().invert_xaxis()
plt.show()

# Создание круговой диаграммы
plt.figure(figsize=(12, 8))
financial_sums = df[['earnings', 'revenue', 'gross_profit']].sum()
financial_sums.plot.pie(autopct='%1.1f%%', labels=None, explode=[0.1, 0, 0], startangle=90)
plt.legend(['Выручка', 'Чистая прибыль', 'Валовая прибыль'], loc='upper right', title='Условные обозначения:')
plt.title('Общие финансовые показатели Microsoft Corporation с 2011 по 2024 гг.', fontsize=18)
plt.ylabel('')
plt.show()
