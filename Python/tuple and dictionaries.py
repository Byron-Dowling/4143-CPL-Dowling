"""
    Name: Byron Dowling
    Class: 4143 Programming Techniques
    Date: 11/01/2021

    To-Do List:
        - Tuples
        - Dictionaries

    in-class
        - regular expressions
"""

import sys
import os
import re

## Character to ASCII
print(ord('A'))

HT1 = {}     ## Empty Dictionary

HT2 = {101: 'Prime', 103: 'Numbers', 113: 'Are', 119: 'Cool'}

print(HT2)

tp = ('Steve', 'Woodrow', 'Cornelius')
print(tp)

try:
    ## Tuples are immutable so this command will not work
    ## Unlike a list, once you create a tuple, you cannot alter its contentes
    ## Similar to a string
    tp[1] = 'Byron'


except:
    print("Sorry, Tuples are immutable, that won't work")