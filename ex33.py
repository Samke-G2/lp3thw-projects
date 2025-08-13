"""
Exercise 33 - While Loops
author: Samke_g2

Learning while-loops while doing th three checks to make sure they don't run forever:
    1. Make sure that you use while-loops sparingly. Usually a for-loop is better
    2. Review your while statements and make sure that the boolean test will become False at some
        point.
    3. When in doubt,print out your test variable at the top and bottom of the while-loop toseewhat
        it’s doing.
"""
# i = 0
# numbers = []

def numGen(end, step):
    i = 0
    numbers = []

    while i < (end + 1):
        print(f"At the top i is {i}")
        numbers. append(i)

        i += step

        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

    return numbers

# print("The numbers: ")
#
# for num in numbers:
#     print(num)

# rewriting the function to use for-loops and range (last study drill)
def numGen2(end, step):
    i = 0
    numbers = []

    for i in range(0, end + 1, step):
        # print(f"At the top i is {i}")
        numbers. append(i)

        # i += step

        print("Numbers now: ", numbers)
        # print(f"At the bottom i is {i}")

    return numbers
