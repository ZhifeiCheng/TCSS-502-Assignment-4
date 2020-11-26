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
    1) DrawingProgram class functionality tests
    """
    def test_add_shape_one_shape(self):
        shape = Square("Square", 30)
        drawing_program = DrawingProgram()
        drawing_program.add_shape(shape)
        self.assertIs(shape, drawing_program.get_shape(0), "one shape not added to the drawing program properly")

    def test_add_shape_multiple_shapes(self):
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
        shape_1 = Square("Square", 30)
        shape_2 = Square("Square", 30)
        shape_3 = Square("Square", 30)
        shape_list = [shape_1, shape_2, shape_3]
        drawing_program = DrawingProgram()
        for shape in shape_list:
            drawing_program.add_shape(shape)
        for i in range(len(shape_list)):
            self.assertIs(shape_list[i], drawing_program.get_shape(i), "duplicated shapes not added to drawing program properly")

    def test_remove_shape_one_shape(self):
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

    def test_print_shape(self):
        shape_1 = Square("Square", 30)
        shape_2 = Circle("Circle", 50)
        shape_3 = Triangle("Triangle", 30, 40, 50)
        shape_4 = Circle("Circle", 50)
        shape_list = [shape_1, shape_2, shape_3, shape_4]
        drawing_program = DrawingProgram()
        for shape in shape_list:
            drawing_program.add_shape(shape)

    def test_get_shape_negative_index(self):
        drawing_program = DrawingProgram()
        try:
            drawing_program.get_shape(-1)
            self.assertEqual(True, False, "index out of range")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_get_shape_valid_index(self):
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
        drawing_program = DrawingProgram()
        try:
            drawing_program.set_shape(-1, Square("Square", 30))
            self.assertEqual(True, False, "should not have got here, set_shape took a negative index")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_set_shape_valid_index(self):
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

    def test_sort_operates_on_empty_list_of_shapes(self):
        drawing_program = DrawingProgram()
        drawing_program.sort_shape()
        self.assertEqual("", drawing_program.__str__())

    def test_sort_one_shape(self):
        shape_1 = Square("Square", 30)
        drawing_program = DrawingProgram()
        drawing_program.add_shape(shape_1)
        shapes = [shape_1]
        drawing_program.sort_shape()
        self.assertEqual(shapes[0], drawing_program.get_shape(0), "should be None for drawing program")

    def test_multiple_shapes_ascending_order(self):
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
    """

    def test_circle_radius_negative_value(self):
        try:
            Circle("Circle", -1.0)
            self.assertEqual(True, False, "circle radius is negative")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_circle_radius_zero_value(self):
        try:
            Circle("Circle", 0.0)
            self.assertEqual(True, False, "circle radius is zero")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_square_side_length_negative_value(self):
        try:
            Square("Square", -1.0)
            self.assertEqual(True, False, "square length is negative")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_square_side_length_zero_value(self):
        try:
            Square("Square", 0.0)
            self.assertEqual(True, False, "square length is zero")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_rectangle_side_lengths_negative_value(self):
        try:
            Rectangle("Rectangle", -1.0,-1.0)
            self.assertEqual(True, False, "rectangle length is negative")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_rectangle_side_lengths_zero_value(self):
        try:
            Rectangle("Rectangle", 0.0, 0.0)
            self.assertEqual(True, False, "rectangle length is zero")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_triangle_side_lengths_negative_value(self):
        try:
            Triangle("Triangle", -1.0, -1.0, -1.0)
            self.assertEqual(True, False, "triangle length is negative")
        except ValueError as value_error:
            self.assertEqual(True, True)

    def test_triangle_side_lengths_zero_value(self):
        try:
            Triangle("Triangle", 0.0, 0.0, 0.0)
            self.assertEqual(True, False, "triangle length is zero")
        except ValueError as value_error:
            self.assertEqual(True, True)



    """
     4) Shape Factory Tests
    """
    def test_returns_circle(self):
        shape = ShapeFactory.create_shape("Circle", 1.0)
        self.assertEqual(vars(shape), vars(Circle("Circle", 1.0)),
                         "Shape factory does not return Circle")

    def test_returns_square(self):
        shape = ShapeFactory.create_shape("Square", 1.0)
        self.assertEqual(vars(shape), vars(Square("Square", 1.0)),
                         "Shape factory does not return Square")

    def test_returns_rectangle(self):
        shape = ShapeFactory.create_shape("Rectangle", 1.0, 1.0)
        self.assertEqual(vars(shape), vars(Rectangle("Rectangle", 1.0, 1.0)),
                         "Shape factory does not return Rectangle")

    def test_returns_triangle(self):
        shape = ShapeFactory.create_shape("Triangle", 3.0, 4.0, 5.0)
        self.assertEqual(vars(shape), vars(Triangle("Triangle", 3.0, 4.0, 5.0)),
                         "Shape factory does not return Triangle")
