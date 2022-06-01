"""
    Name: Byron Dowling
    Class: 4143 Programming Techniques
    Date: 11/03/2021

    To-Do List:
        - Regex

    in-class
        - regular expressions
        - matching and extracting data with regex
        - validating input with regex from problem #2, last program
"""

import sys
import os
import re           ## Regex Header


## Entire person details + a username of an email address


## Function for printing the output as part of question #2 of the assignment
def PrintTable(F_Name, L_Name, age, Prof, Snum, Snam, Cit, Sta, Z, count, E_Address):
    print("The details for person", count, "is as follows:")
    print()
    print(F_Name, L_Name)
    print("Age:", age)
    print("Occupation:", Prof)
    print("Email:", E_Address)
    print("Address:", Snum, Snam, Cit, Sta, Z)



print("How many people do you wish to enter the details for?")
people = int(input())
print()
count = 1

while people > 0:

    ## Condition will stay true until correct input is entered and the segment breaks out of loop
    while True:
        
        try:
            print("Enter the First Name of person #", count)
            Fname = str(input())
            print()

        except:
            raise ValueError('Please enter a valid first name.')
            print()

        if Fname.isnumeric():
            Message = ValueError("Invalid Input, your input contains numeric values.")
            print(Message)
            print()
            continue

        else:
            break



    ## Condition will stay true until correct input is entered and the segment breaks out of loop
    while True:
        try:
            print("Enter the Last Name of person #", count)
            Lname = str(input())
            print()

        except:
            raise ValueError('Please enter a valid last name.')
            print()

        if Lname.isnumeric():
            Message =  ValueError("Invalid Input, name contains numeric values")
            print(Message)
            print()
            continue

        else:
            break


    ## Condition will stay true until correct input is entered and the segment breaks out of loop
    while True:
            try:
                print("Enter the Age of person #", count)
                Age = input()
                print()

            except ValueError:
                raise ValueError("Your input is not valid, please enter an integer value.")
                print()

            ## Checking if numeric using Regex
            if not re.search("(^[0-9]+$)",Age):
                Message = ValueError("Age must be numeric")
                print(Message)
                print()
                continue

            else:
                Age = int(Age)

                if Age < 0 or Age > 150:
                    Message = ValueError("Please enter a REALISTIC age")
                    print(Message)
                    print()
                    continue

                else:
                    break


    ## Condition will stay true until correct input is entered and the segment breaks out of loop
    while True:
        try:
            print("Enter the Occupation of person #", count)
            Occupation = str(input())
            print()

        except:
            raise ValueError("Invalid Input, please try again")
            print()

        if Occupation.isnumeric():
            Message = ValueError("Please enter Occupation using non-numerical values")
            print(Message)
            print()
            continue

        else:
            break


    ## Condition will stay true until correct input is entered and the segment breaks out of loop
    while True:
        try:
            print("Enter the Email Address of person #", count)
            E_Address = str(input())
            print()

        except:
            raise ValueError("Invalid Input, please try again")
            print()

        ## Regex error checking
        if not re.match("(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$)",E_Address):
            Message = ValueError("Please enter the email address including the domain. I.E @gmail.com")
            print(Message)
            print()
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
            print()

            print("Next enter the Street name:")
            Street_name = input()
            print()

            print("Next enter the city:")
            City = input()
            print()

            print("Next enter the state:")
            State = input()
            print()

            print("Finally, enter the zip code:")
            Zip = input()
            print()


        except ValueError:
            raise ValueError("Your input was invalid.")
            print()


        if not re.search("(^[0-9]+$)",Street_num):
            Message = ValueError("Street # must be numeric.")
            print(Message)
            print()
            continue
        
        elif not re.search("(^[a-zA-z])",City):
            Message = ValueError("City cannot contain numbers.")
            print(Message)
            print()
            continue

        elif not re.search("(^[a-zA-z])",City):
            Message = ValueError("State cannot contain numbers.")
            print(Message)
            print()
            continue

        elif not re.search("(^[0-9]+$)",Zip):
            Message = ValueError("Zip Code must be numeric.")
            print(Message)
            print()
            continue

        else:
            Street_num = int(Street_num)
            City = str(City)
            State = str(State)
            Zip = int(Zip)
            break


    ## Function to print the results in a nicer format
    PrintTable(Fname, Lname, Age, Occupation, Street_num, Street_name, City, State, Zip, count, E_Address)

    ## Iterate the count and the people count to control the loop and reference which person
    count = count + 1
    people = people - 1