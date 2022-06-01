"""
    This was some code used to help study for the final over Python
"""

import sys
import os
from collections import Counter
from collections import defaultdict
import re

## Declaring a List with an implementation list
L11 = [10,20,30,40,50]


## Looping through the range of in this case the length of the list L11
for i in range(len(L11)):
    print(i)


## Part C Question #1
## This takes a List with origianl values and shows how to override a value
List1 = [10,20,30,40]
print("Part C: Question #1\n")
print("Before:", List1)
List1[3] = 100
print("After:", List1)


## Part C Question #2
## This prints a string one character at a time
string1 = 'ABCDE'

print("\nPart C: Question #2\n")
for ch in range(len(string1)):
    print(string1[ch])


## Part C Question #3
## Shows how you can use try and except to catch an error that would otherwise
## throw a runtime error when we try to access an index out of range of the list
print("\nPart C: Question #3\n")
try:
    L1 = [0] * 5
    L1[6] = 100
    print(L1)

except:
    print("***Error*** index out of range")


## Part C Question #4
## This example concatonates strings while adding in a character
print("\nPart C: Question #4\n")
routes = ['Salt Lake City', 'Dallas', 'New York', 'Los Angeles', 'Miami']
concat_str = ' -> '.join(routes)
print(concat_str)


## Part C Question #5
## Seems to return the first index only of the found character
print("\nPart C: Question #5\n")
slang = 'C@che me outside, how bout d@t'
print(slang.find('@'))
slang = 'Cache me outside, how bout d@t'
print(slang.find('@'))
slang = 'C@che me outside, how bout d@t'
placeholder = Counter(slang)
print(placeholder['@'])

## Part D Question #1
## Count the occurences of 'a' in a given string

## Using Counter (Python Library)

print("\nPart D: Question #1\n")
sample = "abcdefghabsdadvdabsg"
counter = Counter(sample)
print(counter['a'])

## Using a more manual approch
letter_count = 0

for letter in sample:
     if letter == 'a':
         letter_count += 1

print(f'There are a total of {letter_count} instances of the letter a')



## Part D Question #2
## Write a code with RegEx with regular expression to validate a username
print("\nPart D: Question #2\n")
username = 'user123!'
uname = 'user123'


if not re.match("^[a-zA-Z0-9_.+-]*$", username):
    print(f'\n{username} is not valid.\nUsernames must be alphanumeric only')

else:
    print("\n",username)
    print("Keep the change ya filthy animal")


if not re.match("^[a-zA-Z0-9_.+-]*$", uname):
    print(f'\n{username} is not valid.\nUsernames must be alphanumeric only')

else:
    print()
    print(uname)
    print("Keep the change ya filthy animal")


## Question #3
## Design a graph structure using python dictionary

class Graph:

    def __init__(self, nodeNumber):

        self.graph = defaultdict(list)
        self.nodes = nodeNumber
    
    def addEdge(self,u,v):

        self.graph[u].append(v)




## Question #4
## Read from a file and print contents
print("\nPart D: Question #5\n")

with open("PyP3.txt", "r") as Fin:
    lines = Fin.readlines()

for line in lines:
    print(line)

print()


## Question #5
## Change the style of string to all upper cased
print("\nPart D: Question #5\n")
S = "abcRFkhkj"
print(S)
S = S.upper()
print(S)


