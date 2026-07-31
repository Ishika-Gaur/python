# Problem

# Pehle hamara decorator sirf without arguments wale functions ke liye kaam karta tha.

# Example

# def my_decorator(func):

#     def wrap_func():
#         print("********")
#         func()
#         print("********")

#     return wrap_func


# @my_decorator
# def hello():
#     print("Hello")

# hello()


# Ab Problem Dekho

# Suppose hum hello function me ek parameter add kar dete hain.

# def my_decorator(func):

#     def wrap_func():
#         print("********")
#         func()
#         print("********")

#     return wrap_func


# @my_decorator
# def hello(greeting):
#     print(greeting)

# hello("Hi")


# # First Solution

# # Wrapper me bhi parameter le lo.

# def my_decorator(func):

#     def wrap_func(greeting):

#         print("********")

#         func(greeting)

#         print("********")

#     return wrap_func


# @my_decorator
# def hello(greeting):
#     print(greeting)

# hello("Hi")


# Fir Problem

# Suppose hello function me 2 ,3,5,6,...parameters aa gaye.



# Best Solution → *args and **kwargs
def my_decorator(func):

    def wrap_func(*args, **kwargs):

        print("********")

        func(*args, **kwargs)

        print("********")

    return wrap_func


@my_decorator
def hello(greeting, emoji):
    print(greeting, emoji)


hello("Hi", "😊")