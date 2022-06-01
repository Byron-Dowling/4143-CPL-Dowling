"""
    Name: Byron Dowling
    Class: 4143 Programming Techniques
    Date: 11/15/2021

    in-class
        - stacks
        - implement a min stack
"""


class Stack(): 

    def __init__(self):

        self.stack = []     ## Initializing empty list as stack container
        self.min = None     ## Empty min value to none


    def Push(self, item):   ## Adding a new item to the stack

        print(f'Pushing {item} to the Stack')
        print()

        self.stack.append(item)
        self.Minimum()              ## Calling the Minimum method


    def ShowStack(self):            ## Simple Print Method to show stack contents

        print("Current stack is:")
        print(self.stack)
        print()


    def Pop(self):                  ## Method for removing items from stack

        if self.isEmpty():
            print("Stack is Empty")

        else:
            print("Popping from Stack")
            return self.stack.pop()     ## List function pop, not this method pop


    def Min(self):                      ## Getter function

        return self.min


    ## Method that obtains the minimum value in stack
    def Minimum(self):

        if self.min is None:

            self.min = self.View_Top()

        else:
            if self.View_Top() < self.min:

                self.min = self.View_Top()


    ## Grab the top of the stack
    def View_Top(self):

        try:
            return self.stack[-1]

        except IndexError as e:
            print(e)


    ## Get size of the stack
    def Size(self): 

        return len(self.stack)


    ## Check if the stack is empty of not
    def isEmpty(self):

        return self.Size() == 0



## Declaring new Stack Object
S1 = Stack()

## Pushing values to the stack
S1.Push(17)
S1.Push(-47)
S1.Push(555)
S1.Push(123)

## Printing what the stack looks like thus far
S1.ShowStack()

## Showing what the Min value is
print("The Min value of the stack is:", S1.Min())
print()

## Pushing more values to the stack
S1.Push(-73)
S1.Pop()
S1.Push(-34)

## Showing again what the min is after some changes to the stack
print("The Min value of the stack is now:", S1.Min())
print()

## Printing again to show changes
S1.ShowStack()




