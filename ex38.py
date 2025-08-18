"""
Exercise 38 - Doing Things To Lists
author: Samke_g2

A program created to practice list methods
"""
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

# while len(stuff) != 10:
#     next_one = more_stuff.pop()
#     print("Adding: ", next_one)
#     stuff.append(next_one)
#     print(f"There are {len(stuff)} items now.")

# As part of the study drills for exercise 38,
#I was challenged to redesign the while-loop section to use a for-loop instead
# It works fine, the only noticeable difference beingthat the for-loop starts adding from the fron of "more stuff", and the whil-loop does so from teh back
# I could've used negative indexing to make them almost identical, but i kept the difference as a visual reminder of which loop is running.
for i in more_stuff:
    stuff.append(i)
    print(f"Adding: {i}")
    print(f"The are {len(stuff)} items now.")
    if len(stuff) == 10:
        break
    else:
        continue

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])    # Whoa! Fancy
print(stuff.pop())
print(' '.join(stuff))  # What? cool!
print('#'.join(stuff[3:5])) # super stellar
