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

    def PrintLL(self):
        t1 = self.head
        while t1 is not None:
            print(t1.data)
            t1 = t1.next

obj = SingleLL()
obj.insertAtEnd(10)
obj.insertAtEnd(20)
obj.insertAtEnd(30)
obj.insertAtEnd(40)
obj.insertAtEnd(50)
obj.PrintLL()


# Double linked list

class Node :
    def __init__(self,value = None):
        self.data = value
        self.next = None
        self.prev = None

class DoubleLL :
    def __init__(self):
        self.head = None

    def insertAtTheEnd(self,value):
        temp = Node(value)
        if(self.head == None):
            self.head = temp
            return
        
        t = self.head 
        while(t.next != None):
            t = t.next

        t.next = temp
        temp.prev = t

    def InsertAtBegeining(self,value):
        temp = Node(value)
        if(self.head == None):
            self.head = temp
            return
        temp.next = self.head
        self.head.prev = temp
        self.head = temp

    def InsertAtMiddle(self,value,x):
        t = self.head

        while(t.next != None):
            if(t.data == x):
                break
            else:
                t = t.next
        temp = Node(value)
        temp.next = t.next
        t.next.prev = next
        t.next = temp
        temp.prev = t

    def deletionDLL(self,value): # the method for deletion the element
        if(self.head == None):
            print("The linked list is empty ")
            return
        
        t = self.head
        if(t.data == value): # code for deletion at the begeinning
            self.head = t.next
            self.head.prev = None #upto this
            return
        
        while(t.next != None): # code for deletion at the middle
            if(t.data == value):
                t.prev.next = t.next
                t.next.prev = t.prev
                return
            else:
                t = t.next # upto this
        if(t.data == value):
            t.prev.next = None
