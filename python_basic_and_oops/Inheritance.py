# Inheritance ka matlab hai:

# Ek nayi class (Child Class) kisi existing class (Parent Class) ke attributes aur methods ko inherit (use) kar sakti hai.


class User:

    def sign_in(self):
        print("Logged In")


class Wizard(User):
    pass


wizard1 = Wizard()

wizard1.sign_in()


# Q1. What is Inheritance?

# Answer:

# Inheritance is an OOP feature that allows a child class to inherit the attributes and methods of a parent class.

# Q2. Why do we use Inheritance?

# Because it:

# Promotes code reusability.
# Reduces code duplication.
# Makes code easier to maintain.
# Follows the DRY principle.

# Q3. What is a Parent Class?

# A Parent (Base/Super) Class contains common functionality that can be shared by multiple child classes.

# Q4. What is a Child Class?

# A Child (Derived/Sub) Class inherits features from a parent class and can also define its own unique attributes and methods.