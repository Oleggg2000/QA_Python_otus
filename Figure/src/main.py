class Figure:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        try:
            return self.area + other.area
        except:
            raise ValueError("Impossible to sum areas! Figure isn't valid!")
