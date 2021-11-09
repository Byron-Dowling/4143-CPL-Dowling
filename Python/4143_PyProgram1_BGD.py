"""
    Name: Byron Dowling
    Class: 4143 Programming Techniques
    Date: 10/23/2021
    Assignment: Programming Assignment #3

    Details:
        - Problem #1
            - Design a rocket and print to the screen
            - This was accomplished by drawing up something in a separate text doc
              and then when I was done, I used the multi-line print functionality of
              Python by doing: 

                  print(''' 
                            *multiple lines here* 
                            *multiple lines here*
                        ''')

        - Problem #2
            -Capture user input for:
                    - First Name
                    - Last Name
                    - Age
                    - Occupation
                    - Address
            
            - I accomplished this in part by breaking up the address into mulitple
              entries such as street number, street, city, state, and zip.


        - Problem #3
            - Implememnt a Python equivalent of the stoi (string to integer) function
              found in C++
            - Handle various nuances such as if the number is negative or positive
              and if the number over flows 


"""

import sys
import os
import random


"""
    $$$$$$$\                      $$\       $$\                                 $$\ $$\    $$\   
    $$  __$$\                     $$ |      $$ |                                $$ \$$ \ $$$$ |  
    $$ |  $$ | $$$$$$\   $$$$$$\  $$$$$$$\  $$ | $$$$$$\  $$$$$$\$$$$\        $$$$$$$$$$\\_$$ |  
    $$$$$$$  |$$  __$$\ $$  __$$\ $$  __$$\ $$ |$$  __$$\ $$  _$$  _$$\       \_$$  $$   | $$ |  
    $$  ____/ $$ |  \__|$$ /  $$ |$$ |  $$ |$$ |$$$$$$$$ |$$ / $$ / $$ |      $$$$$$$$$$\  $$ |  
    $$ |      $$ |      $$ |  $$ |$$ |  $$ |$$ |$$   ____|$$ | $$ | $$ |      \_$$  $$  _| $$ |  
    $$ |      $$ |      \$$$$$$  |$$$$$$$  |$$ |\$$$$$$$\ $$ | $$ | $$ |        $$ |$$ | $$$$$$\ 
    \__|      \__|       \______/ \_______/ \__| \_______|\__| \__| \__|        \__|\__| \______|
                                                                                                                                                                                                                                                                                        
"""


print(
'''

                                            **
                                           ****
                                          //  \\
                                         **    **
                                        //      \\
                                       ** ______ **
                                      // //    \\ \\
                                     ** // ---- \\ **
                                    // //________\\ \\
                                    **---------------**
                                    **---------------**
                                    **   $$\   $$\   **
                                    **   $$$\  $$ |  **
                                    **   $$$$\ $$ |  **
                                    **   $$ $$\$$ |  **
                                    **   $$ \$$$$ |  **
                                    **   $$ |\$$$ |  **
                                    **   $$ | \$$ |  **
                                    **   \__|  \__|  **          
                                    **               **             
                                    **   $$$$$$\     **
                                    **   $$  __$$\   **
                                    **   $$ /  $$ |  **
                                    **   $$$$$$$$ |  **
                                    **   $$  __$$ |  **
                                    **   $$ |  $$ |  **
                                    **   $$ |  $$ |  **
                                    **   \__|  \__|  **
                                    **               **         
                                    **    $$$$$$\    **
                                    **   $$  __$$\   **
                                    **   $$ /  \__|  **
                                    **   \$$$$$$\    **
                                    **    \____$$\   **
                                    **   $$\   $$ |  **
                                   /**   \$$$$$$  |  **\
                                  / **    \______/   ** \
                                 /  **               **  \
                 _______________/  /**    $$$$$$\    **\  \_______________
                /                 / **   $$  __$$\   ** \                 \
               /      ___________/  **   $$ /  $$ |  **  \___________      \
              /      /              **   $$$$$$$$ |  **              \      \
             /       |              **   $$  __$$ |  **               |      \
            /        |              **   $$ |  $$ |  **               |       \
           /         \              **   $$ |  $$ |  **               /        \
          /           \             **   \__|  \__|  **              /          \
         |____________|             **               **              |___________|
       $  $  $  $  $  $             **---------------**             $  $  $  $  $  $
      $  $  $  $  $  $              **---------------**              $  $  $  $  $  $
     $  $  $  $  $  $               |_________________|               $  $  $  $  $  $
    $  $  $  $  $  $               /                   \               $  $  $  $  $  $
   $  $  $  $  $  $               /   [] [] [] [] []    \               $  $  $  $  $  $
                                 /   [] [] [] [] [] []   \
                                /_________________________\
                               $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $
                              $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $
                               $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ 
                                $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $
                                 $ $ $ $ $ $ $ $ $ $ $ $ $ $ $ $
                                  $ $ $ $ $ $ $ $ $ $ $ $ $ $
                                 $ $ $ $ $ $ $ $ $ $ $ $ $ $
                                  $ $ $ $ $ $ $ $ $ $ $ $ $
                                   $ $ $ $ $ $ $ $ $ $ $ $
                                     $ $ $ $ $ $ $ $ $ $
                                     $ $ $ $ $ $ $ $ $
                                      $ $ $ $ $ $ $ $
                                       $ $ $ $ $ $ $
                                        $ $ $ $ $ $
                                         $ $ $ $ $  
    
    
    
'''
)



"""
    $$$$$$$\                      $$\       $$\                                 $$\ $$\    $$$$$$\  
    $$  __$$\                     $$ |      $$ |                                $$ \$$ \  $$  __$$\ 
    $$ |  $$ | $$$$$$\   $$$$$$\  $$$$$$$\  $$ | $$$$$$\  $$$$$$\$$$$\        $$$$$$$$$$\ \__/  $$ |
    $$$$$$$  |$$  __$$\ $$  __$$\ $$  __$$\ $$ |$$  __$$\ $$  _$$  _$$\       \_$$  $$   | $$$$$$  |
    $$  ____/ $$ |  \__|$$ /  $$ |$$ |  $$ |$$ |$$$$$$$$ |$$ / $$ / $$ |      $$$$$$$$$$\ $$  ____/ 
    $$ |      $$ |      $$ |  $$ |$$ |  $$ |$$ |$$   ____|$$ | $$ | $$ |      \_$$  $$  _|$$ |      
    $$ |      $$ |      \$$$$$$  |$$$$$$$  |$$ |\$$$$$$$\ $$ | $$ | $$ |        $$ |$$ |  $$$$$$$$\ 
    \__|      \__|       \______/ \_______/ \__| \_______|\__| \__| \__|        \__|\__|  \________|
                                                                                                                                                                                                                                                                                                    
"""

## Function for printing the output as part of question #2 of the assignment
def PrintTable(F_Name, L_Name, age, Prof, Snum, Snam, Cit, Sta, Z, count):
    print()
    print("The details for person", count, "is as follows:")
    print(F_Name, L_Name)
    print("Age:", age)
    print("Occupation:", Prof)
    print("Address:", Snum, Snam, Cit, Sta, Z)



"""
    Start of the prompts for user details. First it asks for how many people
    and then that value sets the while loop.

    Then Each followup question has a while loop that is set to True which
    will make it loop indefinitely until the user enters a correct input which
    will execute the break statement and exit the loop.

    Each question has ValueError "catchers" in the try/except blocks to catch
    any improper input and make the user try again.

"""


print("How many people do you wish to enter the details for?")
people = int(input())
count = 1

while people > 0:

    ## Condition will stay true until correct input is entered and the segment breaks out of loop
    while True:
        try:
            print("Enter the First Name of person #", count)
            Fname = str(input())

        except:
            raise ValueError('Please enter a valid first name.')

        if Fname.isnumeric():
            Message = ValueError("Invalid Input, your input contains numeric values.")
            print(Message)
            continue

        else:
            break



    ## Condition will stay true until correct input is entered and the segment breaks out of loop
    while True:
        try:
            print("Enter the Last Name of person #", count)
            Lname = str(input())

        except:
            raise ValueError('Please enter a valid last name.')

        if Lname.isnumeric():
            Message =  ValueError("Invalid Input, name contains numeric values")
            print(Message)
            continue

        else:
            break


    ## Condition will stay true until correct input is entered and the segment breaks out of loop
    while True:
            try:
                print("Enter the Age of person #", count)
                Age = input()

            except ValueError:
                raise ValueError("Your input is not valid, please enter an integer value.")

            if not Age.isnumeric():
                Message = ValueError("Age must be numeric")
                print(Message)
                continue

            else:
                Age = int(Age)

                if Age < 0 or Age > 150:
                    Message = ValueError("Please enter a REALISTIC age")
                    print(Message)
                    continue

                else:
                    break


    ## Condition will stay true until correct input is entered and the segment breaks out of loop
    while True:
        try:
            print("Enter the Occupation of person #", count)
            Occupation = str(input())

        except:
            raise ValueError("Invalid Input, please try again")

        if Occupation.isnumeric():
            Message = ValueError("Please enter Occupation using non-numerical values")
            print(Message)
            continue

        else:
            break

    """
        Condition will stay true until correct input is entered and the segment breaks out of loop.

        Additionally, this While Loop takes the address and breaks it up into the individual components
        that makes up an address such as the street number, street name, city, state, zip. This allows
        us to judge the correctness of each element to identify which is the culprit if input is incorrect.

            - Input is initially captured as plain input
            - It is then evaluated if it fits the desired category
            - If it doesn't match the desired input, an error is thrown
            - If no error is thrown, then it is cast to its desired type, int, str, etc.

            - The continue statement in the ValueError forces the loop to start over
            - This poses the question again and starts the process over.
            - If the input is correct, the break statement exits the loop
    """
    while True:
        try:
            print("Enter the Full Address Details of person #", count)
            print("Start by entering the Street Number:")
            Street_num = input()

            print("Next enter the Street name:")
            Street_name = input()

            print("Next enter the city:")
            City = input()

            print("Next enter the state:")
            State = input()

            print("Finally, enter the zip code:")
            Zip = input()


        except ValueError:
            raise ValueError("Your input was invalid.")


        if not Street_num.isnumeric():
            Message = ValueError("Street # must be numeric.")
            print(Message)
            continue
        
        elif City.isnumeric():
            Message = ValueError("City cannot contain numbers.")
            print(Message)
            continue

        elif State.isnumeric():
            Message = ValueError("State cannot contain numbers.")
            print(Message)
            continue

        elif not Zip.isnumeric():
            Message = ValueError("Zip Code must be numeric.")
            print(Message)
            continue

        else:
            Street_num = int(Street_num)
            City = str(City)
            State = str(State)
            Zip = int(Zip)
            break


    ## Function to print the results in a nicer format
    PrintTable(Fname, Lname, Age, Occupation, Street_num, Street_name, City, State, Zip, count)

    ## Iterate the count and the people count to control the loop and reference which person
    count = count + 1
    people = people - 1



"""
    $$$$$$$\                      $$\       $$\                                 $$\ $$\    $$$$$$\  
    $$  __$$\                     $$ |      $$ |                                $$ \$$ \  $$ ___$$\ 
    $$ |  $$ | $$$$$$\   $$$$$$\  $$$$$$$\  $$ | $$$$$$\  $$$$$$\$$$$\        $$$$$$$$$$\ \_/   $$ |
    $$$$$$$  |$$  __$$\ $$  __$$\ $$  __$$\ $$ |$$  __$$\ $$  _$$  _$$\       \_$$  $$   |  $$$$$ / 
    $$  ____/ $$ |  \__|$$ /  $$ |$$ |  $$ |$$ |$$$$$$$$ |$$ / $$ / $$ |      $$$$$$$$$$\   \___$$\ 
    $$ |      $$ |      $$ |  $$ |$$ |  $$ |$$ |$$   ____|$$ | $$ | $$ |      \_$$  $$  _|$$\   $$ |
    $$ |      $$ |      \$$$$$$  |$$$$$$$  |$$ |\$$$$$$$\ $$ | $$ | $$ |        $$ |$$ |  \$$$$$$  |
    \__|      \__|       \______/ \_______/ \__| \_______|\__| \__| \__|        \__|\__|   \______/ 
                                                                                                                                                                                                                                                                                      

    Essentially my stoi function functions similar to that of the C++ variant.
    First a string value is read from a file and passed in one at a time to the
    function. Each number case is worked and then return to the calling loop.

    To determine the int value:
        - I have a bool to keep track if the number is positive, and a Temp string
          variable to keep track of our number substring.

        - There are conditions to catch if the string starts with characters that
          are not allowed and would then throw and early exit.
        
        - If those early exits do not occur, I loop through the length of the string
          character by character until we only grab the numbers while also keeping 
          a look out for if there is a postive or negative sign.

        - Once this process is complete. We convert the temp string to an int
          and then determine if you need to flip the number negative.

        - Finally there is an if statement to determine if the number overflowed
          standard FP32 max limits. If so, the max number is thrown adn printed.

"""
def mystoi(Str):
    Positive = True

    InVal = ""


    if len(Str) < 1:
        print("String is Empty!")
        print(0)

    if (Str[0] > " " and Str[0] < '0' and Str[0] is not '+' and Str[0] is not '-'):
        print("Result is:",0)
        return

    if (Str[0] > '9'):
        print("Result is",0)
        return

    for i in range(0, len(Str), 1):

        if Str[i] == '-':
            Positive = False

        if Str[i] >= '0' and Str[i] <= '9':
            InVal += Str[i]




    if Positive == False:
        InVal = int(InVal)
        InVal = InVal * -1

        if InVal < ((2**32)-1) * -1:

            InVal = -2147483648
            print("Result is",InVal)
            return

        else:
            print("Result is:",InVal)
            return

    elif int(InVal) > ((2**32)-1):
        InVal = 2147483647
        print("Result is:",InVal)
        return
        

    else:
        InVal = int(InVal)
        print("Result is:",InVal)
        return




Fin = open("Py1_input.txt", "r")

for itr in Fin:
    print("Value read from file is:",itr)
    mystoi(itr)
    print()


## Close the file once we are done
Fin.close()
