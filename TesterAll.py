import unittest
from Circle import Circle
from Square import Square
from Rectangle import Rectangle
from Triangle import Triangle
from DrawingProgram import DrawingProgram


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

    def test_for_loop_no_shapes(self):
        pass

    def test_for_loop_one_shapes(self):
        pass

    def test_for_loop_5_shapes(self):
        pass

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
        pass

    def test_returns_square(self):
        pass

    def test_returns_rectangle(self):
        pass

    def test_returns_triangle(self):
        pass


if __name__ == '__main__':
    unittest.main()