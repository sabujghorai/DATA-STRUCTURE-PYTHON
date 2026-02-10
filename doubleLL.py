
# Insert at the end....

class Node:
    def __init__(self,value = None):
        self.data = value
        self.next = None
        self.prev = None

class DoubleLL:
    def __init__(self):
        self.head = None

    def insertAtTheEnd(self,value): # Insert at the End
        temp = Node(value)
        if(self.head == None):
            self.head = temp
            return
        
        t = self.head
        while(t.next != None):
            t = t.next

        t.next = temp
        temp.prev = t

    def insertAtTheBeg(self,value): # Insert at the begeining
        temp = Node(value)
        if(self.head == None):
            self.head = temp
            return
        temp.next = self.head
        self.head.prev = temp
        self.head = temp

    def inserAtTheMid(self,value,x):
        t = self.head

        while(t.next != None):
            if(t.data == x):
                break
            else:
                t = t.next
        temp = Node(value)
        temp.next = t.next
        t.next.prev = temp
        t.next = temp



    def printDLL(self):
        t = self.head
        while(t.next != None):
            print(t.data,end = " <--> ")
            t = t.next
        print(t.data)

obj = DoubleLL()
obj.insertAtTheEnd(10)
obj.insertAtTheEnd(20)
obj.insertAtTheEnd(30)
obj.insertAtTheEnd(40)
obj.insertAtTheBeg(5)
obj.printDLL()