from abc import ABC, abstractmethod
from math import pi


class GeometricaObjectInterface(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Resizeable(ABC):
    @abstractmethod
    def resize(self,new_value):
        pass


class Cycle(GeometricaObjectInterface):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius


class ResizeableCycle(Cycle, Resizeable):
    def __init__(self, radius):
        super().__init__(radius)

    def area(self):
        return pi * self.radius ** 2

    def perimeter(self):
        return 2 * pi * self.radius

    def resize(self, new_radius):
        self.radius = new_radius


a=ResizeableCycle(3)

print(a.area(),a.perimeter())
