from Shape import Shape
from turtle import Turtle, delay


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
        
        print(f"name_of_shape {self.name}, area: {self.area()}, perimeter: {self.perimeter()}")

    def draw_graphic(self):
        """Creates a graphic of the rectangle."""
        
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
