# Задача "Записать и запомнить":

def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    strings_position = {}
    ch = 1
    for i in strings:
        strings_position[ch, file.tell()] = i
        file.write(f'{i}\n')
        ch += 1
    return strings_position

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)