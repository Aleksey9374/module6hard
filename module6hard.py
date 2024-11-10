import math
class Figure:
    sides_count = 0 # количество сторон
    def __init__(self, color, *sides):
        self.__color = list(color)  # список цветов в формате RGB
        self.__sides = list(sides) # список сторон (целые числа)
        self.filled = True # закрашенный, bool

    def get_color(self): # возвращает список RGB цветов
       return self.__color

    def __is_valid_color(self, r, g, b): # проверяет корректность цвета: все знач целые числа в диап от [0 до 255]
        return all (isinstance(color, int) and 0 <= color <= 255 for color in (r, g, b))

    def set_color(self, r, g, b): # изменяет атрибут __color при корректных значениях
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *args): # проверка сторон
        for side in args:
            if  isinstance(side, int) and side > 0 and len(args) == self.sides_count:
                return True
            else:
                return False

    def __len__(self): # возвращает периметр фигуры
        return sum(self.__sides)

    def set_sides(self, *new_sides): # принимает новые стороны, если они проходят проверку
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)

    def get_sides(self):  # возвращает значение списка сторон
        return self.__sides

class Circle(Figure):
    sides_count = 1
    def __init__(self, color, *sides): # атрибут цвета наследуем напрямую, стороны через проверку кол-ва сторон
        self.sides = sides[0] if len(sides) == 1 else 1
        super().__init__(color, self.sides)
        self.__radius = self.sides / (2 * math.pi)

    def get_square(self): #возвращает площадь круга
        return math.pi * self.__radius ** 2

class Triangle(Figure):
    sides_count = 3
    def __init__(self, color, *sides):
        self.sides = sides if len(sides) == 3 else [1, 1, 1]
        super().__init__(color, *self.sides)

    def get_square(self):  # возвращает площадь треугольника
        a, b, c = self.sides
        p = (a + b + c) / 2
        s = (p * (p - a) * (p - b) * (p - c)) ** 0.5
        return s

class Cube(Figure):
    sides_count = 12
    def __init__(self, color, *sides):
        side = sides[0] if len(sides) == 1 else 1
        super().__init__(color, *[side] * 12)

    def get_volume(self):  # возвращает объём куба
        return super().get_sides()[0] ** 3

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
