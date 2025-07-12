# Exercise 20 - Functions and Files

# import argv
from sys import argv

# unpack argv
script, input_file = argv


# define a function that prints the whole file (read() + print())
def print_all(f):
    print(f.read())

# define a function that resets where the file is read (like rewinding a casette tape)
def rewind(f):
    # the '.seek()' method resets where we start reading the file, the '0' there is th first (like ina index) byte in the file being read.
    f.seek(0)

# define a function that prints just a single line in the file.
# function takes 2 arguments (the line number we want to display, and the file being read)
def print_a_line(line_count, f):
    # The print statement prints the number we input as the first parameter of the function, then the line of the file being read.
    # the .'readline()' method displays only a single line in the file. it increments itself everytime we call it
    print(line_count, f.readline())         # adding " ,end='' " at the end of the print function will eliminate teh double spaces displayed when we run the 'print_a_line' function

# create a variable wherein we open the file.
current_file = open(input_file)


# statement describing what we'll be preinting
print("First let's print whole file: \n")
# call the function that prints the whole file
print_all(current_file)

# statement describing that we're resetting the state(index) of file reading
print("Now let's rewind, kind of like a tape.")
# call the function that rewinds the file
rewind(current_file)

# Statement dscribing what we'll be printing
print("Let's print three lines: ")

# initialise a variable for the line of the file we want to display
current_line = 1
# call the function that prints one line of the file, passing into it the current line variable so it is displayed first before the line.
print_a_line(current_line, current_file)

# Increment(add one to) the current file variable
current_line += 1       # therefore, current line = 2
# call the function that prints one line of the file, passing into it the INCREMENTED current line variable so it is displayed first before the line.
print_a_line(current_line, current_file)

# Increment(add one to) the current file variable
current_line += 1       # therefore, current line = 3
# call the function that prints one line of the file, passing into it the INCREMENTED current line variable so it is displayed first before the line.
print_a_line(current_line, current_file)


# close the file
current_file.close()
