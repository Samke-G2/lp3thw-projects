# Exercise 10 - escape sequences in strings

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a new line."
backslash_cat = "I'm \\ a \\ cat"

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)


print("ESCAPE SEQUENCES: ")
print("""
Here are some escape sequences Python supports.
You may not use many of these, but memorise their format and what they do anyway.
""")
print(" \\ - For printing a backslash, one just gets ignored.")
print(" \' - For printing a single-quote, so as to not prematurely end a string created with single-quotes.")
print(" \" - For Double-quotes, so as to not prematurely end a string created with double-quotes.")
print(" \a - ASCII bel (BEL)")
