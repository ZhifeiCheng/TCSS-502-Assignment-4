import math
from Shape import Shape
from turtle import Turtle, delay


class Triangle(Shape):
    def __init__(self, name, a, b, c):
        Shape.__init__(self, name)
        self.__a = a
        self.__b = b
        self.__c = c
        self.validation()

    def validation(self):
        if self.__a > 0 and self.__b > 0 and self.__c > 0:
            if self.__a + self.__b > self.__c and self.__a + self.__c > self.__b and self.__b + self.__c > self.__a:
                return True
            else:
                raise ValueError("input sides can't make a triangle")
        else:
            raise ValueError("input must be a positive number")

    def perimeter(self):
        return self.__a + self.__b + self.__c

    def area(self):
        s = self.perimeter()/2
        return math.sqrt(s * (s - self.__a) + s * (s - self.__b) + s * (s - self.__c))

    def __str__(self):
        return self.name

    def draw(self):
        print(f"{self.name}, area: {self.area()}, perimeter: {self.perimeter()}")

    def angle_a(self):
        angle_radians = math.acos((self.__b ** 2 + self.__c ** 2 - self.__a ** 2) / (2 * self.__b * self.__c))
        return angle_radians * 180 / math.pi

    def angle_b(self):
        angle_radians = math.acos((self.__a ** 2 + self.__c ** 2 - self.__b ** 2) / (2 * self.__a * self.__c))
        return angle_radians * 180/math.pi

    def angle_c(self):
        angle_radians = math.acos((self.__a ** 2 + self.__b ** 2 - self.__c ** 2) / (2 * self.__a * self.__b))
        return angle_radians * 180 / math.pi

    def draw_graphic(self):
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


