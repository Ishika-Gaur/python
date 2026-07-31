# Private Attribute ka matlab:

# Isse directly modify nahi karna chahiye.

# Lekin Python me ye strictly enforce nahi hota.


# Python me true private variables nahi hote, lekin single underscore (_) aur double underscore (__) ka use kiya jata hai.



class Player:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def display(self):
        print(f"Name: {self.__name}")
        print(f"Age: {self.__age}")


player1 = Player("Ishika", 21)

player1.display()

# Bad Practice (Still Possible)
player1.__name = "Rahul"

player1.display()



# Double Underscore (__) – Name Mangling (More Private)

class Player:

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def display(self):
        print(f"Name: {self.__name}")
        print(f"Age: {self.__age}")


player1 = Player("Ishika", 21)

player1.display()

# Direct Access
print(player1.__name)