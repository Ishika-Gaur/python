# Higher-Order Function (HOF) wo function hota hai jo ya to kisi function ko argument ke roop me accept karta hai ya fir kisi function ko return karta hai.

# Simple words me:

# Function jo function ke saath kaam kare, use Higher-Order Function kehte hain.

# Higher-Order Function ke 2 Types


# 1. Function accepts another function

def greet():
    print("Hello")


def hello(function):
    function()

hello(greet)

# Step-by-Step Working

# Step 1
# hello(greet)
# Matlab
# function = greet

# Step 2
# function()
# Matlab
# greet()
# Execute hoga.



# 2. Function returns another function
def greet():

    def func():
        return 5

    return func

result = greet()

print(result)   # output - <function greet.<locals>.func at 0x000002074FB0BAB0>
# Return karta hai
# Function Reference



# other

def greet():

    def func():
        return 5

    return func

result = greet()

print(result())  # output - 5>

# Return karta hai
# Function ka Result