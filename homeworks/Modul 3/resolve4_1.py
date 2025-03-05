# Задание "Раз, два, три, четыре, пять .... Это не всё?"

def simple_type(exam):
    global count_num, count_str

    if type(exam) == int:
        count_num += exam
    elif type(exam) == str:
        count_str += len(exam)




def list_type(list_):
    global count_num, count_str
    for i in list_:
        if type(i) == int or type(i) == str:
            simple_type(i)
        elif type(i) == list:
            list_type(i)
        elif type(i) == dict:
            dict_type(i)
        elif type(i) == tuple:
            tuple_type(i)
        elif type(i) == set:
            set_type(i)


def dict_type(dict_):
    global count_num, count_str
    for i in dict_:
        simple_type(i)
        simple_type(dict_[i])


def tuple_type(tupel_):
    global count_num, count_str
    for i in tupel_:
        if type(i) == int or type(i) == str:
            simple_type(i)
        elif type(i) == list:
            list_type(i)
        elif type(i) == dict:
            dict_type(i)
        elif type(i) == tuple:
            tuple_type(i)
        elif type(i) == set:
            set_type(i)


def set_type(set_):
    global count_num, count_str
    for i in set_:
        if type(i) == int or type(i) == str:
            simple_type(i)
        elif type(i) == list:
            list_type(i)
        elif type(i) == dict:
            dict_type(i)
        elif type(i) == tuple:
            tuple_type(i)
        elif type(i) == set:
            set_type(i)


def parsing(structure):
    global count_num, count_str

    for i in structure:
        simple_type(i)
        if type(i) == list:
            for j in i:
                if type(j) == int or type(j) == str:
                    simple_type(j)
                elif type(j) == list:
                    list_type(j)
                elif type(j) == dict:
                    dict_type(j)
        elif type(i) == dict:
            dict_type(i)
        elif type(i) == tuple:
            tuple_type(i)

    return count_str, count_num


count_num = 0
count_str = 0

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
print(parsing(data_structure))
print(count_num + count_str)
