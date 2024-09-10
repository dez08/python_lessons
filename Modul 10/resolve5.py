# Домашнее задание по теме "Многопроцессное программирование"

import multiprocessing, datetime


def read_info(name):
    all_data = []
    with open(name) as file:
        while file.readline():
            all_data.append(file.readline())


file_names = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']


def linear():
    start = datetime.datetime.now()
    for file in file_names:
        read_info(file)
    end = datetime.datetime.now()
    print(f'Время выполнения линейного метода: {end - start}')


def multiprocess():
    with multiprocessing.Pool(processes=4) as pool:
        start = datetime.datetime.now()
        pool.map(read_info, file_names)
        end = datetime.datetime.now()
        print(f'Время выполнения многопроцессорного метода: {end - start}')


if __name__ == '__main__':
    linear()
    multiprocess()