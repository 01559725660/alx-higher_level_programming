#!/usr/bin/python3
#3-print_alphabt.py

for letter in range(97, 123):
        """that prints the ASCII alphabet, in lowercase, not followed by a new line."""
   if chr(letter) != 'q' and chr(letter) != 'e':
       print("{}".format(chr(letter)),end="")
