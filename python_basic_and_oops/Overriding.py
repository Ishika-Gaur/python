# Child class agar same naam ka method bana de,

# to Parent ka method replace ho jata hai.

class User:

    def attack(self):
        print("Do Nothing")


class Wizard(User):

    def attack(self):
        print("Magic Attack")


wizard = Wizard()

wizard.attack()