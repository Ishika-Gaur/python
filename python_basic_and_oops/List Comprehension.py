my_list = [character for character in "Hello"]

print(my_list)




# General Format
# new_list = [
#     expression
#     for variable in iterable
# ]


letters = [
    character
    for character in "Hello"
]

print(letters)



# example with condition

even_numbers = [
    number
    for number in range(10)
    if number % 2 == 0
]

print(even_numbers)




# Q1. What is List Comprehension?

# Answer:

# List Comprehension is a concise way to create a new list using a single line of code.

# Q4. What are the advantages of List Comprehension?

# Answer:

# Short code
# Cleaner syntax
# Easy list creation
# Often faster than using loops with append()


# Q5. What are the disadvantages of List Comprehension?

# Answer:

# Complex expressions can reduce readability, making the code harder for others to understand.