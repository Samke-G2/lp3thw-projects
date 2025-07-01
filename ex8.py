# Exercise 8 -  Printing, printing, printing

# Here we create a string with curly braces where i want to insert other values in future when i format the string
formatter = "{} {} {} {}"

# The next five lines format the formatter with different values in the curly braces
print(formatter.format(1, 2, 3, 4))
print(formatter.format('one', 'two', 'three', 'four'))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "words escape me",
    "ideas resist me",
    "wild and free",
    "rebelling against harmony", end="/n"
))
