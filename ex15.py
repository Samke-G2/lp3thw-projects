# Exercise 15 - Reading Files
# New things -->  python -m pydoc open              -type 'q' when done to exit pydoc

# imports the argv object from the sys module
from sys import argv

# unpacks the argv object so that the terminal command needs an additional argument to run the program
script, filename = argv

# This line accesses the file we want to display (the second argument in the terminal command) and assigns a variable to it (or the other way around)
txt = open(filename)

# This first line displays an f-string where the name of our file (provided in the terminal command) is added in hte string
print(f"Here's your file {filename}: ")
# This line prints our file (the one in the terminal command) using the variable assigned earier (the one created to access - "open" - the file)
print(txt.read())

# Here we print a message, a form of prompt for the next line
print("Type the filename again: ")
# Here we take input from the user. Ideally it would be the naem of a file in the same directory(folder)
file_again = input("> ")

# Here we open the new file, the one given in the input, and assign it to a variable
txt_again = open(file_again)

# Lastly, in this line we print the new file again in the termianl
print(txt_again.read())

# This code should work whether the file in the beginning is the same as the first or different.


# These next two lines close the open txt file(s). Apparently it's important to close() files once you're done working with them.
txt.close()
txt_again.close() 
