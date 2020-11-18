import math
from Shape import Shape
from turtle import Turtle, delay


class Circle(Shape):
    def __init__(self, name: str, radius: float):
        Shape.__init__(self, name)
        self.__radius = radius
        self.validation()

    def validation(self):
        if self.__radius <= 0:
            raise ValueError("the input radius must be a positive number")

    def area(self):
        return math.pi*math.sqrt(self.__radius)

    def __eq__(self, other):
        if isinstance(other, Circle):
            return False
        return super().__eq__(other)

    def perimeter(self):
        return 2*math.pi*self.__radius

    def __str__(self):
        return self.name

    # def draw(self):
    #     print(f"name_of_shape {self.name}, area: {self.area}, perimeter: {self.perimeter}")

    def draw_graphic(self):
        t = Turtle()
        s = t.getscreen()
        s.bgcolor("orange")
        count = 0
        while count < 1:
            t.write("name_of_shape {}, area: {}, perimeter: {}".format(self.name, self.area(), self.perimeter()))
            t.goto(0, 0)
            t.pen(pencolor="purple", fillcolor="green", pensize=6, speed=20)
            t.fillcolor("red")
            t.begin_fill()
            t.circle(self.__radius)
            t.end_fill()
            delay(20)
            t.clear()
            count += 1
