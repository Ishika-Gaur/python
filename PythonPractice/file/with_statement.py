# Problem:

# Hume manually close() karna padta hai.
# Agar beech me error aa jaye to file close nahi hogi.
# Solution → with

with open("test.txt") as my_file:
    print(my_file.read())


    
