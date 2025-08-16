"""
filename = adventure36.py
author: Samke_g2

This program is a text-based adventure game that gives the user choices and takes the user through different scenarios based on their inputs.
Created as part of the Exercise 36 study drill in the "Learn Python 3 the Hard Way" book by Zed Shaw.
"""
from sys import argv, exit

script, name = argv

key = True

def chest_room(key):
    print(f"""
    You enter a room with a chest in the centre of it.
    The chest is locked and fixed to the floor.
    On the other side of the chest there is a door, opened a little bit.
    What do you do?
    """)

    choice = input("> ")

    if ("door" in choice) and (key == True):
        print("    You look at the key in your hands, wondering what it does, before entering the door.")
        print("    Through the door, you escape to the outside world.")
        print("    You are alive and free, but without any treasure.")
        print(f"\n    Good job, {name}, YOU LOSE!\n")
    elif ("door" in choice) and (key == False):
        print("    Through the door, you escape to the outside world.")
        print("    You are alive and free, but without any treasure.")
        print(f"\n    Good job, {name}, YOU LOSE!\n")
    elif ("open" in choice) and (key == False):
        print("    The chest is locked and you cannot open it without a key.")
        print("    You try to open it until you're exhausted, then you starve to death.")
        print(f"\n    Good job, {name}!\n")
    elif ("open" in choice) and (key == True):
        print("    You use the key to open the chest.")
        print("    Inside you find the most valuable diamond in the world.")
        print("    After retrieving it, you enter through the open door and escape to the outside world.")
        print("    You are alive, free, and unimaginably rich.")
        print(f"\n    Good job, {name}, YOU WIN!\n")
    else:
        dead("""
        You trip, fall, and hit your head on the chest.
        You die almost immediately.
        """)


def fire_room():
    dead("""
    You enter a room with an angry fire demon in it.
    The demon spots you and burns you to a crisp.
    """)

def dead(reason):
    print(reason)
    print(f"Good job, {name}!")
    print("YOU LOSE!\n")

def death_room(key):
    print(f"""
    You enter a torch-lit room.
    There are two doors on either side of you.
    The door to your left is pitch black, with a bone handle.
    The door to your right is golden, with a diamond-encrusted handle.
    In front of you is a throne and on the throne sits a cloaked figure.
    """)
    print(f"""
    \"Hello, {name}.\", says the hooded man, \"I have been expecting you.\"
    \"I am Death, and I offfer you a choice.\"
    \"One of these doors leads to your escape, and the other to your demise.\"
    \"The choice is yours...\"

    What do you do??
    """)

    choice = input("> ").lower()

    if "left" in choice:
        chest_room(key)
    elif "right" in choice:
        fire_room()
    else:
        dead("Death gets annoyed at your indecision and takes your soul.")


death_room(key)
