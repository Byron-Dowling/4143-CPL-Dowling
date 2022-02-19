"""
    Name: Byron Dowling
    Class: 4143 Programming Techniques
    Date: 11/21/2021
    Assignment: Programming Assignment #5

    Details:
        - Problem #1
            - (35 points) A stack data structure has following functionalities like empty(), size(), top(),
              push() and pop(). See the lecture slides for the details (how it works, complexity, etc.) I
              have shown you in the class how to implement a stack using a list data structure. You
              need to implement the stack with Linkedlist data structure in python. Implement the
              stack means, all of the stack functionalities including the construction of stacks should
              present on your code.

        - Problem #2
            - (30 points) Given the expression as string str, find the duplicate parenthesis from the
              expression. Your program will output whether or not finding the duplicates, that is true 
              or false.


        - Problem #3
            - (35 points) Write a python code to find the average from a stream. The input of this
              program will receive a stream of numbers and a window size to find the moving average
              of all the numbers in the sliding window. Write your code in OOP style and solve the
              program with queue and or stack data structure.



  $$$$$$\                                  $$\     $$\                             $$\ $$\    $$\   
 $$  __$$\                                 $$ |    \__|                            $$ \$$ \ $$$$ |  
 $$ /  $$ |$$\   $$\  $$$$$$\   $$$$$$$\ $$$$$$\   $$\  $$$$$$\  $$$$$$$\        $$$$$$$$$$\\_$$ |  
 $$ |  $$ |$$ |  $$ |$$  __$$\ $$  _____|\_$$  _|  $$ |$$  __$$\ $$  __$$\       \_$$  $$   | $$ |  
 $$ |  $$ |$$ |  $$ |$$$$$$$$ |\$$$$$$\    $$ |    $$ |$$ /  $$ |$$ |  $$ |      $$$$$$$$$$\  $$ |  
 $$ $$\$$ |$$ |  $$ |$$   ____| \____$$\   $$ |$$\ $$ |$$ |  $$ |$$ |  $$ |      \_$$  $$  _| $$ |  
 \$$$$$$ / \$$$$$$  |\$$$$$$$\ $$$$$$$  |  \$$$$  |$$ |\$$$$$$  |$$ |  $$ |        $$ |$$ | $$$$$$\ 
  \___$$$\  \______/  \_______|\_______/    \____/ \__| \______/ \__|  \__|        \__|\__| \______|
      \___|                                                                                         



       Linked List Stack implementation

       Variables are declared for head, top and a stack size to help keep track
       of various functions of the class. As Nodes are created and linked into the
       Linked List/Stack, the stack size variable is incremented and the self.Top
       variable is updated so we know which value is always as the top of the stack.

       My Linked List/Stack uses a doubly Linked List format as there are next and
       previous 'pointers' implemented to assist with traversing. The previous pointers
       are particularly helpful when popping from the stack as the previous pointer more
       easily helps us determine which value is going to be the new self.Top value.            

"""

class Node:

    def __init__(self, data=None):

        self.data = data
        self.next = None
        self.prev = None

    def GetData(self):

        return self.data


class LinkedList_Stack:

    def __init__(self):

        self.head = None
        self.Stack_Size = 0
        self.Top = None


    def ShowList(self):             ## Using the string append technique to visualize list
    
        temp = self.head

        ll = str()

        while (temp is not None):

            ll += str(temp.data) + " -> " 
            temp = temp.next

        print(ll, "NULL")


    def getStackSize(self):

        return self.Stack_Size


    def Empty(self):                ## Simple function to be used to check if stack is empty

        if self.Stack_Size == 0:

            return True

        else:

            return False


    def getTop(self):

        if not self.Empty():
            
            return self.Top

        else:

            print("Stack is Empty!")
            return None


    def Push_To_Stack(self, new_data):

        if self.Empty():                ## If the stack is empty, simple create a node and link

            New_Link = Node(new_data)
            New_Link.next = None
            New_Link.prev = None
            self.head = New_Link
            self.Top = New_Link
            self.Stack_Size += 1

        else:                           ## If the stack is not empty, we have to create the new node and then 
                                        ## we traverse the list until we reach thelast element whose next pointer is null
            New_Link = Node(new_data)   ## then that's where we connect the new node that we just created. We will also
            New_Link.prev = self.Top    ## increment the stack size.
            self.Top = New_Link

            curr = self.head
            while curr.next is not None:

                curr = curr.next

            curr.next = New_Link
            New_Link.next = None
            self.Stack_Size += 1



    def Pop_Off_Stack(self):

        if not self.Empty():            ## If the stack isn't empty grab the top value and make Top.prev the new top

            New_Top = self.Top.prev
            

            Value = self.Top.data

            self.Top = New_Top
            self.Top.next = None        ## Make the new Top's next pointer = to None to break the link from previous top
            self.Stack_Size -= 1

            print(Value, "removed from the Stack.")

        else:

            print("Stack is Empty!")



LL_Stack = LinkedList_Stack()       ## New class object for our Linked List/Stack


## Pushing several values on to the stack
print()
LL_Stack.Push_To_Stack(100)
LL_Stack.Push_To_Stack(15)
LL_Stack.Push_To_Stack(113)
LL_Stack.Push_To_Stack(99)
LL_Stack.Push_To_Stack(75)
LL_Stack.Push_To_Stack(-47)
LL_Stack.Push_To_Stack(46)
LL_Stack.Push_To_Stack(7)
LL_Stack.Push_To_Stack(11)


#3 Printing current contents of the stack
LL_Stack.ShowList()
print()

## Removing some elements from the stack
LL_Stack.Pop_Off_Stack()
LL_Stack.Pop_Off_Stack()
LL_Stack.Pop_Off_Stack()
print()

## Showing the results of popping those elements from the stack
LL_Stack.ShowList()
print()




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


            This Question seemed fairly straightforward as we are looking for double
            parentheses. I set it up to read from an input file and read the results line
            by line. Each line is cast to a string and each character is read individually
            and a counter is used for both right and left parentheses to make sure we have
            a matching pair. As long as we have matching pairs and there is at least 4 or
            more we have a True status returned. 

            The directions are a bit ambiguous as double would ordinarily imply double the
            normal amount of 2 so we would only be looking for 4 but based off the assignment
            examples, double means at least 2 or more matching sets of parentheses.                                                                                                                                                                                              
"""

with open("PyP3.txt", "r") as Fin:
    Lines = Fin.readlines()


for Line in Lines:

    Left_Paren_CT = 0                                   ## Left Parentheses counter
    Right_Paren_CT = 0                                  ## Right parentheses counter

    Dub_Paren = False;                                  ## Initial status is false

    for char in Line:

        if char == '(':

            Left_Paren_CT += 1

        elif char == ')':
    
            Right_Paren_CT += 1

    if Left_Paren_CT == Right_Paren_CT:

        if Left_Paren_CT + Right_Paren_CT > 2:          ## At this point in the code we know these values are even
                                                        ## so if they're greater than 2, it's at least 4 or more
            Dub_Paren = True                            ## in even intervals of 2

    print("Double Parentheses status is:", Dub_Paren)

Fin.close()
print()


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


            This was a cool question. I reused the Min-Queue code we did in class and made
            a few tweaks to it to suit our needs here. We have the main Queue which will hold
            the numbers which are read from a file and inserted into the queue, before this takes
            place however, it reads the top value in the file and uses that as the window size. If
            not a default value is set. Once all the values are read into the queue, a second minature
            queue is created to keep track of the numbers that are factoring into the window size.
            While the main queue size is less than the window size, a count variable keeps track of
            how big it currently is which is used to calculate the average up until the window size
            is reached.

            There is also the normal queue functions available despite not being at center focus of the
            problem currently being solved.                                                                                                                                                                                                    
"""

class Avg_Queue():
    
    def __init__(self):

        self.Q = []                 ## Main Queue
        self.Averages = []          ## List of averages
        self.Window_Q = []          ## Sub Queue for window values
        self.count = 0              ## Keep track of count while less than window size
        self.window_size = 0        ## Variable tracking how many numbers factor into average



    def enqueue(self, stuff):

        self.count += 1
        self.Q.append(stuff)
        self.Compute_Avg(stuff)


    def dequeue(self):
        
        self.Q.pop(0)

    def SetWindowSize(self, num):

        if num is not None:

            self.window_size = num

        else:

            self.window_size = 3


    def Compute_Avg(self, stuff):

        RT = 0
        Avg = float(0.0)

        if len(self.Q) < self.window_size:

            for num in self.Q:

                RT += num
                self.Window_Q.append(num)

            Avg = RT / self.count
            self.Averages.append(Avg)

        else:

            self.Window_Q.pop(0)
            self.Window_Q.append(stuff)

            for num in self.Window_Q:

                RT += num

            Avg = RT / self.window_size
            self.Averages.append(Avg)



    def rear(self):
        
        if self.Q is not None:

            return self.Q[-1]


    def front(self):                    ## Returning the front of queue
        
        if self.Q is not None:

            return self.Q[0]


    def getAverages(self):              ## Returning the averages
        
        print("Average Values are:", self.Averages)
        print()


    def Show_Q(self):                   ## Printing the Queue

        print("Queue's Contents are:", self.Q)
        print()



AQ = Avg_Queue()            ## New Average Queue object
WindowSize = False          ## Variable to track if window size is read in or not

with open("PyP3_Averages.txt", "r") as Fin:

    Lines = Fin.readlines()

for Line in Lines:

    if WindowSize == False:             ## Grabbing the first value in the file to be used for Window Size
        AQ.SetWindowSize(int(Line))
        WindowSize = True

    else:
        temp = int(Line)
        AQ.enqueue(temp)


## Print Results
AQ.Show_Q()
AQ.getAverages()
