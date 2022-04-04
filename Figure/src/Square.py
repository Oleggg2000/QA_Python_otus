from main import Figure


class Square(Figure):
    def __init__(self, name, side):
        if side > 0:
            super().__init__(name)
            self.side = side
        else:
            raise ValueError

    @property
    def area(self):
        return self.side ** 2

    @property
    def perimeter(self):
        return self.side * 4
