# Задача "Найдёт везде":

class WordsFinder:
    def __init__(self, *args):
        self.file_names = args

    def get_all_words(self):
        all_words = {}
        list_ = [',', '.', '=', '!', '?', ';', ':', ' - ', ' -', '- ', ' — ']
        # добавил разное положение дефиса, для удаления его в начале строки, в конце строки и в середине как разделитель
        # добавил спец символ — так как он есть в дополнительных файлах для проверки [ALT + 0151] = —
        for file in self.file_names:
            with open(file, encoding='utf-8') as f1:
                b = f1.read().lower()
                for i in list_:
                    b = b.replace(i, '')
                all_words[file] = b.split()
                # второй вариант использовать import re и re.sub(r'[^\w\s]')
                # но тогда удаляются все ' из сокращений и - из слов в которых они должны быть

        return all_words

    def find(self, word):
        result = {}
        for file in self.file_names:
            with open(file, encoding='utf-8') as f1:
                ch = 1
                for i in f1.read().split():
                    if word.lower() == i.lower():
                        break
                    ch += 1
            result[file] = ch
        return result

    def count(self, word):
        result = {}
        for file in self.file_names:
            with open(file, encoding='utf-8') as f1:
                ch = 0
                for i in f1.read().split():
                    if word.lower() == i.lower():
                        ch += 1
            result[file] = ch
        return result

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

# # Дополнительная проверка для нескольких файлов
# finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
#                       'Rudyard Kipling - If.txt',
#                       'Mother Goose - Monday’s Child.txt')
# print(finder1.get_all_words())
# print(finder1.find('the'))
# print(finder1.count('the'))