# Задача "Нули ничто, отрицание недопустимо!"
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
len_my_list = len(my_list)
count = 0

while count <= len_my_list:
    if my_list[count] == 0:
        count = count + 1
        continue
    elif my_list[count] > 0:
        print(my_list[count])
    else:
        break
    count = count + 1