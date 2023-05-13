#!/usr/bin/python3
#Python - Data Structures: Lists, Tuples
#3-print_reversed_list_integer.py

def print_reversed_list_integer(my_list=[]):
    """prints all integers of a list, in reverse order."""
    if my_list:
       my_list.reverse()
    for number in my_list:
       print("{:d}".format(number))    
