class Animal:
    def make_sound(self):
        print("")


class Cat(Animal):
    def make_sound(self):
        print("Meow")


class HimalayanCat(Cat):
    def make_sound(self):
        print("Miouw Miouw")


class Dog(Animal):
    def make_sound(self):
        print("Woof Woof")


class Doberman(Dog):
    pass

class KingDoberman(Doberman):
    def make_sound(self):
        print("WOOAAAAAAAAF")


animal=Animal()
animal.make_sound()
cat=Cat()
cat.make_sound()
himalayanCat=HimalayanCat()
himalayanCat.make_sound()
dog=Dog()
dog.make_sound()
doberman=Doberman()
kingDoberman=KingDoberman()
kingDoberman.make_sound()