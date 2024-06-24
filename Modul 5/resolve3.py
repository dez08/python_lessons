# Домашнее задание по уроку "Перегрузка операторов"

class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = int(numberOfFloors)
        self.buildingType = str(buildingType)

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType


build_1 = Building(30, 'ЖК Олимпийский')
build_2 = Building(20, 'ЖК Олимпийский')
build_3 = Building(30, 'ЖК Олимпийский')
build_4 = Building(30, 'ЖК Утро')

print(build_1 == build_2)
print(build_2 == build_3)
print(build_1 == build_3)
print(build_1 == build_4)
