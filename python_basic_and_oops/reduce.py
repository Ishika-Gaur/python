from functools import reduce


def accumulator(acc, item):
    return acc + item


numbers = [1, 2, 3]

result = reduce(accumulator, numbers, 0)

print(result)



# Q1. What is reduce()?

# Answer:

# reduce() is a function from the functools module that applies a function cumulatively to the elements of an iterable and reduces them to a single value.

# Q2. Why do we import reduce()?

# Answer:

# Because reduce() is not a built-in function. It is available in the functools module.

# from functools import reduce
# Q3. What is an accumulator?

# Answer:

# The accumulator stores the result of the previous iteration and passes it to the next iteration.

# Q4. What is the purpose of the initial value?

# Answer:

# The initial value sets the starting value of the accumulator. If omitted, reduce() starts with the first element of the iterable.

# Q5. Does reduce() modify the original list?

# Answer:

# No. It processes the iterable and returns a new single value without modifying the original iterable.

# 🔥 Quick Revision
# reduce() = functools module ka function hai jo iterable ko ek single value me reduce karta hai.
# Import: from functools import reduce
# Syntax: reduce(function, iterable, initial_value)