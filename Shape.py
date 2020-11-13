import abc


class Shape(metaclass=abc.ABCMeta):

    def __init__(self, shape_name):
        self.shape_name = shape_name

    @abc.abstractmethod
    def area(self):
        return NotImplemented

    @abc.abstractmethod
    def perimeter(self):
        return NotImplemented

    def draw(self):
        print(self.shape_name, "area: ", self.area(), "perimeter: ", self.perimeter())

    def __str__(self):
        return "%s:%s:%s" % (self.shape_name, self.area, self.perimeter)

    @classmethod
    def __subclasshook__(cls, C):
        if cls is Shape:
            attrs = set(dir(C))
            if set(cls.__abstractmethods__) <= attrs:
                return True


