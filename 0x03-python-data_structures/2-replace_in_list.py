#!/usr/bin/python3
#Python - Data Structures: Lists, Tuples
#2-replace_in_list.py

def replace_in_list(my_list, idx, element):
   listlength = len(my_list) - 1
   if (idx < 0 or idx > listlength):
      return(None)
   else:
      my_list[idx] = element
      return (my_list)
