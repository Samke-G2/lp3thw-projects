# Exercise 9 - More printing, printing, printing

# Here we create a variable storing the days of the week, in one line seperated by a space
days = "Mon Tue Wed Thu Fri Sat Sun"
# Here we create a variable storing the months, each on a different line with the '\n' character
months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug\nSep\nOct\nNov\nDec"

# Here we display the day variable after a short string explaining what is beng displayed
print("Here are the days: ", days)
# Here we displayb the months after a short string explaining what is being displayed
print("Here are the months: ", months)

# Here we display multiple lines at once using the three double-quotes
# This format is best for displaying paragraphs, what is printed in between is displayed exactly as printed with each space, tab (indent) exactly as it appears in the code
print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")
