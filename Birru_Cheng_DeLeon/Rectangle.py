from turtle import Turtle, delay

from Shape import Shape


class Rectangle(Shape):
    """
    The Rectangle class is a child class of Shape.
    It provides provide specific implementations of area, perimeter, and graphics of rectangles.
    """

    def __init__(self, name, side_1_length, side_2_length):
        """Creates a Rectangle with a name, two side lengths, and an angle of 90."""

        Shape.__init__(self, name)
        self.__side_1_length = side_1_length
        self.__side_2_length = side_2_length
        self.angle = 90
        self.validation()

    def validation(self):
        """
        Ensures that the rectangle can be constructed
        by raising an error when a negative number is given for either side length.
        """

        if self.__side_1_length <= 0 or self.__side_2_length <= 0:
            raise ValueError("the input radius must be a positive number")

    def perimeter(self):
        """Calculates and returns the perimeter of the rectangle using the two side lengths."""

        return (self.__side_1_length + self.__side_2_length)*2

    def area(self):
        """Calculates and returns the area of the rectangle using the two side lengths."""

        return self.__side_1_length * self.__side_2_length

    def __str__(self):
        """Returns the name of the rectangle."""

        return self.name

    def draw(self):
        """
        Prints the name of the shape followed by the area and perimeter of the shape
        formatted as follows: 'name_of_shape, area: value_of_area, perimeter: value_of_perimeter'
        """
        print(f"{self.name}, area: {self.area()}, perimeter: {self.perimeter()}")

    def draw_graphic(self):
        """Creates a graphic of the rectangle."""

        t = Turtle()
        text = Turtle()
        s = t.getscreen()
        s.bgcolor("yellow")
        count = 0
        while count < 1:
            text.penup()
            text.setposition(-100, -100)
            text.pencolor("green")
            text.write("{}, area: {:.2f}, perimeter: {:.2f}".format(self.name, self.area(), self.perimeter()), align="left",
                    font=("Arial", 20, "bold"))
            t.pen(pencolor="green", fillcolor="green", pensize=6, speed=800)
            for edge in range(2):
                t.fillcolor("red")
                t.begin_fill()
                t.forward(self.__side_1_length)
                delay(100)
                t.left(self.angle)
                t.forward(self.__side_2_length)
                t.left(self.angle)
                delay(30)
                t.end_fill()
            t.clear()
            t.reset()
            text.clear()
            text.reset()
            count += 1