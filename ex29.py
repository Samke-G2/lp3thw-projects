"""
Exercise 29 - What if
author: Samke_G2 (all exercises in this repo should be assumed to be typed by me under the direction of the "Learn Python 3 The Hard Way" book by Zed Shaw)

This particular exercise seems to be a practice exercise on 'if' statements combined with the use of booleans.
"""
people = 20
cats = 30
dogs = 15


if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")


dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")
