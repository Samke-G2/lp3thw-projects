"""
Exercise 30 - Else and If
author: Samke_G2

In this exercise I practice the else-if statements. It's just to reinforce the concept of branches and conditionals, it think.
"""
# These three lines declare a variable for the cars, people, and trucks respectively
people = 30
cars = 15
trucks = 15


# The first if statement checks whether there are more people than cars
if cars < people:
    # If there are more people than cars, this is printed
    print("We should take the cars.")
# If the previous block doesnt run, we check if there are more cars than people
elif cars > people:
    # This next block runs if there are more cars than people
    print("We should not take the cars.")
#If the first two blocks don't run, we run this this third with the 'else'
else:
    # If the first two blocks don't run, we print this one
    print("We can't decide")

# This if statement checks whether there are more trucks than cars
if trucks > cars:
    # If there are more trucks than cars, this is printed
    print("That's too many trucks.")
# If the previous block doesnt run, this checks if there are more cars than trucks
elif trucks < cars:
    # This next block runs if there are more cars than trucks
    print("Maybe we could take the trucks.")
#If the first two blocks don't run, we run this this third with the 'else'
else:
    # If the first two blocks don't run, we print this one
    print("We still can't decide.")

# This if statement checks whether there are more people than trucks
if people > trucks:
    # If there are more people than trucks, this is printed
    print("Alright, let's just take the trucks.")
#If the first block doesn't run, we run this this third with the 'else'
else:
    # This code block is printed if the first part of the 'if' statement doesn't run
    print("Fine, let's stay home then.")
