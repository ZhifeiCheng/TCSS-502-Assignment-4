from Circle import Circle
from Square import Square
from Rectangle import Rectangle
from Triangle import Triangle


class ShapeFactory:
     """
     The assignment says to use @staticmethod decorator/annotation
     on top of your create_shape definition. Need to try this, if required.
     """
     def create_shape(self, shape_name, *args):
        if shape_name == 'circle':
            radius = args[0]
            return Circle(shape_name, radius)
        elif shape_name == 'square':
            side = args[0]
            return Square(shape_name, side)
        elif shape_name == 'rectangle':
            length = args[0]
            breadth = args[1]
            return Rectangle(shape_name, length, breadth)
        elif shape_name == 'triangle':
            a = args[0]
            b = args[1]
            c = args[2]
            return Triangle(shape_name, a, b, c)
