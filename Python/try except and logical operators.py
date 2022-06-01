"""
    Name: Byron Dowling
    Class: 4143 Programming Techniques
    Date: 10/18/2021

    To-Do List:
        - use range()
        - use reversed()
        - use break/continue
        - max(), min(), sum()
        - True/False
        - None, is, is not
        - float('inf')
"""

import sys
import os
import random
import math


# for i in range(0, 20, 2):
#     print(i)

# for i in range(1, 20, 2):
#     print(i)


## Even or Odd or Zero Function
def doStuff(num):
    if num % 2 == 0:
        print("Number is even")

    elif num == 0:
        print("Number is neither even or odd")

    else:
        print("Number is odd")



infinity = float('inf')
neg_infinity = float('-inf')

List1 = [10, 20, 30, 40, 50]
List2 = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# print("Min element in list is: ", min(List2))
# print("Max element in list is: ", max(List2))
# print("Sum of elements in list is: ", sum(List2))

minimum = max(List2)
maximum = 0
running_total = 0

for a in List2:
    if a > maximum:
        maximum = a

    if a < minimum:
        minimum = a

    running_total += a


print("Min element in list is: ", minimum)
print("Max element in list is: ", maximum)
print("Sum of elements in list is: ", running_total)

    

    


## Iterators
it = 0
it2 = 0

var = None

for j in range(0, 11):
    if var is None:
        print("Var is None")

    if var is not None:
        print(var)

    var = j


## Continue Example
print("\n")
for val in List1:
    it += 1

    if val == 30:
        print("Found 30")
        continue
        ##break

    else:
        print("Didn't find 30 on iteration: ", it)


## Break example
print("\n")
for val in List2:
    it2 += 1

    if val == 4:
        print("Found 4 on iteration: ", it2)
        break
        ##continue

    else:
        print("Didn't find 4 on iteration: ", it2)


found = False

## True/False example
print("\n")
for val in List2:

    if val == 4:
        found = True

if found == True:
    print("Number was found")

else:
    print("Number was NOT found")



print("\nSelf Desctruct sequence initiated\nSelf Destruct in: ")
for tick in List2:
    if tick != 0:
        print(tick)

    else:
        print("Boom!")



print("\nPlease enter some number")
x = input()

print("You have entered ", x)



## Reverse an integer's digits

try:
    intVal = int(x)

    for i in range(0, intVal, 1):
        print(i)

    print('\n')

    for i in reversed(range(0, intVal, 1)):
        print(i)


except:
    print("You have not entered a number")



## Reverse a string entered by the user

print("\nPlease enter some word")
word = input()

print("You have entered ", x)


try:
    intVal = word

    for q in word:
        print(q)

    print('\n')

    for q in reversed(word):
        print(q)


except:
    print("You have failed")




## Grab a number from the user and check if it's even or odd by doing the function call
## Will catch an error if they don't type in an integer value

print("\nPlease enter some integer number")
num_oe = input()
print("You have entered ", num_oe)

try:
    check = int(num_oe)
    doStuff(check)

except:
    print("That's not an integer you silly goose")