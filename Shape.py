from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, name):
        self.name = name
        # self.drawer = Shape.draw()

    @property
    def get_name(self):
        return self.name

    @abstractmethod
    def validation(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def __str__(self):
        return self.name

    def draw(self):
        print(f"name_of_shape {self.name}, area: {self.area()}, perimeter: {self.perimeter()}")

    @abstractmethod
    def draw_graphic(self):
        pass

    def __lt__(self, other):
        return (self.name, self.area(), self.perimeter()) < (other.name, other.area(), other.perimeter())

    def __eq__(self, other):
        return (self.name, self.area(), self.perimeter()) == (other.name, other.area(), other.perimeter())

