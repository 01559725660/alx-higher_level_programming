#!/usr/bin/python3
def write_file(filename="", text=""):
   """writes a string to a text file
   Args:
       filename(str): filename
       text(str): text to write
   Returns:
       number of characters written
   """
   with open(filename, "w", encoding="UTF-8") as f:
       return f.write(text)
