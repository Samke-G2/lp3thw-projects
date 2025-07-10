# Exercise 16 - Reading and writing Files

# impoprts argv from the sys module
from sys import argv

# unpacks argv to require two arguments when running in the terminal
script, filename = argv

# prints a warning that the file will be erased before going further
print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit ENTER.")

# input where the user will decide what to do based on the prior info
input("?")

# If we continue, here we print that we're opening the file and then open the file.
print("Opening the file...")
# Here we open the file, the second parameter in the function call "w" specifies that we aren't just opening to read, but to write - "w" - (meanig we'll be editing and including things in the file)
target = open(filename, "w")

# Here we erase the file we just opened, using the 'truncate()' method
print("Truncating the file. Goodbye! ")
target.truncate()

# prints a prompt informing the user to prepare 3 lines to include in the file
print("Now I'm going to ask you for three lines.")

# Each input is a line that will be added to the file
line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

# Writes each input line into the file, while writing a linebreak after each

# target.write(line1)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

# This line is an improved, shortened version of the last 6, completed as part of the study drills 
target.write(f"{line1} \n {line2} \n {line3} \n")

# A prompt to tell the user that we're closing the file...and then we close it with "close()"
print("And finally, we close it.")
target.close()
