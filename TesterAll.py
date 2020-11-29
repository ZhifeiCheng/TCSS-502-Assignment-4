import random
import unittest
from Circle import Circle
from DrawingProgram import DrawingProgram
from Rectangle import Rectangle
from Square import Square
from Triangle import Triangle
from ShapeFactory import ShapeFactory
from DrawingProgramIterator import DrawingProgramIterator


class MyTests(unittest.TestCase):
    """
    This class contains unit tests to ensure proper functionality of the programs for Assignment 4.
    """

    """
    1) DrawingProgram class functionality tests
    """
    
    """Adding shapes. Also demonstrates different types of shapes can be properly created."""
    
    def test_add_shape_one_shape(self):
        """Demonstrates that one shape can be added."""
        shape = Square("Square", 30)
        drawing_program = DrawingProgram()
        drawing_program.add_shape(shape)
        self.assertIs(shape, drawing_program.get_shape(0), "one shape not added to the drawing program properly")

    def test_add_shape_multiple_shapes(self):
        """Demonstrates thtat multiple shapes can be added."""
        shape_1 = Square("Square", 30)
        shape_2 = Circle("Circle", 50)
        shape_3 = Triangle("Triangle", 30, 40, 50)
        shape_list = [shape_1, shape_2, shape_3]
        drawing_program = DrawingProgram()
        for shape in shape_list:
            drawing_program.add_shape(shape)
        for i in range(len(shape_list)):
            self.assertIs(shape_list[i], drawing_program.get_shape(i), "multiple shapes not added to drawing program properly")

    def test_add_shape_duplicated_shapes(self):
        """Demonstrates that duplicated shapes can be added."""
        shape_1 = Square("Square", 30)
        shape_2 = Square("Square", 30)
        shape_3 = Square("Square", 30)
        shape_list = [shape_1, shape_2, shape_3]
        drawing_program = DrawingProgram()
        for shape in shape_list:
            drawing_program.add_shape(shape)
        for i in range(len(shape_list)):
            self.assertIs(shape_list[i], drawing_program.get_shape(i), "duplicated shapes not added to drawing program properly")

    """Removing shapes."""
    
    def test_remove_shape_one_shape(self):
        """Demonstrates that one shape can be removed."""
        shape_1 = Square("Square", 30)
        shape_2 = Circle("Circle", 50)
        shape_3 = Triangle("Triangle", 30, 40, 50)
        shape_4 = Circle("Circle", 80)
        shape_list = [shape_1, shape_2, shape_3, shape_4]
        drawing_program = DrawingProgram()
        for shape in shape_list:
            drawing_program.add_shape(shape)
        self.assertEqual(drawing_program.remove_shape(shape_2), 1, "shapes not removed properly")
        remain_shapes = [drawing_program.get_shape(i) for i in range(3)]
        removed_shapes = list(filter(lambda shape: shape not in remain_shapes, shape_list ))
        self.assertIs(removed_shapes[0], shape_2)

    def test_remove_shape_duplicated_shapes(self):
        """Demonstrates that duplicated shapes can be removed."""
        shape_1 = Square("Square", 30)
        shape_2 = Circle("Circle", 50)
        shape_3 = Triangle("Triangle", 30, 40, 50)
        shape_4 = Circle("Circle", 50)
        shape_list = [shape_1, shape_2, shape_3, shape_4]
        drawing_program = DrawingProgram()
        for shape in shape_list:
            drawing_program.add_shape(shape)
        self.assertEqual(drawing_program.remove_shape(shape_2), 2, "shapes not removed properly")
        remain_shapes = [drawing_program.get_shape(i) for i in range(2)]
        removed_shapes = list(filter(lambda shape: shape not in remain_shapes, shape_list))
        self.assertIs(removed_shapes[0], shape_2)
        self.assertIs(removed_shapes[1], shape_4)

    """Printing shapes."""
    
    def test_print_shape(self):
        """Demonstrates shapes can be printed."""
        shape_1 = Square("Square", 30)
        shape_2 = Circle("Circle", 50)
        shape_3 = Triangle("Triangle", 30, 40, 50)
        shape_4 = Circle("Circle", 50)
        shape_list = [shape_1, shape_2, shape_3, shape_4]
        drawing_program = DrawingProgram()
        for shape in shape_list:
            drawing_program.add_shape(shape)

    """Testing given indeces."""
    
    def test_get_shape_negative_index(self):
        """Demonstrates proper handling of a negative index for get_shape."""
        drawing_program = DrawingProgram()
        try:
            drawing_program.get_shape(-1)
            self.assertEqual(True, False, "index out of range")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_get_shape_valid_index(self):
        """Demonstrates get_shape is functional when given a valid index."""
        shape_1 = Square("Square", 30)
        shape_2 = Circle("Circle", 50)
        shape_3 = Triangle("Triangle", 30, 40, 50)
        shape_4 = Circle("Circle", 50)
        shapes = [shape_1, shape_2, shape_3, shape_4]
        drawing_program = DrawingProgram()
        for shape in shapes:
            drawing_program.add_shape(shape)
        for idx in range(len(shapes)):
            self.assertEqual(shapes[idx], drawing_program.get_shape(idx), "shapes not got properly")

    def test_set_shape_negative_index(self):
        """Demonstrates proper handling of a negative index for set_shape."""
        drawing_program = DrawingProgram()
        try:
            drawing_program.set_shape(-1, Square("Square", 30))
            self.assertEqual(True, False, "should not have got here, set_shape took a negative index")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_set_shape_valid_index(self):
        """Demonstrates functionality of set_shape when given a valid index."""
        shape_1 = Square("Square", 30)
        shape_2 = Circle("Circle", 50)
        shape_3 = Triangle("Triangle", 30, 40, 50)
        shape_4 = Circle("Circle", 50)
        shapes = [shape_1, shape_2, shape_3, shape_4]
        drawing_program = DrawingProgram()
        for shape in shapes:
            drawing_program.add_shape(shape)
        drawing_program.set_shape(2, shape_3)
        self.assertEqual(shape_3, drawing_program.get_shape(2), "shapes not set properly")

    """Sorting shapes. Also demonstrates proper use of of comparing functions."""
    
    def test_sort_operates_on_empty_list_of_shapes(self):
        """Demonstrates sorting an empty list of shapes."""
        drawing_program = DrawingProgram()
        drawing_program.sort_shape()
        self.assertEqual("", drawing_program.__str__())

    def test_sort_one_shape(self):
        """Demonstrates sorting of a list of one shape."""
        shape_1 = Square("Square", 30)
        drawing_program = DrawingProgram()
        drawing_program.add_shape(shape_1)
        shapes = [shape_1]
        drawing_program.sort_shape()
        self.assertEqual(shapes[0], drawing_program.get_shape(0), "should be None for drawing program")

    def test_multiple_shapes_ascending_order(self):
        """Demonstrates sorting of a list of multiple shapes with ascending order."""
        shape_1 = Circle("Circle", 30)
        shape_2 = Rectangle("Rectangle", 30, 50)
        shape_3 = Rectangle("Rectangle", 30, 60)
        shape_4 = Square("Square", 30)
        shapes = [shape_1, shape_2, shape_3, shape_4]
        drawing_program = DrawingProgram()
        for shape in shapes:
            drawing_program.add_shape(shape)
        drawing_program.sort_shape()
        for i in range(len(shapes)):
            self.assertEqual(shapes[i], drawing_program.get_shape(i), "shapes not sorted properly")

    def test_multiple_shapes_descending_order(self):
        """Demonstrates sorting a list of multiple shapes with descending order."""
        shape_1 = Circle("Circle", 30)
        shape_2 = Rectangle("Rectangle", 30, 50)
        shape_3 = Rectangle("Rectangle", 30, 60)
        shape_4 = Square("Square", 30)
        shapes = [shape_1, shape_2, shape_3, shape_4]
        drawing_program = DrawingProgram()
        for shape in reversed(shapes):
            drawing_program.add_shape(shape)
        drawing_program.sort_shape()
        for i in range(len(shapes)):
            self.assertEqual(shapes[i], drawing_program.get_shape(i), "shapes not sorted properly")

    def test_multiple_shapes_random_order(self):
        """Demonstrates sorting a list of multiple shapes with random order."""
        shape_1 = Circle("Circle", 30)
        shape_2 = Rectangle("Rectangle", 30, 50)
        shape_3 = Rectangle("Rectangle", 30, 60)
        shape_4 = Square("Square", 30)
        shapes = [shape_1, shape_2, shape_3, shape_4]
        drawing_program = DrawingProgram()
        random_shapes = shapes[:]
        random.shuffle(random_shapes)
        for shape in random_shapes:
            drawing_program.add_shape(shape)
        drawing_program.sort_shape()
        for i in range(len(shapes)):
            self.assertEqual(shapes[i], drawing_program.get_shape(i), "shapes not sorted properly")
            
    """
    2) DrawingProgramIterator class functionality tests
    Demonstrating the program's ability to iterate 
    across a collection of no shapes, one shape, or multiple shapes.
    """

    def test_looping_no_shapes(self):
        lst = []
        iter_0 = DrawingProgramIterator(lst)
        with self.assertRaises(StopIteration):
            next(iter_0)

    def test_looping_one_shapes(self):
        lst = []
        lst.append(1)
        iter_1 = DrawingProgramIterator(lst)
        self.assertEqual(next(iter_1), 1)
        with self.assertRaises(StopIteration):
            next(iter_1)

    def test_looping_5_shapes(self):
        lst = []
        lst.append(1)
        lst.append(2)
        lst.append(3)
        lst.append(4)
        lst.append(5)
        iter_5 = DrawingProgramIterator(lst)
        self.assertEqual(next(iter_5), 1)
        self.assertEqual(next(iter_5), 2)
        self.assertEqual(next(iter_5), 3)
        self.assertEqual(next(iter_5), 4)
        self.assertEqual(next(iter_5), 5)
        with self.assertRaises(StopIteration):
            next(iter_5)

    """
     3) Functionality of Shapes
     Testing negative and zero values demonstrates proper validation.
     Testing perimeter and area ensures proper shape creation.
    """
    
    """Circles."""
    
    def test_circle_radius_negative_value(self):
        """Demonstrates proper handling given a negative radius."""
        try:
            Circle("Circle", -1.0)
            self.assertEqual(True, False, "circle radius is negative")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_circle_radius_zero_value(self):
        """Demonstrates proper handling given a radius of zero."""
        try:
            Circle("Circle", 0.0)
            self.assertEqual(True, False, "circle radius is zero")
        except ValueError as value_error:
            self.assertEqual(True, True)
    
    def test_circle_perimeter(self):
        try:
            circle_perimeter = Circle.perimeter(Circle("Circle", 1.0))
            self.assertEqual(round(circle_perimeter, 2), 6.28, "circle perimeter is wrong")
        except ValueError as value_error:
            self.assertEqual(True, True)
        
    def test_circle_area(self):
        try:
            circle_area = Circle.area(Circle("Circle", 1.0))
            self.assertEqual(round(circle_area, 2), 3.14, "circle area is wrong")
        except ValueError as value_error:
            self.assertEqual(True,True)
    
    """Squares."""
    
    def test_square_side_length_negative_value(self):
        """Demonstrates proper handling given negative side length."""
        try:
            Square("Square", -1.0)
            self.assertEqual(True, False, "square length is negative")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_square_side_length_zero_value(self):
        """Demonstrates proper handling given a side length of zero."""
        try:
            Square("Square", 0.0)
            self.assertEqual(True, False, "square length is zero")
        except ValueError as value_error:
            self.assertEqual(True, True)
            
   def test_square_perimeter(self):
        try:
            square_perimeter = Square.perimeter(Square("Square", 1.0))
            self.assertEqual(square_perimeter, 4.0, "square perimeter is wrong")
        except ValueError as value_error:
            self.assertEqual(True, True)
        
    def test_square_area(self):
        try:
            square_area = Square.area(Square("Square", 1.0))
            self.assertEqual(square_area, 1.0, "square area is wrong")
        except ValueError as value_error:
            self.assertEqual(True,True)

    """Rectangles."""
    
    def test_rectangle_side_lengths_negative_value(self):
        """Demonstrates proper handling given negative side length."""
        try:
            Rectangle("Rectangle", -1.0,-1.0)
            self.assertEqual(True, False, "rectangle length is negative")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_rectangle_side_lengths_zero_value(self):
        """Demonstrates proper handling given side length of zero."""
        try:
            Rectangle("Rectangle", 0.0, 0.0)
            self.assertEqual(True, False, "rectangle length is zero")
        except ValueError as value_error:
            self.assertEqual(True, True)
     
    def test_rectangle_perimeter(self):
        try:
            rectangle_perimeter = Rectangle.perimeter(Rectangle("Rectangle", 1.0, 2.0))
            self.assertEqual(rectangle_perimeter, 6.0, "rectangle perimeter is wrong")
        except ValueError as value_error:
            self.assertEqual(True, True)
        
    def test_rectangle_area(self):
        try:
            rectangle_area = Rectangle.area(Rectangle("Rectangle", 1.0, 2.0))
            self.assertEqual(rectangle_area, 2.0, "rectangle area is wrong")
        except ValueError as value_error:
            self.assertEqual(True,True)

    """Triangles."""
    
    def test_triangle_side_lengths_negative_value(self):
        """Demonstrates proper handling given negative side lenghths."""
        try:
            Triangle("Triangle", -1.0, -1.0, -1.0)
            self.assertEqual(True, False, "triangle length is negative")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_triangle_side_lengths_zero_value(self):
        """Demonstrates proper handling given side lenghts of zero."""
        try:
            Triangle("Triangle", 0.0, 0.0, 0.0)
            self.assertEqual(True, False, "triangle length is zero")
        except ValueError as value_error:
            self.assertEqual(True, True)
            
    def test_triangle_perimeter(self):
        try:
            triangle_perimeter = Triangle.perimeter(Triangle("Triangle", 2.0, 3.0, 4.0))
            self.assertEqual(triangle_perimeter, 9.0, "triangle perimeter is wrong")
        except ValueError as value_error:
            self.assertEqual(True, True)
        
    def test_triangle_area(self):
        try:
            triangle_area = Triangle.area(Triangle("Triangle", 2.0, 3.0, 4.0))
            self.assertEqual(round(triangle_area, 2), 2.90, "triangle area is wrong")
        except ValueError as value_error:
            self.assertEqual(True,True)

    """
     4) Shape Factory Tests
    """
    def test_returns_circle(self):
        """Ensures circles can be created."""
        shape = ShapeFactory.create_shape("Circle", 1.0)
        self.assertEqual(vars(shape), vars(Circle("Circle", 1.0)),
                         "Shape factory does not return Circle")

    def test_returns_square(self):
        """Ensures squares can be created."""
        shape = ShapeFactory.create_shape("Square", 1.0)
        self.assertEqual(vars(shape), vars(Square("Square", 1.0)),
                         "Shape factory does not return Square")

    def test_returns_rectangle(self):
        "Ensures rectangles can be created."""
        shape = ShapeFactory.create_shape("Rectangle", 1.0, 1.0)
        self.assertEqual(vars(shape), vars(Rectangle("Rectangle", 1.0, 1.0)),
                         "Shape factory does not return Rectangle")

    def test_returns_triangle(self):
        """Ensures triangles can be created."""
        shape = ShapeFactory.create_shape("Triangle", 3.0, 4.0, 5.0)
        self.assertEqual(vars(shape), vars(Triangle("Triangle", 3.0, 4.0, 5.0)),
                         "Shape factory does not return Triangle")
