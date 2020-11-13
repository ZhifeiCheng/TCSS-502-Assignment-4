from Shape import Shape


class Square(Shape):
    def __init__(self, shape_name, side):
        self.shape_name = shape_name
        self.side = side

    def area(self):
        return float(self.side)*float(self.side)

    def perimeter(self):
        return 4.0*float(self.side)