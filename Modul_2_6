import random

list_1 = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
list_3 = []
list_4 = []


def is_number(answer):
    try:
        int(answer)
        return True
    except ValueError:
        return False


def cipher(k):
    list_3.clear()
    list_4.clear()
    for i in list_2:
        for j in list_2:
            if k % (i + j) == 0:
                if f'{j} + {i}' in list_3 or i == j:
                    continue
                else:
                    list_3.append(f'{i} + {j}')
                    list_4.extend([i, j])


while 1 < 10:

    answer = input('Добрый день, пользователь!\n'
                   'Введите Ваш вариант использования программы:\n'
                   '"Рандом" - если вам нужно вывести пароль на рандомное число от 3 до 20.\n'
                   '"Все" - если вам нужно вывести все пароли на числа от 3 до 20.\n'
                   'Либо введите число от 3 до 20 для получения пароля.\n'
                   'Для выхода из программы введите "Выход"\n'
                   'Поле ввода: ')

    answer_type = is_number(answer)

    if answer_type == True and 3 <= int(answer) <= 20:
        cipher(int(answer))
        print()
        print(f'Указанное число: {answer} - Пароль:', *list_4)
        print()
    else:
        if answer == 'Рандом' or answer == 'рандом':
            i = random.choice(list_1)
            cipher(i)
            print()
            print(f'Рандомное число: {i} - Пароль', *list_4)
            print()
        elif answer == 'Все' or answer == 'все':
            for i in list_1:
                cipher(i)
                print()
                print(f'Число: {i} - Пароль:', *list_4)
                print()
        elif answer == 'Выход' or answer == 'выход':
            print()
            print('Завершение работы программы.')
            print()
            break
        else:
            print()
            print('Введено неверное значение!')
            print()
