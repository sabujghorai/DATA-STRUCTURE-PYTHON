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

# # write a program to find the sum of n natural number
def sum(a):
    if(a == 0):
        return 0
    return a+sum(a-1)

a = int(input("Enter the number of turms :"))
print("The sum of your n number of term is :",sum(a))

# Write a program using recursion to print the factorial of a number n take input from the user
def factorial(b):
    if(b == 0):
        return 1
    return b*(factorial(b-1))
b = int(input("Enter the number you want to find factorial :"))
print("The factorial of your number is : ", factorial(b))



# SingleLinked list 

class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

node1.next = node2
node2.next = node3
node3.next = node4

n1 = node1
while(n1 != None):
    print(n1.data,end=" --> ")
    n1 = n1.next
print("None")


# Insert at the end
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class SingleLL :
    def __init__(self):
        self.head = None

    def insertAtEnd(self,value):
        temp = Node(value)

        if self.head is None:
            self.head = temp
        else:
            t1 = self.head
            while t1.next is not None:
                t1 = t1.next
            t1.next = temp 

    