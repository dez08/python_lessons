# Практическое задание по теме: "Словари и множества"
my_dict = {'Vladislav':1990, 'Diana':1993, 'Roman':2023}
print(my_dict)

print(my_dict.get('Vladislav'))
print(my_dict.get('Oksana'))

my_dict.update({'Anatoly':1980, 'Oleg':2010})
print(my_dict.pop('Oleg'), '- Значение удаленной пары')
print(my_dict)

my_set = {1, 1, 1, 2, 3, 1.2, 'str'}
print(my_set)

my_set.update([9, 12])
print(my_set)
my_set.discard(9)
print(my_set)