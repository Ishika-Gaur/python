# Encapsulation ka matlab hai:

# Data (Attributes) aur un par kaam karne wale Functions (Methods) ko ek hi object/class ke andar package (bind) kar dena.


class PlayerCharacter:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        print(f"My name is {self.name}")
        print(f"I am {self.age} years old")

player1 = PlayerCharacter("Ishika", 100)

player1.speak()    