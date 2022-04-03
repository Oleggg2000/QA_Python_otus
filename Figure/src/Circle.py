from main import Figure
from math import pi


class Circle(Figure):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    @property
    def area(self):
        return pi * self.radius ** 2

    @property
    def perimeter(self):
        return 2 * pi * self.radius
