from collections import OrderedDict

d1 = OrderedDict()

d1["A"] = 1
d1["B"] = 2

d2 = OrderedDict()

d2["B"] = 2
d2["A"] = 1

print(d1 == d2)   #output false


# Why?

# Insertion Order alag hai.


# d1 = {
# "A":1,
# "B":2
# }

# d2 = {
# "B":2,
# "A":1
# }

# print(d1 == d2)


# Python 3.7 aur uske baad normal dict bhi insertion order preserve karta hai.
# Isliye aaj ke modern Python me OrderedDict ki zarurat pehle se kaafi kam ho gayi hai.
# Lekin OrderedDict me kuch extra methods aur order-specific behavior hote hain, isliye kuch special cases me ab bhi use hota hai.