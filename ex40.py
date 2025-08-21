"""
Exercise 40 - Modules, Classes, and Objects
author: Samke_g2

In this program we go through the principles of OOP (Object-oriented programming)
and what the benefits of using classes & objects are.
"""
class Song(object):

    def __init__(self, title,  lyrics):
        self.lyrics = lyrics
        self.title = title

    def sing_me_a_song(self):
        print(f"{self.title} goes like this: \n ---")
        for line in self.lyrics:
            print(line)
        print("\n")

    def name_that_song(self):
        print(f"The song is named: {self.title}.")


happy_bday = Song("Happy Birthday Song", ["Happy birthday to you",
                                            "I don't want to get sued",
                                            "So I'll stop right there"])

bulls_on_parade = Song("Bulls on parade", ["They rally around tha family",
                                            "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

twinkle = [
    "Twinkle, twinkle little star,",
    "How I wonder what you are.",
    "Up above the world the so high,",
    "Like a diamond in hte sky."
]

star = Song("Twinkle twinkle", twinkle)

itsy = [
    "Itsy bitsy spider,",
    "went up the water spout.",
    "Down came the rain",
    "and washed the spider out."
    "\n",
    "Out came the sunshine,",
    "and dried up all the rain.",
    "so itsy bitsy spider"
    "was climbing up again."
]

spider = Song("Itsy bitsy spider", itsy)
