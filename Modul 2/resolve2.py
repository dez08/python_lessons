# Задача "Все ли равны?"
print('Введите три целех числа.')
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))

if a == b == c:
    print('Равных чисел 3')
elif a == b or b == c or a == c:
    print('Равных чисел 2')
else:
    print('Равных чисел 0')