"""
Exercise 24 - More practice
author: samke_g2

This is a practice exercise to recap all the other exercises done until this point and practice the important stuff.
"""

print("Let's practice everything.")
print('You\'d need to know \'bout escape with \\ that do:')
print("\n newlines and \t tabs.")

poem = """
\tThe lovely world
with logic is so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""
# Line 18 has a double tab and it move the line further right than the tab escape in line 13.

print("--------------")
print(poem)
print("--------------")

five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates
# The function returns three values, assigned in that order to any we call it to (like unpacking the argv method)



start_point = 10000
# Here we assign the values returned by the function to three different variables IN ONE LINE!
beans, jars, crates = secret_formula(start_point)

# Remember that this is another way to format a string
# the '.format()' method does what the 'f' at the beginning of a string does, just that the formatted bits need to be arguments of the method instead of directly in the string
print("With a starting point of: {}".format(start_point))
# It's just like with an f-string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

# Here we modify the starting point slightlty from the original, like reassigning it basically
start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)

# this is an easy way to apply a list to format string
# Like it says, we apply a list to a format string, but now we bypass the need for variable names to carry the values returned by the function
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
