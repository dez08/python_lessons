# Домашнее задание по теме "Обзор сторонних библиотек Python"

import pandas as pd
import matplotlib.pyplot as plt

# Загрузка данных из CSV файла
url = 'https://raw.githubusercontent.com/dez08/python_lessons/refs/heads/main/Modul%2011/resolve1/titanic.csv'
df = pd.read_csv(url)

# Показать первые несколько строк данных
print("Первые 5 строк данных:")
print(df.head())

# Основная информация о наборе данных
print("\nИнформация о наборе данных:")
print(df.info())

# Статистические характеристики количественных переменных
print("\nСтатистические характеристики:")
print(df.describe())

# Количество выживших и не выживших
survival_counts = df['Survived'].value_counts()
print("\nКоличество выживших и не выживших:")
print(survival_counts)

# Анализ выживаемости по полу
sex_survival_counts = df.groupby('Sex')['Survived'].value_counts().unstack()
print("\nВыживаемость по полу:")
print(sex_survival_counts)

# Анализ выживаемости по классам (Pclass)
class_survival_counts = df.groupby('Pclass')['Survived'].value_counts().unstack()
print("\nВыживаемость по классам:")
print(class_survival_counts)

# Анализ количества несовершеннолетних на борту (Age)
minor_counts = df[df['Age'] < 18]['Survived'].value_counts()
print("\nКоличество несовершеннолетних на борту.:")
print(minor_counts)

# Создаем подграфики
fig, axs = plt.subplots(2, 2, figsize=(15, 9))

# Визуализация количества выживших и не выживших
axs[0, 0].bar(survival_counts.index, survival_counts.values, color=['red', 'green'])
axs[0, 0].set_title('Количество выживших и не выживших на Титанике')
axs[0, 0].set_xlabel('Выживание')
axs[0, 0].set_ylabel('Количество пассажиров')
axs[0, 0].set_xticks([0, 1])
axs[0, 0].set_xticklabels(['Не выжил', 'Выжил'], rotation=0)

# Анализ выживаемости по полу
sex_survival_counts = df.groupby('Sex')['Survived'].value_counts().unstack()
sex_survival_counts.plot(kind='bar', stacked=True, ax=axs[0, 1], color=['lightblue', 'salmon'])
axs[0, 1].set_title('Выживаемость по полу')
axs[0, 1].set_xlabel('Пол')
axs[0, 1].set_ylabel('Количество пассажиров')
axs[0, 1].set_xticks([0, 1])
axs[0, 1].set_xticklabels(['Мужчины', 'Женщины'], rotation=0)
axs[0, 1].legend(['Не выжил', 'Выжил'])

# Анализ выживаемости по классам (Pclass)
class_survival_counts = df.groupby('Pclass')['Survived'].value_counts().unstack()
class_survival_counts.plot(kind='bar', stacked=True, ax=axs[1, 0], color=['lightcoral', 'lightgreen'])
axs[1, 0].set_title('Выживаемость по классу')
axs[1, 0].set_xlabel('Класс')
axs[1, 0].set_ylabel('Количество пассажиров')
axs[1, 0].set_xticks([0, 1, 2])
axs[1, 0].set_xticklabels(['1-й класс', '2-й класс', '3-й класс'], rotation=0)
axs[1, 0].legend(['Не выжил', 'Выжил'])

# Анализ выживаемости среди несовершеннолетних (Age)
axs[1, 1].pie(minor_counts, labels=['Не выжил', 'Выжил'], autopct='%.1f', colors=['lightcoral', 'lightgreen'])
axs[1, 1].set_title('Выживаемость среди несовершеннолетних')

# Показать все графики
plt.tight_layout()  # Для автоматической настройки отступов
plt.show()

'''
Matplotlib — это одна из самых популярных библиотек для визуализации данных в Python. 
Она предоставляет широкий набор инструментов для создания статичных, анимированных и интерактивных графиков. 

Pandas — это библиотека для анализа и манипуляции данными, предоставляющая мощные инструменты для работы с структурированными данными. 

Взаимодействие Matplotlib и Pandas

Matplotlib и Pandas часто используются вместе для анализа данных и их визуализации. 
Pandas позволяет быстро и легко манипулировать данными, а Matplotlib предоставляет мощные инструменты для их наглядного представления. 
Это делает их отличным выбором для анализа данных в области науки, бизнеса и многих других областей.
'''
