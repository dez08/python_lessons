# Домашнее задание по теме "Создание потоков".
# Задача "Потоковая запись в файлы":

import time
from datetime import datetime
from threading import Thread


def wite_words(word_count, file_name):
    with open(file_name, 'a') as file:
        for i in range(word_count):
            file.write(f'Какое-то слово № {i + 1}')
            time.sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')


time_start = datetime.now()
print('Начата запись в файлы с помощью вызова функций.')
wite_words(10, 'example1.txt')
wite_words(30, 'example2.txt')
wite_words(200, 'example3.txt')
wite_words(100, 'example4.txt')
time_end = datetime.now()
time_res = time_end - time_start
print(f'При вызове функций времени заняло: {time_res}.')
print()

time_start = datetime.now()
print('Начата запись в файлы с помощью потоков.')
thr_1 = Thread(target=wite_words, args=(10, 'example5.txt'))
thr_2 = Thread(target=wite_words, args=(30, 'example6.txt'))
thr_3 = Thread(target=wite_words, args=(200, 'example7.txt'))
thr_4 = Thread(target=wite_words, args=(100, 'example8.txt'))

thr_1.start()
thr_2.start()
thr_3.start()
thr_4.start()

thr_1.join()
thr_2.join()
thr_3.join()
thr_4.join()
time_end = datetime.now()
time_res = time_end - time_start
print(f'При работе с потоками времени заняло: {time_res}.')