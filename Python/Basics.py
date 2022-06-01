""" 
     Author: Byron Dowling
     Course: CMPS 4143 Contemporary Programming Languages 
     Semester: Fall 2021
     Assignment: In-Class Assignment: Python Hello World and variable casting
     Date: 10/11/2021

        - Declare three types of variables, integer, float, and string
        - Convert each into a different variable type and print the result
        - Print the type of variable at each interval
        - Print the length using len()
        - input capture
        - string concatenation
"""

## Variable Declaration of different types:

x = '3.1416'        ## String Declaration
y = 12              ## Int declaration
z = '1234'          ## String Declaration

fNum = 12.24        ## Float Declaration

print("Mathematical Pi is: " + x)

## Converting to a string
var1 = str(y)
var4 = type(fNum)               ## Printing the type of variable
print(var4)



## Converting to a float
var2 = float(x)


## Converting to an integer
var3 = int(z)

print(var1)                     ## Printing var1 which went from an Int to String
print(var2)                     ## Printing var2 which went from a String to a Float
print(var3)                     ## Printing var3 which went from a String to an Int


## While Loop Example Below
num = 5

while num > 0 :
    print(num)
    num = num - 1

print("Blast Off!!")


## if/else example

status = False

if status == True:
    print("Status is true")

else:
    print("Status is false")


## Mathematical operations Below:

exNum = 31
val1 = exNum // 2       ## Integer Division
val2 = exNum / 2        ## Regular Division
print(val1, val2)


powR = 2**8             ## Powers: i.e. 2^8
print(powR)


print(float('inf'))     ## Positive Infinity: Checking for
print(float('-inf'))    ## Negative Infinity: Checking for



## Grabbing input

print("Enter your name please")
name = input()                      ## Works like a getline()
print("Hello " + name + "!")
print("Enter your age and SSN")
age = input()
ssn = input()
print("You are " + age + " years old and you are also foolish for giving me your SSN of " + ssn)


## String Concatenation

fname = "Cornelius "
lname = "Vanderschmidt"

fullname = fname + lname        ## Adding them together, String Concatenation
print(fullname)
length = len(fullname)          ## Length of the new Concatenated String

print("Length of last string is: ", length)     ## Printing result