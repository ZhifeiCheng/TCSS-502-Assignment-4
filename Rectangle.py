from Shape import Shape


class Rectangle(Shape):
    def __init__(self, shape_name, length, breadth):
        self.shape_name = shape_name
        self.length = length
        self.breadth = breadth

    def area(self):
        return float(self.length)*float(self.breadth)

    def perimeter(self):
        return 2.0*(float(self.length)+float(self.breadth))