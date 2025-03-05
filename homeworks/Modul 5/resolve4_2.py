# Домашнее задание по уроку "Различие атрибутов класса и экземпляра"

class Building:
    total = 1

    def __init__(self, total):
        self.total = total


for i in range(1, 40 + 1):
    locals()['bld' + str(i)] = Building(i)
    print(f'Объект {locals()['bld' + str(i)]} № {locals()['bld' + str(i)].total} в классе "Building"')
