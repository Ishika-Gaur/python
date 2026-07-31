my_file = open("test.txt")

print(my_file.read())

my_file.seek(0)

print(my_file.read())

my_file.close()