#Abstract classes in Exercise 7 class Person
import random
from abc import ABC,abstractmethod

class Person(ABC):

    def __init__(self, name, salary, sum_serves=0):
        self.name = name
        self.salary = salary
        self.sum_serves = sum_serves


class Waiter(Person):
    def serve(self, costumers, barista):
        print(f"Waiter: {self.name} serve {costumers} using barista {barista.name}")
        self.sum_serves += costumers
        barista.prepare(costumers)

    def __str__(self):
        return f"O Waiter: {self.name} εξυπηρέτησε {self.sum_serves}"


class Barista(Person):
    def prepare(self, costumers):
        print(f"Barista: {self.name} prepare {costumers}")
        self.sum_serves += costumers

    def __str__(self):
        return f"O Barista: {self.name} εξυπηρετησε {self.sum_serves}"


class Owner(Person):
    def serve(self, costumers, barista):
        print(f"Owner: {self.name} serve {costumers} using barista {barista.name}")
        self.sum_serves += costumers
        barista.prepare(costumers)

    def prepare(self, costumers):
        print(f"Owner: {self.name} prepare {costumers}")
        self.sum_serves += costumers


barista1 = Barista("Babis-barista", 1500)
barista2 = Barista("Sotos-barista", 1550)
owner = Owner("Giannis-Afentiko", 10000)
waiter1 = Waiter("Giorgos-servitoros", 1000)
waiter2 = Waiter("Vasilis-servitoros", 1100)

waiters = [waiter1, waiter2, owner]
baristas = [barista1, barista2, owner]

for i in range(10):
    costumers = random.randint(1, 5)
    random_waiter = random.choice(waiters)
    random_barista = random.choice(baristas)
    random_waiter.serve(costumers, random_barista)
