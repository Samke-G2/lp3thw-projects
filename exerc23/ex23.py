"""
Exercise 23 - Strings, Bytes, and Character Encodings
author: Samke_G2
last modified: 14/07/2025

This program is created to learn 4 things:

1. How modern computers store human languages for displaying and processing, and how python 3 calls this string.

2. How you must "encode" and "decode" Python's strings into a type called bytes.

3. How to handle errors in string and byte handling.

4. How to read code and find out what it means even if previously unseen.

*UTF-8 = Unicode Transformation Format 8 Bits
"""
import sys
script, input_encoding, error = sys.argv


def main(language_file, encoding, errors):
    line = language_file.readline()

    if line:
        print_line(line, encoding, errors)
        return main(language_file, encoding, errors)

def print_line(line, encoding, errors):
    next_lang = line.strip()
    raw_bytes = next_lang.encode(encoding, errors=errors)
    cooked_string = raw_bytes.decode(encoding, errors=errors)

    print(raw_bytes, "<===>", cooked_string)


languages = open("languages.txt", encoding="utf-8")

main(languages, input_encoding, error )
