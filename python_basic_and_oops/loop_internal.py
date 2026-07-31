def special_for(iterable):

    iterator = iter(iterable) #Iterable ko Iterator me convert karta hai.

    while True:

        try:
            print(next(iterator))

        except StopIteration:
            break

special_for([1, 2, 3])        