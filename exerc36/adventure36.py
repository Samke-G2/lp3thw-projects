"""
filename = adventure36.py
author: Samke_g2

This program is a text-based adventure game that gives the user choices and takes the user through different scenarios based on their inputs.
Created as part of the Exercise 36 study drill in the "Learn Python 3 the Hard Way" book by Zed Shaw.
"""
from sys import argv, exit

script, name, key = argv

# key = False

def chest_room(key):
    print(f"""
    You enter a room with a chest in the centre of it.
    The chest is locked and fixed to the floor.
    On the other side of the chest there is a door, opened a little bit.
    What do yu do?
    """)

    choice = input("> ")

    if "door" in choice and key == True:
        print("You look at the key in your hands, wondering what it does, before entering the door.")
        print("Through the door, you escape to the outside world.")
        print("You are alive and free, but without any treasure.")
        print(f"\nGood job, {name}!, YOU LOSE\n")
    elif "door" in choice and key == False:
        print("Through the door, you escape to the outside world.")
        print("You are alive and free, but without any treasure.")
        print(f"\nGood job, {name}, YOU LOSE!\n")
    elif "open" in choice and not key == False:
        print("The chest is locked and you cannot open it without a key.")
        print("You try to open it until you're exhausted, then you starve to death.")
        print(f"\nGood job, {name}!\n")
    elif "open" in choice and key == True:
        print("You use the key to open the chest.")
        print("Inside you find the most valuable diamond in tte world.")
        print("After retrieving it, you enter throught the open door and escape to the outside world.")
        print("You are alive, free, and unimaginably rich.")
        print(f"\nGood job, {name}, YOU WIN!\n")
    else:
        print("You trip, fall, and hit your head on hte chest.")
        print("You die almost immediately.")
        print(f"\nGood job, {name}!\n")


chest_room(key)
