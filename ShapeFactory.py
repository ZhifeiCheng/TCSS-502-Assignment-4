from Circle import Circle
from Square import Square
from Rectangle import Rectangle
from Triangle import Triangle


class ShapeFactory:
    """
    The assignment says to use @staticmethod decorator/annotation
    on top of your create_shape definition. Need to try this, if required.
    """
    @staticmethod
    def create_shape(name, *args):
        if name == "Circle":
            return Circle(name, args[0])
        elif name == "Square":
            return Square(name, args[0])
        elif name == "Rectangle":
            return Rectangle(name, args[0], args[1])
        elif name == "Triangle":
            return Triangle(name, args[0], args[1], args[2])