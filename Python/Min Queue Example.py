"""
    Name: Byron Dowling
    Class: 4143 Programming Techniques
    Date: 11/17/2021

    in-class
        - Queues
        - implement a min queue
"""

class Min_Queue():

    def __init__(self):

        self.min = float('inf')
        self.Q = []


    def enqueue(self, stuff):

        if stuff < self.min:
            
            self.min = stuff
            self.Q.append(stuff)

        else:

            self.Q.append(stuff)


    def dequeue(self):
        
        temp = self.Q[0]
        self.Q.pop(0)

        if temp == self.min:

            self.min = float('inf')

            for i in self.Q:

                if i < self.min:

                    self.min = i


    def rear(self):
        
        if self.Q is not None:

            return self.Q[-1]


    def front(self):            ## Returning the front of queue
        
        if self.Q is not None:

            return self.Q[0]


    def getMin(self):           ## Returning the min value
        
        return self.min


    def Show_Q(self):           ## Printing the Queue

        print(self.Q)
        print()



## New Queue object
Q1 = Min_Queue()

## Adding values to the Queue
Q1.enqueue(1)
Q1.enqueue(11)
Q1.enqueue(21)
Q1.enqueue(31)
Q1.enqueue(41)

## Printing the Queue
Q1.Show_Q()
print("Front of Queue:", Q1.front())
print("Back of Queue:", Q1.rear())
print("Current min is:", Q1.getMin())
print()

## Popping items from the Queue
Q1.dequeue()
Q1.dequeue()

## Adding more elements to the Queue
Q1.enqueue(17)
Q1.enqueue(81)
Q1.enqueue(13)
Q1.enqueue(51)
Q1.enqueue(7)

## Printing the new Queue results
Q1.Show_Q()

print("Front of Queue:", Q1.front())
print("Back of Queue:", Q1.rear())
print("Current min is:", Q1.getMin())