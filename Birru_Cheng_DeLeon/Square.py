from Shape import Shape
from turtle import Turtle, delay


class Square(Shape):
    """
    The Square class is a child class of Shape.
    It provides provide specific implementations of area, perimeter, and graphics of squares.
    """

    def __init__(self, name: str, side_length: float) -> Shape:
        """Creates a square with the given name and side length."""
        Shape.__init__(self, name)
        self.__side_length = side_length
        self.angle = 90
        self.validation()

    def validation(self):
        """Ensures the square can be made by checking that the given side lenght is positive."""
        if self.__side_length <= 0:
            raise ValueError("the input radius must be a positive number")

    def perimeter(self):
        """Calculates and returns the perimeter of the square."""
        return self.__side_length * 4

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__side_length ** 2

    def __str__(self):
        """Returns the name of the square."""
        return self.name

    def draw(self):
        """Prints the name, area, and perimeter of the square."""
        print(f"{self.name}, area: {self.area()}, perimeter: {self.perimeter()}")

    def draw_graphic(self):
        """Creates a graphic of the square."""
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
