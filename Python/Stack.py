class Stack():

    def __init__(self):

        self.stack = []

    def Push_To_Stack(self, val):

        self.stack.append(val)

    def Pop_From_Stack(self):

        self.stack.pop(len(self.stack) - 1)

    def Show_Stack(self):

        print(self.stack)


Pile = Stack()

Pile.Push_To_Stack(6)
Pile.Push_To_Stack(5)
Pile.Push_To_Stack(4)
Pile.Push_To_Stack(3)
Pile.Push_To_Stack(2)
Pile.Push_To_Stack(1)

Pile.Show_Stack()

Pile.Pop_From_Stack()
Pile.Pop_From_Stack()

Pile.Show_Stack()