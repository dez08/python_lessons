import os
import pandas as pd
from prettytable import PrettyTable


class PriceAnalyzer:
    def __init__(self, input_folder="prise_list", output_folder="output"):
        """Инициализация класса PriceAnalyzer."""
        self.input_folder = input_folder
        self.output_folder = output_folder
        self.data = pd.DataFrame()
        self.filtered_data = pd.DataFrame()
        self.last_search = None

    def load_prices(self):
        """Загружает данные из файлов в указанной папке с "price" в названии."""

        price_files = [f for f in os.listdir(self.input_folder) if "price" in f.lower()]
        all_data = []

        # Обрабатываем каждый файл из списка
        for file in price_files:
            file_path = os.path.join(self.input_folder, file)
            try:
                df = pd.read_csv(file_path)
                # Нормализация названий колонок
                columns_map = {
                    "название": "name",
                    "продукт": "name",
                    "товар": "name",
                    "наименование": "name",
                    "цена": "price",
                    "розница": "price",
                    "фасовка": "weight",
                    "масса": "weight",
                    "вес": "weight",
                }
                # Приведение к нижнему регистру и переименование
                df = df.rename(columns=str.lower).rename(columns=columns_map)

                # Проверяем, что в файле есть нужные колонки
                if {"name", "price", "weight"}.issubset(df.columns):
                    # Оставляем только нужные столбцы
                    df = df[["name", "price", "weight"]]
                    # Добавляем столбец с названием файла
                    df["file"] = file
                    # Удаляем строки с пустыми значениями
                    df = df.dropna(subset=["name", "price", "weight"])
                    # Вычисляем цену за килограмм
                    df["price_per_kg"] = df["price"] / df["weight"]
                    # Добавляем номер строки
                    df.reset_index(drop=True, inplace=True)
                    df.index += 1  # Начинаем индексацию с 1
                    # Переименовываем столбцы
                    df.columns = ["Наименование", "Цена", "Вес", "Файл", "Цена_за_кг"]
                    # Добавляем данные в общий список
                    all_data.append(df)
            except Exception as e:
                # Обрабатываем ошибку при чтении или обработке файла
                print(f"Ошибка при обработке файла {file}: {e}")

        # Объединяем все данные в одну таблицу
        if all_data:
            self.data = pd.concat(all_data, ignore_index=True)

    def export_to_html(self, filename=None, data=None):
        """Экспортирует данные в HTML файл в папке output."""
        if filename is None:
            filename = f"filtered_output_{self.last_search}.html"
        # Если не переданы данные, берём все загруженные данные
        if data is None:
            data = self.data

        if data.empty:
            print("Нет данных для экспорта.")
            return

        # Создаём папку output
        os.makedirs(self.output_folder, exist_ok=True)
        # Путь к итоговому файлу
        output_path = os.path.join(self.output_folder, filename)

        # Округляем значения
        # data["Цена"] = data["Цена"].round(2)
        data["Вес"] = data["Вес"].round(3)
        data["Цена_за_кг"] = data["Цена_за_кг"].round(2)

        # Сортируем данные по цене за кг
        data.sort_values(by="Цена_за_кг", inplace=True)

        # Сбрасываем индекс, чтобы он стал обычным столбцом
        data.reset_index(drop=True, inplace=True)

        # Добавляем колонку с номерами строк
        data.index += 1  # Начинаем индексацию с 1
        data.index.name = "№"  # Название индекса

        # Создаем новый DataFrame с номерами строк в качестве первого столбца
        data_with_index = data.reset_index()
        data_with_index.rename(columns={"index": "№"}, inplace=True)

        # Экспортируем с индексом
        data_with_index.to_html(output_path, index=False, escape=False)

        print(f"Данные экспортированы в {output_path}")

    def find_text(self, text):
        """
        Ищет текст в названиях продуктов и возвращает отсортированный список найденных позиций.
        """
        self.last_search = text
        if self.data.empty:
            print("Данные не загружены.")
            return pd.DataFrame()

        # Фильтруем данные в столбце "Наименование"
        self.filtered_data = self.data[self.data["Наименование"].str.contains(text, case=False, na=False)]

        # Проверяем, есть ли найденные данные
        if self.filtered_data.empty:
            print("Данные не найдены. Повторите поиск.")
            return pd.DataFrame()

        # Сортируем по цене за кг
        self.filtered_data = self.filtered_data.sort_values(by="Цена_за_кг")

        # Создаём таблицу для вывода в консоль
        table = PrettyTable()
        table.field_names = ["№", "Наименование", "Цена", "Вес", "Файл", "Цена_за_кг"]
        for i, row in enumerate(self.filtered_data.itertuples(), start=1):
            table.add_row([i, row.Наименование, f"{row.Цена:.2f}", f"{row.Вес:.2f}", row.Файл, f"{row.Цена_за_кг:.2f}"])

        # Выводим таблицу в консоль
        print(table)
        return self.filtered_data


if __name__ == "__main__":
    analyzer = PriceAnalyzer()
    analyzer.load_prices()

    # Основной цикл для поиска и экспорта
    while True:
        query = input("Введите текст для поиска \n"
                      "'export' для экспорта последнего результата поиска\n"
                      "'exit' для выхода\n"
                      ">:")
        # Проверяем что ввел пользователь
        if query.lower() == "exit":
            print("Работа завершена.")
            # Экспорт всех данных
            analyzer.export_to_html(filename="output.html")
            break
        elif query.lower() == "export":
            # Проверяем, есть ли результаты последнего поиска
            if analyzer.filtered_data.empty:
                print("Нет данных для экспорта. Сначала выполните поиск.")
            else:
                analyzer.export_to_html(data=analyzer.filtered_data)
        else:
            # Ищем текст в данных
            analyzer.find_text(query)
