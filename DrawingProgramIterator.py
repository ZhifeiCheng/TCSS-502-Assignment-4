class DrawingProgramIterator:
    """
    This provides the ability to iterate across the collection of shapes in DrawingProgram.
    """
    
    """Takes a given list of shapes and sets the index."""
    def __init__(self, shape_collection):
        self.__shape_collection = shape_collection
        self.__idx__ = 0

    """Iterates across the shapes in the list."""
    def __next__(self):
        if self.__idx__ == len(self.__shape_collection):
            raise StopIteration
        else:
            shape = self.__shape_collection[self.__idx__]
            self.__idx__ += 1
            return shape
    
    """Returns itself."""
    def __iter__(self):
        return self

