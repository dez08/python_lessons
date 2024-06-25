class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print('Такого этажа не существует.')
        else:
            for i in range(1, new_floor + 1):
                print(i)
                import time
                time.sleep(0.5)
            print(f'Вы прибыли на {new_floor} этаж {self.name}.')


house1 = House('ЖК Эльбрус', 30)


house1.go_to(int(input('Добрый день. '
                       '\nВведите номер этажа: ')))
