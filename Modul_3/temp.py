# Задание "Раз, два, три, четыре, пять .... Это не всё?"

def calculate_structure_sum(structure):
    global count_num, count_str

    if isinstance(structure, int):
        count_num += structure
    elif isinstance(structure, str):
        count_str += len(structure)
    else:
        for i in structure:
            if isinstance(i, str):
                calculate_structure_sum(i)
            elif isinstance(i, int):
                calculate_structure_sum(i)
            elif isinstance(i, list):
                for j in i:
                    calculate_structure_sum(j)
            elif isinstance(i, tuple):
                for j in i:
                    calculate_structure_sum(j)
            elif isinstance(i, dict):
                for j in i:
                    calculate_structure_sum(j)
                    calculate_structure_sum(i[j])
            elif isinstance(i, set):
                for j in i:
                    calculate_structure_sum(j)
    print(count_str, count_num, structure)
    return count_str + count_num


count_num = 0
count_str = 0


data_structure = [
    # [1, 2, 3],
    # {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    # "Hello",
    # ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print(calculate_structure_sum(data_structure))
print(count_str, count_num)

