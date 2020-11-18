from Shape import Shape
from DrawingProgramIterator import DrawingProgramIterator


class DrawingProgram:
    def __init__(self):
        self.__shape_list = []

    def add_shape(self, shape: Shape):
        self.__shape_list.append(shape)

    def remove_shape(self, shape: Shape):
        remain = list(filter(lambda x: x is not shape, self.__shape_list))
        count = len(self.__shape_list) - len(remain)
        self.__shape_list = remain
        return count

    def print_shape(self, target_shape: Shape):
        for shape in self.__shape_list:
            if shape.name == target_shape.name:
                shape.draw()
                shape.draw_graphic()

    def get_shape(self, index: int) -> Shape:
        if 0 <= index < len(self.__shape_list):
            return self.__shape_list[index]
        else:
            raise ValueError("index is out of range")

    def set_shape(self, index: int, shape: Shape):
        if 0 <= index < len(self.__shape_list):
            self.__shape_list[index] = shape
        else:
            raise ValueError("index is out of range")

    def sort_shape(self):
        DrawingProgram.merge_sort(self.__shape_list)

    @staticmethod
    def merge_sort(lst):
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
            while j < len(left):
                lst[k] = left[j]
                j += 1
                k += 1

    def __str__(self):
        for shape in self.__shape_list:
            print(f"{shape}\n")

    def __iter__(self):
        return DrawingProgramIterator(self.__shape_list)
