import pdb

def add(a,b):

    pdb.set_trace()

    return a+b

print(add(5,10))



# PDB (Python Debugger) is a built-in module that lets you pause program execution and inspect variables interactively.

# Import
# import pdb
# Breakpoint
# pdb.set_trace()

# Program execution pauses here.


# Useful PDB Commands
# 1️⃣ help

# Shows all commands.

# (Pdb) help
# 2️⃣ help command

# Example

# (Pdb) help list

# Shows documentation of a command.

# 3️⃣ list

# Shows source code.

# (Pdb) list
# 4️⃣ step (s)

# Moves to the next line.

# (Pdb) step

# or

# (Pdb) s

# Useful for executing line-by-line.

# Example

# Current Line

# x = 5

# Step

# ↓

# Next Line

# y = 10
# 5️⃣ continue (c)

# Continue program execution until the next breakpoint or the program ends.

# (Pdb) continue
# 6️⃣ a

# Shows function arguments.

# Example

# (Pdb) a

# Output

# num1 = 4

# num2 = "hello"
# 7️⃣ w (where)

# Shows current execution stack (call stack).

# (Pdb) w

# Useful to know which function you're currently in.

# 8️⃣ Variable Inspection

# Suppose

# a = 10

# Inside PDB

# (Pdb) a

# Output

# 10

# You can directly type variable names to inspect their values.

# 9️⃣ Modify Variables

# Suppose

# Current value

# num2 = "Hello"

# Inside PDB

# (Pdb) num2 = 5

# Now execution continues using the new value.

# This is very useful for testing without editing your source code.