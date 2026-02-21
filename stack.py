class Stack:
    def __init__(self):
        self.s = [] # making a list of stack named s which is empty

    def length(self):
        return len(self.s)
    
    def push(self,value): # to insert element at top
        self.s.insert(0,value)

    def peek(self): # TO see the top element
        if len(self.s) == 0 :
            raise Exception("The stack is empty")
        else:
            return self.s[0]