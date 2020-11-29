from Shape import Shape
from DrawingProgramIterator import DrawingProgramIterator


class DrawingProgram:
    """
    This program holds a list of shapes to be drawn. 
    The list can be edited by adding, removing, setting, and sorting shapes. 
    Users can also get a shape at a given index, print shapes, and return the list of shapes.
    """
    
    def __init__(self):
        """DrawingProgram Constructor. Creates an empty list of shapes."""
        self.__shape_list = []

    def add_shape(self, shape: Shape):
        """Adds a given Shape to the list of shapes."""
        self.__shape_list.append(shape)

    def remove_shape(self, shape: Shape):
        """removes all shapes that match the one passed as a parameter and return in integer value to signify how many
        of that shape was removed."""
        remain = list(filter(lambda x: x != shape, self.__shape_list))
        count = len(self.__shape_list) - len(remain)
        self.__shape_list = remain
        return count

    def print_shape(self, target_shape: Shape):
        """Prints all shapes that match the type of the shape passed in both textually and graphically."""
        for shape in self.__shape_list:
            if shape.name == target_shape.name:
                shape.draw()
                shape.draw_graphic()

    def get_shape(self, index: int) -> Shape:
        """Returns the shape that is in the list at the given index."""
        if len(self.__shape_list) > 0 and 0 <= index < max(len(self.__shape_list), 1):
            return self.__shape_list[index]
        else:
            raise ValueError("index is out of range")

    def set_shape(self, index: int, shape: Shape):
        """Sets the given shape to the given index in the list."""
        if len(self.__shape_list) > 0 and 0 <= index < len(self.__shape_list):
            self.__shape_list[index] = shape
        else:
            raise ValueError("index is out of range")

    def sort_shape(self):
        """
        Sorts shapes in the list.
        Shapes will be sorted first by name, then by area if names are same.
        """
        DrawingProgram.merge_sort(self.__shape_list)

    @staticmethod
    def merge_sort(lst):
        """Merge sort used to sort the shapes."""
        if len(lst) > 1:
            mid = len(lst) // 2
            left = lst[:mid]
            right = lst[mid:]
            DrawingProgram.merge_sort(left)
            DrawingProgram.merge_sort(right)
            i = 0
            j = 0
            k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    lst[k] = left[i]
                    i += 1
                else:
                    lst[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                lst[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                lst[k] = right[j]
                j += 1
                k += 1
    
    def __str__(self):
        """Returns the strings of the shapes in the list."""
        return "\n".join(map(lambda shape: shape.get_name, self.__shape_list))

    def __iter__(self):
        """Return iterator."""
        return DrawingProgramIterator(self.__shape_list)
