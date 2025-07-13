"""
Exercise 21 - Functions can return something
author: Samke_G2
last modified: 13/07/2025

Intro to the return statement of functions.
"""

def add(a, b):
    print(f"ADDING {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"SUBTRACTING {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"MULTIPLYING {a} * {b}")
    return a * b

def divide(a, b):
    print(f"DIVIDING {a} / {b}")
    return a / b


print("Let's do some math with just functions!")

age = add(20, 6)
height = subtract(2, 0.49)
weight = multiply(25, 2)
iq = divide(100, 2)

print(f"Age: {age}, \nHeight: {height}, \nWeight: {weight}, \nIQ: {iq}")


# A puzzle for the extra credit, type it in anyway
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")
