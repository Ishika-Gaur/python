# isinstance() Python ka ek built-in function hai.

# Iska use check karne ke liye hota hai ki:

# Kya koi object kisi particular class ka instance hai?



class User:

    def sign_in(self):
        print("Logged In")


class Wizard(User):
    pass


wizard1 = Wizard()

print(isinstance(wizard1, User))




# Q1. What is isinstance()?

# Answer:

# isinstance() is a built-in Python function used to check whether an object is an instance of a particular class or its parent class.

# Q2. Why does isinstance(wizard1, User) return True?

# Because Wizard inherits from User, so every Wizard object is also considered a User object.

# Q3. What is the base class of all Python classes?

# Answer:

# The built-in object class is the base class of all classes in Python.

# Q4. Where do dunder methods like __str__() and __repr__() come from?

# They are inherited from Python's built-in object class.