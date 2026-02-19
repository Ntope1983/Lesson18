class King:
    def __init__(self, realm):
        self.realm = realm

    def rule(self):
        print("Now i rule")


class Philosopher:
    def __init__(self, school):
        self.school = school

    def think(self):
        print("Now i think")


class PhilosopherKing(King,Philosopher):
    def __init__(self,realm,school):
        King.__init__(self,realm)
        Philosopher.__init__(self,school)
    def routine(self):
        self.rule()
        self.think()
        self.rule()

marcos=PhilosopherKing("Rome","Stoick")
marcos.routine()