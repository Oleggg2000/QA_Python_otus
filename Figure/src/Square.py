from main import Figure


class Square(Figure):
    def __init__(self, name, side):
        super().__init__(name)
        self.side = side

    @property
    def area(self):
        return self.side ** 2

    @property
    def periment(self):
        return self.side * 4
