# Polymorphism = Many Forms

# Programming me iska matlab:

# Ek hi method ka naam alag-alag classes me ho sakta hai, lekin har class us method ko apne tareeke se implement karti hai.
class Wizard:

    def attack(self):
        print("Attack with Magic")


class Archer:

    def attack(self):
        print("Attack with Arrows")


wizard = Wizard()
archer = Archer()

wizard.attack()
archer.attack()