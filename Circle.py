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
        
        return math.pi*math.sqrt(self.__radius)

    def __eq__(self, other):
        """Determines if circles are equal."""
        
        if isinstance(other, Circle):
            return False
        return super().__eq__(other)

    def perimeter(self):
        """Calculates and returns the perimeter of the circle using the radius."""
        
        return 2*math.pi*self.__radius

    def __str__(self):
        """Returns the circle name."""
        
        return self.name

    # def draw(self):
    """
    prints the name of the shape followed by the area and perimeter of the shape 
    formatted as follows: 'name_of_shape, area: value_of_area, perimeter: value_of_perimeter'
    """
    
    #     print(f"name_of_shape {self.name}, area: {self.area}, perimeter: {self.perimeter}")

    def draw_graphic(self):
        """Creates a graphic of the circle."""
        
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
