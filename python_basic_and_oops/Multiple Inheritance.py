# Multiple Inheritance means a child class inherits properties and methods from more than one parent class.


class User:

    def sign_in(self):
        print("Logged In")


class Wizard(User):

    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print("Magic Attack")


class Archer(User):

    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def run(self):
        print("Ran Really Fast")


class HybridBorg(Wizard, Archer):

    def __init__(self, name, power, arrows):
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, arrows)


hb = HybridBorg("Borgie", 50, 100)

hb.attack()
hb.run()
hb.sign_in()
print(hb.name)
print(hb.power)
print(hb.arrows)