# (Normal Function)
def multiply_by_two(item):
    return item * 2


numbers = [1,2,3]

print(list(map(multiply_by_two, numbers)))


# (Using Lambda)

numbers = [1,2,3]

result = list(
    map(
        lambda item: item * 2,
        numbers
    )
)

print(result)




# Lambda with map()

# General Form

# map(
#     lambda parameter: expression,
#     iterable
# )

# Example

# list(
#     map(
#         lambda x: x*2,
#         [1,2,3]
#     )
# )






# Q1. What is a Lambda Expression?

# Answer:

# A Lambda Expression is an anonymous (nameless) function written in a single line and generally used for short, one-time operations.

# Q2. What is the syntax of a Lambda function?

# Answer:

# lambda parameters: expression
# Q3. Does a Lambda function use the return keyword?

# Answer:

# No. The expression is automatically returned.

# Q4. Where are Lambda functions commonly used?

# Answer:

# They are commonly used with:

# map()
# filter()
# reduce()
# sorted()
# List comprehensions (in some cases)
# Q5. What is the difference between a normal function and a Lambda function?

# Answer:

# A normal function has a name and can contain multiple statements. A Lambda function is anonymous, usually written in one line, automatically returns its expression, and is mainly used for short, one-time operations.