import math
from Shape import Shape
from turtle import Turtle, delay


class Circle(Shape):
    """
    The Circle class is a child class of Shape.
    It provides provide specific implementations of area, perimeter, and graphics of circles.
    """

    def __init__(self, name: str, radius: float):
        """Creates a Circle with a name and radius."""

        Shape.__init__(self, name)
        self.__radius = radius
        self.validation()

    def validation(self):
        """
        Ensures that the circle can be constructed
        by raising an error when a negative number is given for the radius.
        """

        if self.__radius <= 0:
            raise ValueError("the input radius must be a positive number")

    def area(self):
        """Calculates and returns the area of the circle using the radius."""
        return math.pi*(self.__radius**2)

    def perimeter(self):
        """Calculates and returns the perimeter of the circle using the radius."""

        return 2*math.pi*self.__radius

    def __str__(self):
        """Returns the circle name."""

        return self.name

    def draw_graphic(self):
        """Creates a graphic of the circle."""

        t = Turtle()
        text = Turtle()
        s = t.getscreen()
        s.bgcolor("orange")
        count = 0
        while count < 1:
            text.penup()
            text.setposition(-100, -100)
            text.pencolor("purple")
            text.write("{}, area: {:.2f}, perimeter: {:.2f}".format(self.name, self.area(), self.perimeter()), align="left",
                    font=("Arial", 20, "bold"))
            t.goto(0, 0)
            t.pen(pencolor="purple", fillcolor="green", pensize=6, speed=20)
            t.fillcolor("red")
            t.begin_fill()
            t.pendown()
            t.circle(self.__radius)
            t.end_fill()
            delay(30)
            t.clear()
            t.reset()
            text.clear()
            text.reset()
            count += 1
