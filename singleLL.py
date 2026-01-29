class Node:
    def __init__(self,data,next = None):
        self.data = data
        self.next = next

# creating a node
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)
node4 = Node(40)

# connecting the nodes
node1.next = node2
node2.next = node3
node3.next = node4

# printing the nodes
n1 = node1
while(n1 != None):
    print(n1.data,end = " -> ")
    n1 = n1.next
print("None")


# New linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLL:
    def __init__(self):
        self.head = None

    def insertAtTheEnd(self, value):
        temp = Node(value)

        if self.head is None:
            self.head = temp
        else:
            t1 = self.head
            while t1.next is not None:
                t1 = t1.next
            t1.next = temp   # linking the new node

    def printLL(self):
        t1 = self.head
        while t1 is not None:
            print(t1.data)
            t1 = t1.next


obj = SingleLL()
obj.insertAtTheEnd(10)
obj.insertAtTheEnd(20)
obj.insertAtTheEnd(30)
obj.insertAtTheEnd(40)
obj.printLL()


# Insert at the begeining
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleLL:
    def __init__(self):
        self.head = None

    def insertAtTheEnd(self, value):
        temp = Node(value)
        if self.head is None:
            self.head = temp
        else:
            t1 = self.head
            while t1.next is not None:
                t1 = t1.next
            t1.next = temp   # linking the new node

    def insertAtBeg(self,value): # inserts the value at the begeing
        temp = Node(value) 
        temp.next = self.head # prints the value --> 5
        self.head = temp # prints the other values

    def printLL(self):
        t1 = self.head
        while t1 is not None:
            print(t1.data)
            t1 = t1.next


obj = SingleLL()
obj.insertAtTheEnd(10)
obj.insertAtTheEnd(20)
obj.insertAtTheEnd(30)
obj.insertAtTheEnd(40)
obj.insertAtBeg(5)
obj.printLL()


