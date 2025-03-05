# Практическое задание по теме: "Неизменяемые и изменяемые объекты. Кортежи и списки"
immutable_var = [1, 'str', 3.2], 2, 'str'
print(immutable_var)

# immutable_var[1] = 3
# print(immutable_var)
# Изменить элемент кортежа нельзя, так как кортеж относится к неизменяемым типам данных.

immutable_var[0][0] = 2
print(immutable_var)

mutable_list = [1, 2, 3.2, 'str']
print(mutable_list)
mutable_list[0] = 10
print(mutable_list)