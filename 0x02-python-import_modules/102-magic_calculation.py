#!/usr/bin/python3
# Fibonacci numbers module
# 102-magic_calculation.py

from magic_calculation_102 import add, sub
def magic_calculation(a, b):

    if a < b:
        c = add(a, b)
        for i in range (4, 6):
            c = add(a, b)
            return(c)
        else:
            return(sub(a, b))
