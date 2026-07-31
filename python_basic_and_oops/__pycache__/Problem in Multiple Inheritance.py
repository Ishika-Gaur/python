# -----------------------------
# Multiple Inheritance Example
# -----------------------------

class User:

    def sign_in(self):
        print("Logged In")


class Wizard(User):

    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"{self.name} attacked with power {self.power}")


class Archer(User):

    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows

    def check_arrows(self):
        print(f"Arrows Left: {self.arrows}")

    def run(self):
        print("Ran Really Fast")


# ==========================================
# ❌ Problem
# ==========================================

# HybridBorg inherits from Wizard and Archer,
# but it doesn't have its own constructor.

class HybridBorg(Wizard, Archer):
    pass


# This will give an error because HybridBorg
# doesn't know how to initialize both parents.

# hb = HybridBorg("Borgie", 50)
# TypeError: HybridBorg() takes no arguments


# ==========================================
# ✅ Solution
# ==========================================

class HybridBorg(Wizard, Archer):

    def __init__(self, name, power, arrows):
        Wizard.__init__(self, name, power)
        Archer.__init__(self, name, arrows)


# Create Object
hb = HybridBorg("Borgie", 50, 100)

# Wizard Method
hb.attack()

# Archer Methods
hb.check_arrows()
hb.run()

# User Method
hb.sign_in()

# Attributes
print(hb.name)
print(hb.power)
print(hb.arrows)