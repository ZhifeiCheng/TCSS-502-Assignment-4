from Shape import Shape
from turtle import Turtle, delay


class Square(Shape):
    def __init__(self, name: str, side_length: float) -> Shape:
        Shape.__init__(self, name)
        self.__side_length = side_length
        self.angle = 90
        self.validation()

    def validation(self):
        if self.__side_length <= 0:
            raise ValueError("the input radius must be a positive number")

    def perimeter(self):
        return self.__side_length * 4

    def area(self):
        return self.__side_length ** 2

    def __str__(self):
        return self.name

    def draw(self):
        print(f"{self.name}, area: {self.area()}, perimeter: {self.perimeter()}")

    def draw_graphic(self):
        t = Turtle()
        text = Turtle()
        s = t.getscreen()
        s.bgcolor("purple")
        count = 0
        while count < 1:
            text.penup()
            text.setposition(-100, -100)
            text.pencolor("yellow")
            text.write("{}, area: {:.2f}, perimeter: {:.2f}".format(self.name, self.area(), self.perimeter()), align="left",
                    font=("Arial", 20, "bold"))
            t.pen(pencolor="yellow", fillcolor="green", pensize=6, speed=800)
            for edge in range(4):
                t.fillcolor("red")
                t.begin_fill()
                t.forward(self.__side_length)
                delay(50)
                t.left(self.angle)
                t.end_fill()
            t.clear()
            t.reset()
            text.clear()
            text.reset()
            count += 1
