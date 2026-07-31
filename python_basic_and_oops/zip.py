a = [1,2,3]

b = [10,20,30]

result = list(zip(a,b))

print(result)

print(a)

print(b)

# Q1. What is zip()?

# Answer:

# zip() is a built-in Python function that combines elements from two or more iterables into tuples and returns a zip object.

# Q2. What does zip() return?

# Answer:

# It returns a zip object (iterator).

# Q3. Why do we use list(zip(...))?

# Answer:

# Because zip() returns a zip object, and converting it to a list lets us view the paired elements.

# Q4. Does zip() modify the original lists?

# Answer:

# No. It creates a new zip object and leaves the original iterables unchanged.

# Q5. What happens if iterables have different lengths?

# Answer:

# zip() stops when the shortest iterable ends, and any extra elements in longer iterables are ignored.