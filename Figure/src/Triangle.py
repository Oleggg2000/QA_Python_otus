from main import Figure
from math import sqrt


class Triangle(Figure):
    def __init__(self, name, side1, side2, side3):
        if (side1 < side2 + side3) and (side2 < side1 + side3) and (side3 < side2 + side1):
            super().__init__(name)
            self.side1 = side1
            self.side2 = side2
            self.side3 = side3
        else:
            raise ValueError

    @property
    def area(self):
        half_perimeter = self.perimeter / 2
        return sqrt(half_perimeter * (half_perimeter - self.side1) *
                    (half_perimeter - self.side2) * (half_perimeter - self.side3))

    @property
    def perimeter(self):
        return self.side1 + self.side2 + self.side3
