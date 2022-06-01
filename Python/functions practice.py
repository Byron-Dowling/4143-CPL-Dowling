"""
    Name: Byron Dowling
    Class: 4143 Programming Techniques
    Date: 10/20/2021

    To-Do List:
        - functions
        - fibonacci function
        - Overtime Pay Calculator
"""

import sys
import os
import random


## Overtime Pay Calculator
def GrossPay(hours, hourly_rate):
    if hours > 40:
        OT = float(hours - 40)

        OT_pay = float(OT * (hourly_rate * 1.5))

        return float(((hourly_rate * 40) + OT_pay))

    else:
        return float(hours * hourly_rate)



## Fibonacci Function
## 1 2 3 4 5 6  7  8  9
## 1 1 2 3 5 8 13 21 34 
def Fibonacci(n):


    if n < 0:
        print("That's not valid input")
 
    elif n == 0:
        return 0

    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)



## Addition Function
def addition(x1, y1):
    print('\n')
    return x1 + y1




print("Please enter your hours worked and your hourly rate")
HW, HR = input().split()
print(GrossPay(float(HW), float(HR)))

print("\nEnter a number to find the fibonacci number: ")
val = int(input())

print(Fibonacci(val)) # return the recursive value number


print("\nPlease enter two numbers with a space between.")
x, y = input().split()


try:
    x = int(x)
    y = int(y)

    print(addition(x, y))


except:
    print("That won't work you silly goose")

