# Домашнее задание по уроку "Различие атрибутов класса и экземпляра"

class Building:
    total = 1

    def __init__(self, total):
        self.total = total


for i in range(40):
    bld = Building(i + 1)
    print(f'Объект {bld} № {bld.total} в классе "Building"')
