def generator_function(n):
    for i in range(n):
         yield i   # yield function ko permanently end nahi karta.  Ye sirf Pause kar deta hai. Baad me Resume kar sakte hain.

g = generator_function(3)
print(g) #<generator object generator_function at 0x00000113C11BD2F0> Ye generator memory me sirf state save karta hai.Values nahi.
print(next(g))
print(next(g))
print(next(g))


# Q1. What is a Generator?

# Answer:

# A Generator is a special Python object that generates values one at a time instead of storing all values in memory.

# Q2. Why are Generators memory efficient?

# Answer:

# Because they generate values on demand instead of creating the entire sequence in memory.

# Q3. Is range() a Generator?

# Answer:

# range() behaves like a lazy iterable that generates values as needed, which is why it is memory efficient. (In introductory courses it's often described as a generator, although technically it returns a range object, not a generator object.)


# | List                             | Generator                      |
# | -------------------------------- | ------------------------------ |
# | Saari values ek saath banata hai | Ek-ek value generate karta hai |
# | Zyada Memory Use                 | Bahut kam Memory Use           |
# | Fast Access                      | Lazy Evaluation                |
# | Large Data ke liye expensive     | Large Data ke liye best        |
