"""
Exercise 41 - Learning to speak Object-oriented
author: Samke_g2

This is a simple script you should be able to figure out,
and the only thing it does is use a library called urllib
to download a list of words.
"""
import random
from urllib.request import urlopen
import says

WORD_URL = "https://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%",
    "class %%%(object): \n\tdef __inti__(self, ***)":
        "class %%% has-a __inti__ that takes self and *** as params.",
    "class %%%(object):\n\tdef ***(self, @@@)":
        "class %%% has-a function *** that takes self and @@@ as params.",
    "*** = %%%()":
        "Set *** to an instance of class %%%.",
    "***.***(@@@)":
        "From *** get the *** function, call it with params self, @@@.",
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."
}

# do they want to drill phrases first
