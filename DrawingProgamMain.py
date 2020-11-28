from DrawingProgram import DrawingProgram
from ShapeFactory import ShapeFactory


class DrawingProgramMain:
    """
    Creates a DrawingProgram, adds shapes to it, sorts the shapes, 
    adds some more shapes, replaces some shapes, and sorts again.
    """
    @staticmethod
    def main():
        """Create DrawingProgram"""
        drawing_program = DrawingProgram()
        print('DrawingProgram created.')
        
        """Create Shapes"""
        circle_1 = ShapeFactory.create_shape("Circle", 20) # circle with radius 20
        circle_2 = ShapeFactory.create_shape("Circle", 60) # circle with radius 60
        circle_3 = ShapeFactory.create_shape("Circle", 80) # circle with radius 80
        rectangle_1 = ShapeFactory.create_shape("Rectangle", 80, 120) # rectangle with side lengths 80 and 120
        square_1 = ShapeFactory.create_shape("Square", 100) # square with side length 100
        square_2 = ShapeFactory.create_shape("Square", 100) # another square with side length 100
        triangle_1 = ShapeFactory.create_shape("Triangle", 150, 200, 250) # triangle with side lengths 150, 200, and 250
        triangle_2 = ShapeFactory.create_shape("Triangle", 100, 150, 200) # triangle with side lengths 100, 150, and 200
        print('Shapes created.')
        
        """Add shapes to DrawingProgram"""
        drawing_program.add_shape(square_1)
        drawing_program.add_shape(rectangle_1)
        drawing_program.add_shape(rectangle_1)
        drawing_program.add_shape(rectangle_1)
        drawing_program.add_shape(rectangle_1)
        drawing_program.add_shape(circle_1)
        drawing_program.add_shape(square_2)
        drawing_program.add_shape(circle_2)
        drawing_program.add_shape(circle_3)
        drawing_program.add_shape(triangle_1)
        drawing_program.add_shape(triangle_2)
        print('Shapes added to DrawingProgram.')
        
        """Removes shape"""
        drawing_program.remove_shape(square_2)
        print('square_2 removed.')
        
        """Sorts shapes"""
        drawing_program.sort_shape()
        print('Shapes sorted.')
        
        """Prints a shape"""
        drawing_program.print_shape(circle_2)
        print('circle_2 printed.')
        
        """Gets a shape"""
        drawing_program.get_shape(2)
        print('Got shape at index 2.')
        
        """Sets a shape"""
        drawing_program.set_shape(4, square_2)
        print('Set shape at index 4 as square_2.')
        
        """Prints shape again"""
        drawing_program.print_shape(circle_2)
        print('circle_2 printed.')
        
        """Draw all the shapes"""
        for shape in drawing_program:
            shape.draw()
            shape.draw_graphic()
        print('Shapes drawn.')


if __name__ == "__main__":
    DrawingProgramMain.main()
