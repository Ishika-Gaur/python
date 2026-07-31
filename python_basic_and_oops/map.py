def multiply_by_two(item):
    return item * 2


numbers = [1, 2, 3]

result = map(multiply_by_two, numbers)

print(list(result))


# map() is a built-in Python function that applies a given function to every element of an iterable and returns a new map object.

# Simple words me:

# map() kisi function ko iterable (list, tuple, etc.) ke har element par apply karta hai aur naya result return karta hai.


# Q1. What is map()?

# Answer:

# map() is a built-in Python function that applies a given function to every element of an iterable and returns a map object.

# Q2. What are the arguments of map()?

# Answer:

# Function
# Iterable
# Q3. Why do we use list(map(...))?

# Answer:

# Because map() returns a map object, which is an iterator. Converting it to a list lets us see all the results.

# Q4. Does map() modify the original list?

# Answer:

# No. It creates a new iterator (or a new list after conversion) and leaves the original iterable unchanged.

# Q5. Why is map() used in Functional Programming?

# Answer:

# Because it separates data (the iterable) from behavior (the function), avoids side effects when used with pure functions, and produces clean, reusable code.