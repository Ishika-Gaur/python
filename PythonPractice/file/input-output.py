my_file = open("test.txt")

print(my_file.read())
print(my_file.read())#shows empty because the file pointer is at the end of the file after the first read
my_file.close()

#for avoiding this we can use seek() method to move the file pointer to the beginning of the file