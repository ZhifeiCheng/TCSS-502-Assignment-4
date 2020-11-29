from abc import ABC, abstractmethod


class Shape(ABC):
    """
    An abstract class used to create shapes to be drawn with given properties
    such as name, perimeter, and area. Specific methods depend on the type of shape.
    """

    """Creates a shape with the given name."""
    def __init__(self, name):
        self.__name = name
    
    """Returns the name of the shape."""
    @property
    def name(self):
        return self.__name
    
    """Validates the shape can be made."""
    @abstractmethod
    def validation(self):
        pass
    
    """Calculates and returns the perimeter of the shape."""
    @abstractmethod
    def perimeter(self):
        pass
    
    """Calculates and returns the area of the shape."""
    @abstractmethod
    def area(self):
        pass
    
    """Returns the string of the shape name."""
    @abstractmethod
    def __str__(self):
        return self.name
    
    """Prints the name, area, and perimeter of the shape."""
    def draw(self):
        print(f"{self.name}, area: {self.area():.2f}, perimeter: {self.perimeter():.2f}")
    
    """Draws a graphic of the shape."""
    @abstractmethod
    def draw_graphic(self):
        pass
    
    """Compares if the size of the shape is less than another."""
    def __lt__(self, other):
        return (self.name, self.area(), self.perimeter()) < (other.name, other.area(), other.perimeter())
    
    """Compares if the size of the shape is equal to another."""
    def __eq__(self, other):
        return (self.name, self.area(), self.perimeter()) == (other.name, other.area(), other.perimeter())

