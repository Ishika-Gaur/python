# Problem in Normal Dictionary
# student = {
#     "name":"Ishika"
# }

# print(student["age"])

# Output

# KeyError


#*** defaultdict ek dictionary hai jo missing key ke liye error dene ki jagah default value return karti hai.


from collections import defaultdict

d = defaultdict(int)

print(d["age"])  #output 0