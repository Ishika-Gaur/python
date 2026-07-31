class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, My name is {self.name} and I am {self.age} years old."


# Objects (Instances)
student1 = Student("Ishika", 20)
student2 = Student("Rahul", 21)

# Accessing Attributes
print(student1.name)
print(student1.age)

print(student2.name)
print(student2.age)

# Calling Methods
print(student1.introduce())
print(student2.introduce())