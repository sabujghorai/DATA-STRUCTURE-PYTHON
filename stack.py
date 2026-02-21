class Stack :
    def __init__(self):
        self.s = []
    
    def length(self):
        return len(self.s)
    
    def push(self,value):
        return self.s.insert(0,value)
    
    def peek(self):
        if len(self.s) == 0:
            raise Exception("The stack is empty")
        else:
            return self.s[0]