# without walrus operator

a = "Helloooooooo"

if len(a) > 10:
    print("Too Long")
    print(len(a))




    # with walrus operator
    a = "Helloooooooo"

if (n := len(a)) > 10:
    print("Too Long")
    print(n)



#     Walrus Operator (:=) isliye use karte hain kyunki ye ek hi line me variable me value assign bhi karta hai aur usi value ko expression (if, while, etc.) me use bhi kar deta hai.

# Example:

# if (length := len(name)) > 5:
#     print(length)

# Yahan:

# length = len(name) → value assign hui.
# length > 5 → usi value se condition bhi check ho gayi.

# 👉 = = Sirf assign
# 👉 := = Assign + turant use