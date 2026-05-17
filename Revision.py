# Array
from array import *
values = array("i",[1,2,3,4,5,7,6,9,8])
for i in range(0,len(values)):
    print(values[i],end=" ")

# stack 
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


Stack = []
Stack.append(10)
Stack.append(20)
Stack.append(30)
Stack.append(40)
print(Stack)

Stack.pop()
Stack.pop()
print(Stack)


# Queue
class Queue:

    def __init__(self):
        self.q = []

    def enqueue(self,value):
        self.q.append(value)

    def dequeue(self):
        return self.q.pop(0)

    def peek(self):
        return self.q[0]

q = Queue()

q.enqueue(10)
q.enqueue(20)
q.enqueue(30)

print(q.dequeue())
print(q.peek())


# Recursion 

# write a program to find the sum of n natural number