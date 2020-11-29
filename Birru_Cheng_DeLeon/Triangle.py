import math
from Shape import Shape
from turtle import Turtle, delay


class Triangle(Shape):
    """
    The Triangle class is a child class of Shape.
    It provides provide specific implementations of area, perimeter, and graphics of triangles.
    """
     
    def __init__(self, name, a, b, c):
        """Creates a triangle with the given name and side lengths a, b, and c."""
        Shape.__init__(self, name)
        self.__a = a
        self.__b = b
        self.__c = c
        self.validation()
    
    def validation(self):
        """Ensures that the triangle can created with the given side lengths."""
        if self.__a > 0 and self.__b > 0 and self.__c > 0:
            if self.__a + self.__b > self.__c and self.__a + self.__c > self.__b and self.__b + self.__c > self.__a:
                return True
            else:
                raise ValueError("input sides can't make a triangle")
        else:
            raise ValueError("input must be a positive number")
    
    def perimeter(self):
        """Calculates and returns the perimeter of the triangle."""
        return self.__a + self.__b + self.__c

    def area(self):
        """Calculates and returns the area of the triangle."""
        s = self.perimeter()/2
        return math.sqrt(s * (s - self.__a)*(s - self.__b)*(s - self.__c))

    def __str__(self):
        """Returns the name of the triangle."""
        return self.name

    def draw(self):
        """Prints the name, area, and perimeter of the triangle."""
        print(f"{self.name}, area: {self.area()}, perimeter: {self.perimeter()}")

    def angle_a(self):
        """Calculates and returns angle a."""
        angle_radians = math.acos((self.__b ** 2 + self.__c ** 2 - self.__a ** 2) / (2 * self.__b * self.__c))
        return angle_radians * 180 / math.pi

    def angle_b(self):
        """Calculates and returns angle b."""
        angle_radians = math.acos((self.__a ** 2 + self.__c ** 2 - self.__b ** 2) / (2 * self.__a * self.__c))
        return angle_radians * 180/math.pi

    def angle_c(self):
        """Calculates and returns angle c."""
        angle_radians = math.acos((self.__a ** 2 + self.__b ** 2 - self.__c ** 2) / (2 * self.__a * self.__b))
        return angle_radians * 180 / math.pi

    def draw_graphic(self):
        """Draws a graphic of the triangle."""
        t = Turtle()
        text = Turtle()
        s = t.getscreen()
        s.bgcolor("blue")
        count = 0
        while count < 1:
            text.penup()
            text.setposition(-100, -100)
            text.pencolor("yellow")
            text.write("{}, area: {:.2f}, perimeter: {:.2f}".format(self.name, self.area(), self.perimeter()), align="left",
                    font=("Arial", 20, "bold"))
            t.pen(pencolor="yellow", fillcolor="green", pensize=6, speed=800)
            t.fillcolor("red")
            t.begin_fill()
            t.forward(self.__a)
            delay(100)
            t.left(180 - self.angle_c())
            t.forward(self.__b)
            delay(100)
            t.left(180 - self.angle_a())
            t.forward(self.__c)
            delay(100)
            t.end_fill()
            t.clear()
            t.reset()
            text.clear()
            text.reset()
            count += 1


