class Figure:
    def __init__(self, name):
        self.name = name

    def add_area(self, figure):
        try:
            return self.area + figure.area
        except:
            raise ValueError("Impossible to sum areas! Figure isn't valid!")
