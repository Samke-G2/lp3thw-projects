# Exercise 6

# This line creates a variable and assigns a integer value to the variable
types_of_people = 10
# This line we creates a variable and then assigns a formatted string (f-string) to the variable, the f-string contains the previous string.
x = f"There are {types_of_people} types of people."

# The next two lines create 2 seperate variables with strings in each.
binary = "binary"
do_not = "don't"
# The next line creates an f-string and formats it with the two previously created strings
y = f"Those who know {binary} and those who {do_not}."      # string in string

# The next two lines display the created f-strings 'x' and 'y'
print(x)
print(y)

# The next two lines print reformat and redisplay the prevoisly formatted strings
print(f"I said: {x}")                                       # string in string
print(f"I also said: '{y}'")                                # string in string

# Here we create a variable and assign a boolean value to it
hilarious = False

# Here we create a variable with a format space in it, preparing to format it prior to displaying it
joke_evaluation = "Isn't that joke so funny?! {}"

# Here we display the string created in the previous line, and format it (using the .format() method)
# The result is an f-string created not wiht the f"" notation, but with a method
print(joke_evaluation.format(hilarious))

# created 2 seperate variables and assign strings to each
w = "This is the left side of..."
e = "a string with a right side."

# display two strings as one using concatenation
print(w + e)
