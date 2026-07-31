class SuperList(list):

    def __len__(self):
        return 1000


super_list = SuperList()

super_list.append(5)

print(super_list)

print(super_list[0])

print(len(super_list))


# Method Overriding occurs when a child class provides its own implementation of a method that already exists in the parent class.

# Yahan:

# Parent class = list
# Parent method = __len__()
# Child class = SuperList
# Child method = __len__()

# Isliye SuperList ne list ke __len__() method ko override kar diya.