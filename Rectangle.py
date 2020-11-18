from Shape import Shape
from turtle import Turtle, delay


class Rectangle(Shape):
    def __init__(self, name, side_1_length, side_2_length):
        Shape.__init__(self, name)
        self.__side_1_length = side_1_length
        self.__side_2_length = side_2_length
        self.angle = 90
        self.validation()

    def validation(self):
        if self.__side_1_length <= 0 or self.__side_2_length <= 0:
            raise ValueError("the input radius must be a positive number")

    def perimeter(self):
        return (self.__side_1_length + self.__side_2_length)*2

    def area(self):
        return self.__side_1_length * self.__side_2_length

    def __str__(self):
        return self.name

    def draw(self):
        print(f"name_of_shape {self.name}, area: {self.area()}, perimeter: {self.perimeter()}")

    def draw_graphic(self):
        t = Turtle()
        s = t.getscreen()
        s.bgcolor("orange")
        count = 0
        while count < 1:
            t.write("name_of_shape {}, area: {}, perimeter: {}".format(self.name, self.area(), self.perimeter()))
            t.pen(pencolor="purple", fillcolor="green", pensize=6, speed=800)
            for edge in range(2):
                t.forward(self.__side_1_length)
                delay(100)
                t.left(self.angle)
                t.forward(self.__side_2_length)
                t.left(self.angle)
                delay(100)
            t.clear()
            t.reset()
            count += 1