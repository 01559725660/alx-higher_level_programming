#!/usr/bin/python3
#Python - Data Structures: Lists, Tuples
#6-print_matrix_integer.py

def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_matrix.append([number ** 2 for number in row])
    return new_matrix
