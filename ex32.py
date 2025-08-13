"""
Exercise 32 - Loops and Lists
author: Samke_g2

Building some lists using some for - loops and printing them out
"""
the_count = [1, 2, 3, 4, 5]
fruits = ["apples", "oranges", "pears", "apricots"]
change = [1, "pennies", 2, "dimes", 3, "quarters"]

# this first kind of for-loops goes through a lists
for number in the_count:
    print(f"This is count {number}")

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# also we can go through mixed lists too
for i in change:
    print(f"I got {i}")

# we can also build lists, first start with an empty one
# One of the study drills is to avoid using the for loop to add numbers to the elements list by assigning range directly to it
elements = list(range(0, 6))

# # then use the range function to do o to 5 counts
# for i in range(0, 6):
#     print(f"Adding {i} to the list.")
#     # append is a function that lists understand
#     elements.append(i)

# now we can print them out too
for i in elements:
    print(f"Element was: {i}")
