my_file = open("test.txt")

print(my_file.read())

my_file.seek(0)

print(my_file.readline()) #Reads only one line.

print(my_file.readlines()) #Reads the entire file and returns a list.

my_file.close()