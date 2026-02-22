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
        
    def pop(self):
        if len(self.s) == 0:
            raise Exception("The stack is empty")
        else:
            return self.s.pop(0)
        
stk = Stack()
stk.push(10)
stk.push(20)
stk.push(30)
stk.push(40)
print(stk.pop()) # delete the top element and print it which is 40
print(stk.pop()) # delete the top element and print it which is 30
print(stk.peek()) # print the top element which is now 20




class Stack :
    def __init__(self):
        self.st = []

    def push(self,value):
        self.st = [value]+self.st

    def pop(self):
        if len(self.st) == 0 :
            print("the stack is empty")
        else:
            return self.st.pop(0)

ptr = Stack()
ptr.push(10)
ptr.push(20)
ptr.push(30)
ptr.push(40)
print(ptr.st) # [40,30,20,10]
ptr.pop()
ptr.pop()
print(ptr.st) # [20, 10]