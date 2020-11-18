class DrawingProgramIterator:
    def __init__(self, shape_collection):
        self.__shape_collection = shape_collection
        self.__idx__ = 0

    def __next__(self):
        if self.__idx__ == len(self.__shape_collection):
            raise StopIteration
        else:
            shape = self.__shape_collection[self.__idx__]
            self.__idx__ += 1
            return shape

    def __iter__(self):
        return self

