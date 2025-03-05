# Домашнее задание по уроку "Специальные методы классов"

class House:
    def __init__(self, numberOfFloors):
        self.numberOfFloors = numberOfFloors

    def __setNewNumberOfFloors__(self, floors):
        self.numberOfFloors = floors
        print(f'Этажей стало {self.numberOfFloors}')


perem = House(30)
print(f'Этажей было {perem.numberOfFloors}')
perem = perem.__setNewNumberOfFloors__(12)

