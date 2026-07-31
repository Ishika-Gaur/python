def only_odd(item):
    return item % 2 != 0


numbers = [1, 2, 3]

result = filter(only_odd, numbers)

print(list(result))



# Q1. What is filter()?

# Answer:

# filter() is a built-in Python function that filters elements from an iterable based on a condition and returns only those elements for which the condition is True.

# Q2. What are the arguments of filter()?

# Answer:

# Function (returns True or False)
# Iterable
# Q3. What does the function passed to filter() return?

# Answer:

# It should return a Boolean value (True or False).

# True → Keep the element.
# False → Remove the element.
# Q4. Why do we use list(filter(...))?

# Answer:

# Because filter() returns a filter object (iterator). Converting it to a list lets us view all the filtered elements.

# Q5. Does filter() modify the original list?

# Answer:

# No. It creates a new iterator (or a new list after conversion) and leaves the original iterable unchanged.