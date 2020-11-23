import unittest
from Circle import Circle
from Square import Square
from Rectangle import Rectangle
from Triangle import Triangle
from DrawingProgram import DrawingProgram
from DrawingProgramIterator import DrawingProgramIterator
from ShapeFactory import ShapeFactory


class MyTests(unittest.TestCase):

    """
    1) DrawingProgram class functionality tests
    """

    def test_sort_operates_on_empty_list_of_shapes(self):
        pass

    def test_sort_one_shape(self):
        pass

    def test_multiple_shapes_ascending_order(self):
        pass

    def test_multiple_shapes_descending_order(self):
        pass

    def test_multiple_shapes_random_order(self):
        pass

    """
    2) DrawingProgramIterator class functionality
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


if __name__ == '__main__':
    unittest.main()
