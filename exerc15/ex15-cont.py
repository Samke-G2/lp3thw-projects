# Notes on the new command learned in ex15

# Here we have some other commands  you can do with a file, i want those listed nicely for later user

print("""
.open()             - Obviously this accesses the file for use in the program (by creating a file object, seperate from the file itself)
.close()            - Closes the file. Like File -> Save .. in text editor
.read()             - Reads the contents of the file. You can assign the result to a variable.
.readlines()        - Reads just one line of a text file.
.truncate()         - Empties the file. Watch out if you care about the file.
.write('stuff')     - Writes 'stuff' to the file.
.seek(0)            - Move the read/write location to the beginning of the file.
""")
