from abc import ABC, abstractmethod

p = 3, 14159


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


class Circle(GeometricaObjectInterface):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return p * self.radius ** 2

    def perimeter(self):
        return 2 * p * self.radius


class ResizeableCircle(Circle, Resizeable):
    def __init__(self, radius):
        super().__init__(radius)

    def area(self):
        return p * self.radius ** 2

    def perimeter(self):
        return 2 * p * self.radius

    def resize(self, new_radius):
        self.radius = new_radius


a=ResizeableCircle(3)

print(type(a.area()))
