# Задание "Они все так похожи":
from math import pi, sqrt


class Figure:
    def __init__(self, __color, __sides):
        self.__sides = __sides
        self.__color = __color
        self.filled = True

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        if r in range(256) and g in range(256) and b in range(256):
            return True
        return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *args):
        result = False
        if len(args) == self.sides_count:
            for i in args:
                if type(i) is int and i > 0:
                    result = True
                else:
                    break
        return result

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.sides_count > 1:
            a = self.__sides
            b = []
            for _ in range(self.sides_count):
                b.append(a)
            self.__sides = b
        else:
            if self.__is_valid_sides(*new_sides):
                self.__sides = [*new_sides]


class Circle(Figure):
    def __init__(self, __color, __sides):
        super().__init__(__color, __sides)
        self.sides_count = 1
        self.__radius = __sides / (2 * pi)

    def get_square(self):
        return pi * self.__radius ** 2


class Triangle(Figure):
    def __init__(self, __color, __sides):
        super().__init__(__color, __sides)
        self.sides_count = 3
        a = __sides
        b = []
        for _ in range(self.sides_count):
            b.append(a)
        self.__sides = b
        p = sum(self.__sides) / 2
        self.__height = (2 * sqrt(p * (p - self.__sides[0]) * (p - self.__sides[1]) * (p - self.__sides[2]))) / \
                        self.__sides[0]

    def get_square(self):
        return 0.5 * self.__sides[0] * self.__height


class Cube(Figure):
    def __init__(self, __color, __sides):
        super().__init__(__color, __sides)
        self.sides_count = 12

    def get_volume(self):
        return self._Figure__sides[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)




# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
