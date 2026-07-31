class A:
    num = 1


class B(A):
    pass


class C(A):
    num = 2


class D(B, C):
    pass


d = D()

print(d.num)      # Output: 1

print(D.mro())    # Method Resolution Order
print(D.__mro__)  # Same as mro(), but returns tuple


# MRO = Method Resolution Order

# 📖 Definition (Hinglish)

# Method Resolution Order (MRO) woh order hota hai jisme Python method ya attribute ko search karta hai, especially Multiple Inheritance ke case me