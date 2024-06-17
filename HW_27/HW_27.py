class Figure:

    def __init__(self, fig='Абстрактная'):
        self.fig = fig

    def __int__(self):
        return 1

    def __str__(self):
        return self.fig

    def area_fig(self):
        return f'Фигура {self.__str__()}. Площадь {self.__int__()}'


class Circle(Figure):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius
        self.fig = 'круг'

    def __int__(self):
        square = int(round(3.14 * self.radius ** 2, 0))
        return square

    def __str__(self):
        return 'Круг'


class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        super().__init__()
        self.side_a = side_a
        self.side_b = side_b

    def __int__(self):
        return self.side_a * self.side_b

    def __str__(self):
        return 'Прямоугольник'


class RightTriangle(Figure):
    def __init__(self, side_a, side_b):
        super().__init__()
        self.side_a = side_a
        self.side_b = side_b

    def __str__(self):
        return 'Прямоугольный Треугольник'

    def __int__(self):
        square = int(round(((self.side_a ** 2 + self.side_b ** 2) ** 0.5), 0))
        return square


class Trapezoid(Figure):
    def __init__(self, top, base, apex):
        super().__init__()
        self.top = top
        self.base = base
        self.apex = apex

    def __str__(self):
        return 'Трапеция'

    def __int__(self):
        square = int(round((self.top + self.base) / 2 * self.apex, 0))
        return square


fig_1 = Figure()
fig_2 = Circle(5)
fig_3 = Rectangle(2, 3)
fig_4 = RightTriangle(3, 4)
fig_5 = Trapezoid(5, 7, 4)

print(fig_1.area_fig())
print(fig_2.area_fig())
print(fig_3.area_fig())
print(fig_4.area_fig())
print(fig_5.area_fig())
