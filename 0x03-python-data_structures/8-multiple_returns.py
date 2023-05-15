#!/usr/bin/python3
#Python - Data Structures: Lists, Tuples
#8-multiple_returns.py

def multiple_returns(sentence):
    if len(sentence) == 0:
        my_tuple = (0, None)
    else:
        my_tuple = (len(sentence), sentence[:1])
    return(my_tuple)
