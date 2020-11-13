from DrawingProgramIterator import DrawingProgramIterator


class DrawingProgram:

    def __init__(self):
        self.shapes = []

    def add_shape(self, shape):
            self.shapes.append(shape)

    def remove_shape(self, shape):
        """
        currently using list comprehension type of sytax.
        sytnax from book.
        """
        self.shapes = [item for item in self.shapes if type(item) != type(shape)]

    def print_shape(self, shape):
        return shape.area()

    def sort_shapes(self):
        """
        Currently using python sort function. Need to update to merge sort etc below
        and a key to sort. Need to figure this out.
         Got the lamda syntax from google.com
        """
        return sorted(self.shapes, key=lambda x: (x.shape_name, x.area()))

    def __str__(self):
        """"Need to update this"""
        if len(self.shapes) != 0:
            lst = []
            for c in self.shapes:
                lst.append(c.__str__())
            return "\n".join(lst) + "\n"
        else:
            return ""

    def __repr__(self):
        pass

    def get_shape(self, index):
        return self.shapes[index]

    def set_shape(index, shape):
        pass