# Exercise 19 - Functions and variables

# Created "defined" a function that takes 2 arguments (parameters)
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # Prints the value of the first parameter in an f-string
    print(f"You have {cheese_count} cheeses!")
    # Prints the value of the secpnd parameter in an f-string
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    # prints anothe statement
    print("Man that's enough for a party!")
    # prints one final statement, with a linebreak at the end, so the lines that come after are displayed after an open line
    print("Get a blanket. \n")

# A statement that explains the parameters input in the function
print("We can just give the function numbers directly:")
# runs the function with 20 and 3o as the first and second parameters, respectively.
cheese_and_crackers(20, 30)

# A statement that explains the parameters input in the function
print("OR, we can use variables from our script:")
# the next two lines initialise variables for amount of cheeses and amount of crackers
amount_of_cheese = 10
amount_of_crackers = 50
# run the function with the 2 newly initialised variables as the parameters
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


# A statement that explains the parameters input in the function
print("We can even do math inside too:")
# run the function with a calculation in place of a single number as each parameter
cheese_and_crackers(10 + 20, 5 + 6)


# A statement that explains the parameters input in the function
print("And we can combine the two, variables and math:")
# run the function with a mix of variable and calculation as each parameter
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
