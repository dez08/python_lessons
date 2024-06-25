# Домашнее задание по уроку "Различие атрибутов класса и экземпляра"

class Building:
    total = 1

    def __init__(self, total):
        self.total = total


for i in range(40):
    locals()['bld' + str(i)] = Building(i + 1)
    print(f'Объект {locals()['bld' + str(i)]} № {locals()['bld' + str(i)].total} в классе "Building"')
