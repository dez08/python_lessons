# Задание "Раз, два, три, четыре, пять .... Это не всё?"

def calculate_structure_sum(structure):
    global count_num, count_str

    if isinstance(structure, int):
        count_num += structure
    elif isinstance(structure, str):
        count_str += len(structure)
    elif isinstance(structure, dict):
        for i in structure:
            calculate_structure_sum(i)
            calculate_structure_sum(structure[i])
    elif isinstance(structure, (list, tuple, set)):
        for i in structure:
            calculate_structure_sum(i)
    return count_str + count_num


count_num = 0
count_str = 0


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print('Сумма всех значний:', calculate_structure_sum(data_structure))
print('Сумма длин строковых значений:', count_str,
      '\nСумма числовых значений:', count_num)
