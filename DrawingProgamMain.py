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
        square_2 = ShapeFactory.create_shape("Square", 200) # another square with side length 100
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
        drawing_program.add_shape(square_2)
        drawing_program.add_shape(square_2)
        drawing_program.add_shape(circle_2)
        drawing_program.add_shape(circle_3)
        drawing_program.add_shape(triangle_1)
        drawing_program.add_shape(triangle_2)
        print('Shapes added to DrawingProgram.')
        
        print(f'Removed {drawing_program.remove_shape(square_2)} passed-in shapes.')
        """Removes shape"""
        print('square_2 removed.')
        
        drawing_program.sort_shape()
        """Sorts shapes"""
        print('Shapes sorted.')
        
        drawing_program.print_shape(circle_2)
        """Prints a shape"""
        print('circle_2 printed.')
        
        drawing_program.get_shape(2)
        """Gets a shape"""
        print('Got shape at index 2.')
        
        drawing_program.set_shape(4, square_2)
        """Sets a shape"""
        print('Set shape at index 4 as square_2.')
        
        drawing_program.print_shape(circle_2)
        """Prints shape again"""
        print('circle_2 printed.')
        
        for shape in drawing_program:
            """Draw all the shapes"""
            shape.draw()
            shape.draw_graphic()
        print('Shapes drawn.')


if __name__ == "__main__":
    DrawingProgramMain.main()
