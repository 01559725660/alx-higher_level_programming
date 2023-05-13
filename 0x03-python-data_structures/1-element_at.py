#!/usr/bin/python3
#Python - Data Structures: Lists, Tuples
#1-element_at.py

def element_at(my_list, idx):
    listlength = len(my_list) - 1 
    if (idx < 0 or idx > listlength):
       return (None)
    else:
       return (my_list[idx])      
