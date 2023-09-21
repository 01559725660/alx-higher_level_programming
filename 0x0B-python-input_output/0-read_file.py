#!/usr/bin/python3
def read_file(filename=""):
    with open(filename, "r", encoding="UTF8") as f:
        print(f.read())
read_file("my_file_0.txt")
