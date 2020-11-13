from Shape import Shape


class Circle(Shape):
    def __init__(self,shape_name, radius):
        self.shape_name = shape_name
        self.radius = radius

    def area(self):
        return 3.14*float(self.radius)*float(self.radius)

    def perimeter(self):
        return 2.0*3.14*float(self.radius)
