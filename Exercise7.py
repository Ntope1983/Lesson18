class Person:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class Waiter(Person):
    def __init__(self, name, salary, barista):
        super().__init__(name, salary)
        self.barista = barista

    def serve(self, costumers):
        print(f"Waiter : {self.name} serve {costumers} in barista {self.barista}")


class Barista(Person):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def prepare(self, costumers, barista):
        print(f"Waiter : {self.name} prepare {costumers}")


class Owner(Waiter, Barista):
    pass


owner = Owner("Giannis-Afentiko", 10000)
waiter1 = Waiter("Giorgos-servitoros", 1000)
waiter2 = Waiter("Vasilis-servitoros", 1100)
barista = Barista("Babis-barista", 1500)
waiters = [waiter1, waiter2]
baristas = [barista]

