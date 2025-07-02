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
# single-quotes can be used instead of double-quotes for this part, they work hte same
print('''
Here are some escape sequences Python supports.
You may not use many of these, but memorise their format and what they do anyway.
''')
print(" \\ - For printing a backslash, one just gets ignored.")
print(" \' - For printing a single-quote, so as to not prematurely end a string created with single-quotes.")
print(" \" - For Double-quotes, so as to not prematurely end a string created with double-quotes.")
print(" \a - ASCII bel (BEL)")      # "ASCII" refers to the American Standard Code for Information Interchange,  which is a character encoding standard.
print(" \b - ASCII backspace (BS)")
print(" \f - ASCII formfeed (FF)")                  # This one just displays the female sign (stationary) instead of a formfeed(whatev that is), I think lp3thw is based on a outdated version
print(" \n - ASCII linefeed (LF)")
print(" \N{COPYRIGHT SIGN} - For a character named 'COPYRIGHT SIGN' in the Unicode database (Unicode only)")
print(" \r - For Carriage Return (CR)")
print(" \t - For horizontal tab (TAB)")
print(" \u0394 - For a character with 16-bit hex value '0394'")
print(" \U00002122 - For a character with 32-bit hex value '00002122'")
print(" \v - ASCII vertical tab (VT)")              # This one just displays the male sign (motile) instead of a vertical tab, I think lp3thw is based on a outdated version
print(" \251 - For a character with octal value '251'")
print(" \x41 - For a character with hex value '41'")
