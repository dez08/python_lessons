grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students = list(students)
students.sort()
dict_ = {}

for a in range(len(grades)):
    GPA = sum(grades[a]) / len(grades[a])
    dict_.update({students[a]:GPA})
print(dict_)
