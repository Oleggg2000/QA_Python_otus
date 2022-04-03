from main import Figure


class Rectangle(Figure):
    def __init__(self, name, side1, side2):
        super().__init__(name)
        self.side1 = side1
        self.side2 = side2

    @property
    def area(self):
        return self.side1 * self.side2

    @property
    def perimeter(self):
        return self.side1 * 2 + self.side2 * 2
