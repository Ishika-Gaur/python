# Definition

# Existing data delete nahi hota.

# Naya data end me add hota hai.

with open("test.txt","a") as file:

    file.write(" Python")

# Mode  	Meaning
# x	    Create a new file, error if it already exists
# w+	Read + Write, but overwrite existing file
# a+	Read + Append, writes at the end and creates the file if needed
# rb	Read binary files (images, PDFs, videos)
# wb	Write binary files
# ab	Append to binary files