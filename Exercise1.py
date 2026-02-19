# Base class for all animals with common attributes
class Animal:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height


# Horse inherits from Animal and adds colour and tail size
class Horse(Animal):
    def __init__(self, weight, height, colour, size_tail):
        super().__init__(weight, height)
        self.colour = colour
        self.tail = size_tail


# Dog inherits from Animal and adds bark volume
class Dog(Animal):
    def __init__(self, weight, height, bark_db):
        super().__init__(weight, height)
        self.bark_db = bark_db

    # Dog behavior method
    def bark(self):
        print(f"Woof*{self.bark_db}")


# Doberman is a specific type of Dog
class Doberman(Dog):
    def __init__(self, weight, height, bark_db):
        super().__init__(weight, height, bark_db)

    def run(self):
        print("Running doberman")


# Bulldog is another Dog type with ear size
class Bulldog(Dog):
    def __init__(self, weight, height, bark_db, size_ear):
        super().__init__(weight, height, bark_db)
        self.size_ear = size_ear

    def sleep(self):
        print("Sleeping Bulldog")


# Create objects and call methods
horse = Horse(1, 200, "black", 0.80)
doberman = Doberman(50, 0.50, 70)
bulldog = Bulldog(40, 0.40, 30, 0.12)

print(horse.colour)
doberman.bark()
doberman.run()
doberman.bark()
bulldog.bark()
bulldog.sleep()