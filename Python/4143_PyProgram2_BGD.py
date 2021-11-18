"""
    Name: Byron Dowling
    Class: 4143 Programming Techniques
    Date: 10/23/2021
    Assignment: Programming Assignment #4

    Details:
        - Problem #1
            - (35 points) Write a Python program using file operation. You will open an input file
             “students.dat” that will contain a list of student names, classification, and grade in the
             class. (All student info is completely made up) You should read through the entire input
             file. After reading in all information, do operations (No built-in functions like Average,
             min, max, count, etc.), close the input file and write that following information with
             labels to an output file “student_statistics.txt”

                • Highest grade in the class
                • Lowest grade in the class
                • Class average grade (rounded to one decimal place)
                • Number of freshmen students
                • Number of sophomore students
                • Number of junior students
                • Number of senior students

        - Problem #2
            - (35 points) Given an array of strings strs, group the anagrams together. You can return the
              answer in any order.

              An Anagram is a word or phrase formed by rearranging the letters of a different word or
              phrase, typically using all the original letters exactly once.

                    - Input type: A list with words;
                    - Output type: A list of lists with grouping the anagrams together

            Note: You cannot use any built-in functions. You can have only string, tuples, dictionaries
            to solve this problem. Follow the instructions that I have mentioned during the class.


        - Problem #3
            - (30 points) Write the OOP program in python using class. Assuming you have four
              classes: Bank account which is the parent class and it has two child classes Saving
              Account class and Checking account class. Customer is another class who has a bank
              account; either saving or checking or both. Implement the scenario using python OOP
              and make sure you have covered those OOP concepts on your code: inheritance(any),
              polymorphism (runtime and compile time), abstraction and encapsulation.


"""

import copy                             ## Header File needed for Deep Copy
from abc import abstractmethod, ABC     ## For Abstract Classes and Methods


"""
  $$$$$$\                                  $$\     $$\                             $$\ $$\    $$\   
 $$  __$$\                                 $$ |    \__|                            $$ \$$ \ $$$$ |  
 $$ /  $$ |$$\   $$\  $$$$$$\   $$$$$$$\ $$$$$$\   $$\  $$$$$$\  $$$$$$$\        $$$$$$$$$$\\_$$ |  
 $$ |  $$ |$$ |  $$ |$$  __$$\ $$  _____|\_$$  _|  $$ |$$  __$$\ $$  __$$\       \_$$  $$   | $$ |  
 $$ |  $$ |$$ |  $$ |$$$$$$$$ |\$$$$$$\    $$ |    $$ |$$ /  $$ |$$ |  $$ |      $$$$$$$$$$\  $$ |  
 $$ $$\$$ |$$ |  $$ |$$   ____| \____$$\   $$ |$$\ $$ |$$ |  $$ |$$ |  $$ |      \_$$  $$  _| $$ |  
 \$$$$$$ / \$$$$$$  |\$$$$$$$\ $$$$$$$  |  \$$$$  |$$ |\$$$$$$  |$$ |  $$ |        $$ |$$ | $$$$$$\ 
  \___$$$\  \______/  \_______|\_______/    \____/ \__| \______/ \__|  \__|        \__|\__| \______|
      \___|                                                                                                                                                                                                                                                                                        


        Pretty straightforward as I read in the data into a custom object
        and appended them to a list. Then as I looped through that list, I
        kept track of key variables such as highest grade, lowest grade, etc
        until we reached the end and then wrote those results to a file.

"""


## Custom Object Properties
Student = {
    "F_Name": "",
    "L_Name": "",
    "Classification": "",
    "Grade": 0
}


## Empty List Declaration
Students = []

with open ("students.txt", "r") as Fin:
    lines = Fin.readlines()             ## Read all lines as one variable

    for line in lines:                  ## Read through the lines individually
        temp = line.split()

        ## Capturing user details to a new objects
        Student['F_Name'] = temp[0]
        Student['L_Name'] = temp[1]
        Student['Classification'] = temp[2]
        Student['Grade'] = int(temp[3])

        ## Appending object to list and making sure it's a deep copy
        ## and not a shallow copy that could potentially corrupt data
        ## *** This happened to me in Database on my MongoDB API ***
        Students.append(copy.deepcopy(Student))


## Statistic Variables
Highest_Grade = 0
Lowest_Grade = 100
Class_Average = float()
RT = 0
Num_Fresh = 0
Num_Soph = 0
Num_Jun = 0
Num_Sen = 0
Student_Count = len(Students)
Overachiever = ""
Underachiever = ""


## Looping through our list of Objects
for obj in Students:

    RT = RT + obj['Grade']

    if obj['Grade'] > Highest_Grade:
        Highest_Grade = obj['Grade']

    if obj['Grade'] < Lowest_Grade:
        Lowest_Grade = obj['Grade']

    if obj['Classification'] == "freshman":
        Num_Fresh = Num_Fresh + 1

    elif obj['Classification'] == "sophomore":
        Num_Soph = Num_Soph + 1

    elif obj['Classification'] == "junior":
        Num_Jun = Num_Jun + 1

    elif obj['Classification'] == "senior":
        Num_Sen = Num_Sen + 1


Class_Average = RT / Student_Count


## Determine which student had which grade
for i in Students:
    if i['Grade'] == Highest_Grade:
        Overachiever = i['F_Name'] + " " + i['L_Name']

    if i['Grade'] == Lowest_Grade:
        Underachiever = i['F_Name'] + " " + i['L_Name']


## File Write destination
Fout = open("student_statistics.txt", "w")

## Writing our results to a file using file write f strings
Fout.write(f'Highest Grade is: {Highest_Grade} achieved by: {Overachiever}\n')
Fout.write(f'Lowest Grade is: {Lowest_Grade} achieved by perennial dissapointment: {Underachiever}\n')
Fout.write(f'Class Average: {Class_Average}\n')
Fout.write(f'Freshman: {Num_Fresh}\n')
Fout.write(f'Sophomores: {Num_Soph}\n')
Fout.write(f'Juniors: {Num_Jun}\n')
Fout.write(f'Seniors: {Num_Sen}\n')


## Close files
Fin.close
Fout.close


"""
  $$$$$$\                                  $$\     $$\                             $$\ $$\    $$$$$$\  
 $$  __$$\                                 $$ |    \__|                            $$ \$$ \  $$  __$$\ 
 $$ /  $$ |$$\   $$\  $$$$$$\   $$$$$$$\ $$$$$$\   $$\  $$$$$$\  $$$$$$$\        $$$$$$$$$$\ \__/  $$ |
 $$ |  $$ |$$ |  $$ |$$  __$$\ $$  _____|\_$$  _|  $$ |$$  __$$\ $$  __$$\       \_$$  $$   | $$$$$$  |
 $$ |  $$ |$$ |  $$ |$$$$$$$$ |\$$$$$$\    $$ |    $$ |$$ /  $$ |$$ |  $$ |      $$$$$$$$$$\ $$  ____/ 
 $$ $$\$$ |$$ |  $$ |$$   ____| \____$$\   $$ |$$\ $$ |$$ |  $$ |$$ |  $$ |      \_$$  $$  _|$$ |      
 \$$$$$$ / \$$$$$$  |\$$$$$$$\ $$$$$$$  |  \$$$$  |$$ |\$$$$$$  |$$ |  $$ |        $$ |$$ |  $$$$$$$$\ 
  \___$$$\  \______/  \_______|\_______/    \____/ \__| \______/ \__|  \__|        \__|\__|  \________|
      \___|                                                                                                                                                                                                                                                                                                      


        Essentially my approach to solving this without the obvious built in function
        is to create a second list and alphabetically sort each individual item of the
        first list. Then I create a third list by initializing it to a copy of the second
        list and then I reduce it to only the unique values. then I loop through this list 
        of unique values and look for matches in the sorted list. when I find a match, I have
        the original string list and the sorted string list set up to where they share parellel
        indexes so when a match is found in the sorted list, I grab that index and push that index
        of the original strings into an empty list to finally be pushed to the final result of
        anagrams. 

        So to summarize:
            - One list strs is the original strings
            - Results list is the final list of anagram pairs
            - A temp list str_chars to capture the words
            - A list sorted_strs that holds the original list but with each string in
              alphabetical order
            - A list called listcopy that takes a copy of sorted_strs and reduces to
              only the unique values within that list.

"""

strs = ["eat","tea","tan","ate","nat","bat"]

sorted_strs = []
Results = []

for s in strs:

    str_chars = []

    x = len(s)

    for i in range (0,x):
        str_chars.append(s[i])


    for i in range(0,x):

        for j in range(0,x):

            if str_chars[i] < str_chars[j]:

                temp = str_chars[i]
                str_chars[i] = str_chars[j]
                str_chars[j] = temp

    j = ""

    for i in range(0,x):
        j = j + str_chars[i]

    sorted_strs.append(j)


listcopy = []
listcopy = sorted_strs

listcopy = list(set(listcopy))


print("Original strings:", strs)
print("Sorted strings:", sorted_strs)
print("Minimized Copy:", listcopy)

for i in range(0, len(listcopy), 1):

    temp = []

    for j in range(0, len(sorted_strs), 1):

        if listcopy[i] == sorted_strs[j]:

            temp.append(strs[j])

    
    Results.append(temp)
    

print("Anagram Pairs:", Results)



"""
  $$$$$$\                                  $$\     $$\                             $$\ $$\    $$$$$$\  
 $$  __$$\                                 $$ |    \__|                            $$ \$$ \  $$ ___$$\ 
 $$ /  $$ |$$\   $$\  $$$$$$\   $$$$$$$\ $$$$$$\   $$\  $$$$$$\  $$$$$$$\        $$$$$$$$$$\ \_/   $$ |
 $$ |  $$ |$$ |  $$ |$$  __$$\ $$  _____|\_$$  _|  $$ |$$  __$$\ $$  __$$\       \_$$  $$   |  $$$$$ / 
 $$ |  $$ |$$ |  $$ |$$$$$$$$ |\$$$$$$\    $$ |    $$ |$$ /  $$ |$$ |  $$ |      $$$$$$$$$$\   \___$$\ 
 $$ $$\$$ |$$ |  $$ |$$   ____| \____$$\   $$ |$$\ $$ |$$ |  $$ |$$ |  $$ |      \_$$  $$  _|$$\   $$ |
 \$$$$$$ / \$$$$$$  |\$$$$$$$\ $$$$$$$  |  \$$$$  |$$ |\$$$$$$  |$$ |  $$ |        $$ |$$ |  \$$$$$$  |
  \___$$$\  \______/  \_______|\_______/    \____/ \__| \______/ \__|  \__|        \__|\__|   \______/ 
      \___|                                                                                            
                                                                                                                                                                                                               
"""

## Parent/Super Class with Abstract Method/s

class Bank_Account(ABC):


    def __init__(self, AN = None, Bal = None):

        if not AN is None:
            self.Account_Number = AN

        if not Bal is None:
            self.Balance = Bal


    def Set_Balance(self, Bal):             ## Setter method i.e abstraction

        self.Balance = Bal

    def Set_Account_Number(self, AN):       ## Setter method i.e abstraction

        self.Account_Number = AN


    def Get_Balance(self):                  ## Getter method i.e abstraction
                                            ## Data is indirectly accessed via a method
        return self.Balance

    def Get_Account_Number(self):           ## Getter method i.e abstraction
                                            ## Data is indirectly accessed via a method
        return self.Account_Number


    def Deposit(self, DA):

        self.Balance = self.Balance + DA

    @abstractmethod                         ## Abstract method to be implemented later
    def Transfer_Money(self):
        
        pass



## Savings Account (Child Class) inherits from Bank Account (Super)

class Saving_Account(Bank_Account):

    __Annual_IR = float()

    def __init__(self, AN = None, Bal = None, AIR = None):

        super().__init__(AN, Bal)

        if not AIR is None:

            self.__Annual_IR = AIR

        else:

            self.__Annual_IR = 0.06

    def Set_Interest_Rate(self, IR):            ## Setter method i.e abstraction

        self.__Annual_IR = IR

    def Get_Interest_Rate(self):                ## Getter method i.e abstraction
                                                ## Data is indirectly accessed via a method
        return self.__Annual_IR


    def Transfer_Money(self, PA,):                ## Overriding the Inherited Transfer Money Method
                                                  ## I.E Runtime Polymorphism
        
        print()
        print("Current Balance of Checking Account:", self.Balance)   
        self.Balance = self.Balance - PA
        print("New Balance of Checking Account:", self.Balance) 




## Checking Account (Child Class) inherits from Bank Account (Super)

class Checking_Account(Bank_Account):
    
    __Annual_IR = float()
    Overdrawn = False
    Overdraw_fee = 35.00

    def __init__(self, AN = None, Bal = None, AIR = None):

        super().__init__(AN, Bal)

        if not AIR is None:

            self.__Annual_IR = AIR

        else:

            self.__Annual_IR = 0.03

    def Set_Interest_Rate(self, IR):                               ## Setter method i.e abstraction

        self.__Annual_IR = IR

    def Get_Interest_Rate(self):                                   ## Getter method i.e abstraction
                                                                   ## Data is indirectly accessed via a method
        return self.__Annual_IR

    def Transfer_Money(self, PA):           ## Overriding the Inherited Transfer Money Method
                                                                   ## I.E Runtime Polymorphism
        
        print()
        print("Current Balance of Checking Account:", self.Balance)   
        self.Balance = self.Balance - PA
        print("New Balance of Checking Account:", self.Balance) 




## Customer Class that contains instances of both the Checking Account
## and the Savings Account classes as well as its own specific variables

class Customer:

    Name = ""
    SSN = ""
    Age = int()
    Credit_Score = int()

    ## Encapsulation by having objects as Class Variables
    C1 = Checking_Account("123456789", 5476.12)
    S1 = Saving_Account("987654321", 1000.00)


    def __init__(self, name, social, age, CS):

        if not name is None:
            self.Name = name

        else:
            self.Name = "John Doe"


        if not social is None:
            self.SSN = social


        if not age is None:
            self.Age = age


        if not CS is None:
            self.Credit_Score = CS

        else:
            self.Credit_Score = 700


    def Deposit_Money(self, Amount):

        print()
        print("Current Balance:", self.C1.Balance)
        try:
            Amount = float(Amount)

            self.C1.Deposit(Amount)
            print("New Balance:", self.C1.Balance)

        except:

            print("Invalid Amount")


    def Transfer_From_Checking(self, Amt):

        self.C1.Transfer_Money(Amt)

    
    def Transfer_From_Savings(self, Amt):
    
        self.C1.Transfer_Money(Amt)

    
    def Get_Details(self):
        
        print()
        print("Name:", self.Name)
        print("SSN#:", self.SSN)
        print("Age:", self.Age)
        print(f'Checking Account# {self.C1.Account_Number} Balance:', self.C1.Balance)
        print(f'Savings Account# {self.S1.Account_Number} Balance:', self.S1.Balance)
    
        

## Creating a new customer object
Cust1 = Customer("Dominik Szoboszlai", "123-12-1234", 21, 742)


## Callimg the Customer method to deposit money
Cust1.Deposit_Money(100.75)


## Calling the Customer method and passing it an instance of an Account object
## so that the Customer object can transfer money from its account into the account
## of the Bank Account object
Cust1.Transfer_From_Checking(250.00)
Cust1.Transfer_From_Savings(500.00)
Cust1.Get_Details()


