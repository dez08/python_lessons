# Задача "Распаковка"
print('\n1.Функция с параметрами по умолчанию:\n')

def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params()
print_params(1, 2 ,3)
print_params(1, 2)
print_params(b=25)
print_params(c=[1, 2, 3])

print('\n2.Распаковка параметров:\n')

values_list = [1, 2, 3]
values_dict = {'a': 1, 'b': 2, 'c': 3}
print_params(*values_list)
print_params(**values_dict)

print('\n3.Распаковка + отдельные параметры:\n')

values_list_2 = [54.32, 'привет']
print_params(*values_list_2, 42)