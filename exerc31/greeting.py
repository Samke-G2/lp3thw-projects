"""
file: greeting.py
author: Samke_G2

This file is created as part of the exercise 31 study drills where I have to create my own "choose your own adventure" type
file that uses if statements and code branches to got to a solution in several small steps.
"""
print("""
This program helps you figure out if you should say hi to someone you know, and have just seen, in several steps.
We start at an inital question and go from there,
let's get started..

Do I say 'Hi'?
""")

print("Do you remember the person's name? (yes/no)")
name = input("> ").lower()

if name == "yes":
    print("\nIs it an ex? (yes/no)")
    ex = input("> ").lower()

    if ex == "yes":
        print("\nAre you drunk? (yes/no)")
        drunk = input("> ").lower()

        if drunk == "no":
            print("\nAre you in a convertible with Michael B. Jordan and/or Rihanna? (yes/no)")
            convertible = input("> ").lower()

            if convertible == "yes":
                print("\n Say hi. \n")

            elif convertible == "no":
                print("\n Don't say hi. \n")
            else:
                pass

        elif drunk == "yes":
            print("\nDo you want to rekindle? (yes/no)")
            rekindle = input("> ").lower()

            if rekindle == "yes":
                print("\n Say hi. \n")

            elif rekindle == "no":
                print("\n Don't say hi. \n")

            else:
                pass
        else:
            pass


    elif ex == "no":
        print("\nA friend's ex? (yes/no)")
        frex = input("> ").lower()

        if frex == "yes":
            print("\n Don't say hi. \n")

        elif frex == "no":
            print("\nAn enemy or frenemy? (yes/no)")
            enmity = input("> ").lower()

            if enmity == "yes":
                print("\nAre you in a convertible with Michael B. Jordan and/or Rihanna? (yes/no)")
                convertible = input("> ").lower()

                if convertible == "yes":
                    print("\n Say hi. \n")

                elif convertible == "no":
                    print("\n Don't say hi. \n")

                else:
                    pass

            elif enmity == "no":
                print("\nAre you robbing a bank? (yes/no)")
                robbery = input("> ").lower()

                if robbery == "yes":
                    print("\n Don't say hi. \n")

                elif robbery == "no":
                    print("\nAre you in a bathrobe? (yes/no)")
                    bathrobe = input("> ").lower()

                    if bathrobe == "yes":
                        print("\n Don't say hi. \n")

                    elif bathrobe == "no":
                        print("\n Say hi. \n")
                    else:
                        pass
                else:
                    pass
            else:
                pass
        else:
            pass
    else:
        pass

elif name == "no":
    print("\nIs there time to flee? (yes/no)")
    flee = input("> ").lower()

    if flee == "yes":
        print("\n Run for it! \n")

    elif flee == "no":
        print("\nCould you pretend to get a call on your phone? (yes/no)")
        phone = input("> ").lower()

        if phone == "yes":
            print("\n Hello, doctor. What are my test results? \n")

        elif phone == "no":
            print("\nAre you wearing sunglasses? (yes/no)")
            sunglasses = input("> ").lower()

            if sunglasses == "yes":
                print("\n Just keep walking. \n")

            elif sunglasses == "no":
                print("""
                Address the person using an amusing nickname
                such as "Bro", "Bafo", or "Chommie".
                """)

            else:
                pass
        else:
            pass
    else:
        pass

else:
    print(f"{name} is not a valid input")
