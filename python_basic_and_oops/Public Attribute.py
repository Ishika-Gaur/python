
# Public Attribute Kya Hota Hai?

# Jo attribute ya method directly access aur modify kiya ja sake.


class PlayerCharacter:

    def __init__(self, name, age):
        self.name = name
        self.age = age

player1 = PlayerCharacter("ishika", 25)
print(player1.name)  # Output: ishika access 

player1.name = "Rahul"
print(player1.name)  # Output: Rahul modify