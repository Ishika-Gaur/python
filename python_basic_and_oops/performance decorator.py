from time import time

def performance(func):

    def wrapper(*args, **kwargs):

        t1 = time()

        result = func(*args, **kwargs)

        t2 = time()

        print(f"Execution Time : {t2 - t1} seconds")

        return result

    return wrapper


@performance
def long_time():

    for i in range(10000000):
        i * 5


long_time()


# Why do we need a Performance Decorator?

# Suppose hamare paas ek function hai jo bahut bada calculation karta hai.

# def long_time():
#     for i in range(10000000):
#         i * 5

# Ab hume nahi pata ki ye function

# 0.5 second me complete hua?
# 2 second me?
# 10 second me?

# Isliye hum execution time measure karte hain.