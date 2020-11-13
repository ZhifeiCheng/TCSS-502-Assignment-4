from Shape import Shape


class Triangle(Shape):
    def __init__(self, shape_name, a, b, c):
        self.shape_name = shape_name
        self.a = float(a)
        self.b = float(b)
        self.c = float(c)

    def area(self):
        s = (self.a + self.b + self.c)/2.0
        return (s*(s-self.a)*(s-self.b)*(s-self.c))**0.5

    def perimeter(self):
        return self.a + self.b + self.c
