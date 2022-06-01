
x = 5
y = 7

"""
    Simple If statements below including less than, greater than,
    not equal and equal statements.
"""
if x < 10:
    print('X is Smaller than 10')

x = 27

if x > 20:
    print('X is now Larger than 20')

if x != y:
    print('X and Y are not equal')

y = x

if x == y:
    print('X and Y are now equal')

status = False

if (status != True):
    print('Status is False\n')



"""
    If/ElseIf example from input below
    Tested with various examples. Also use a boolean operator/expression
    to ensure that the if is separate from the elif and separate from the
    else statement.

    Also use a for loop to execute this 3 different times to satisfy the
    in class requirements.
"""

for i in range (0,3):
    print('\nPlease enter a number:')
    ##num = input()                 ## This captures as a string 
    ##num = int(input())
    num = float(input())            ## This casts as a float so we can do number comparison properly
                                    ## Could have done int as well but I tested with floats as well

    print('You have entered: ', num)

    ## If statement with boolean && (and) condition to limit each statement execution
    if num > 50 and num < 100:
        print('Number entered is greater than 50')

    ## else if condition
    elif num > 100:
        print('Number is greater than 100')

    ## if number is less than 50
    else:
        print('Number is less than 50')


"""
    While loop:

    The while loop promtps the user to enter an integer value and tells them that
    to stop the process type in zero. If you enter anything other than an integer value
    such as a string or a float, the try/except section will catch the error and gently
    remind the user to type in an INTEGER value. There's also a line of code to print
    what was typed in.

    In Class:
        - Asked us to find the summation of digits leading up to a number
        - check if the input is valid 
            - then keep the running total of them down to zero
"""

stuff = -1

while stuff != 0:
    print('\nPlease enter an integer number and see what happens ***Its not really that exciting***')
    print('To stop, type in 0')

    try:
        stuff = int(input())
        if stuff != 0:
            print('You entered: ', stuff, " exciting stuff!")
    except:
        print("Oops, that won't work.\nPlease enter an INTEGER value :) ")


sum_num = -1
RT = 0
valid_input = False

while sum_num != 0:
    if valid_input == False:
        print('\nNow enter an integer value and we will perform the summation of this number')
        try:
            sum_num = int(input())
            valid_input = True

        except:
            print("Please enter an INTEGER value")
    else:
        RT += sum_num
        sum_num -= 1

print('Summation is:',RT)
