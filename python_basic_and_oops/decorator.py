def my_decorator(func):

    def wrap_func():
        func()

    return wrap_func


#     Step-by-Step
# Line 1
# def my_decorator(func):

# Ye ek Higher-Order Function hai.

# Kyun?

# Kyuki ye ek function receive kar raha hai.

# Line 2
# def wrap_func():

# Ye wrapper function hai.

# Iska kaam hai original function ko wrap karna.

# Line 3
# func()

# Original function execute hoga.

# Line 4
# return wrap_func

# ⚠️ Bahut Important

# Humne likha

# return wrap_func

# Na ki

# return wrap_func()

# Difference:

# return wrap_func

# ↓

# Function Return

# return wrap_func()

# ↓

# Function Execute + Result Return



def my_decorator(func):

    def wrap_func():

        print("********")

        func()

        print("********")

    return wrap_func


@my_decorator
def hello():
    print("Hello")


hello()