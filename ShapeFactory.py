from Circle import Circle
from Square import Square
from Rectangle import Rectangle
from Triangle import Triangle


class ShapeFactory:
    """
    This creates shapes based on the given name.
    Circles, squares, rectangles, and triangles can be created.
    """
    
    @staticmethod
    def create_shape(name, *args):
        if name == "Circle":
            return Circle(name, args[0]) # creates circle
        elif name == "Square":
            return Square(name, args[0]) # creates square
        elif name == "Rectangle":
            return Rectangle(name, args[0], args[1]) # creates rectangle
        elif name == "Triangle":
            return Triangle(name, args[0], args[1], args[2]) #creates triangle
