# Exercise 7 - More printing

# assigns string to variable
print("Mary had a little lamb.")
# Assigns string to variable, formatting the last word in
print("It's coat was white as {}.".format('snow'))
# assigns string to variable
print("And everywhere that Mary went.")
# prints a period a set numer of times in one line (set by whatever number comes after the '*')
print("." * 10)         # What'd that do?
                        # - It displays the character multiple times, according to the number after the '*'

# next 12 lines assign string to variable
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch end = ' ' at the end. try to remove it and see what happens
        # - It stops the line from wrapping, it makes the two consecutive lines display next to each other witht he character(s) in quotes as the seperator
# Here we combine (concatenate) the strings together,
# at the end, we put the space so the next line does't display under the preceding
print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 , end8 , end9 , end10 , end11 , end12)               # Left the commas in this one to show the difference in displaying multiple vars with '+' vs ','
