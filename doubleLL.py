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

    def printDLL(self):
        t = self.head
        while(t.next != None):
            print(t.data)
            t = t.next
        print(t.data)

obj  = DoubleLL()
obj.insertAtTheEnd(10)
obj.insertAtTheEnd(20)
obj.insertAtTheEnd(30)
obj.InsertAtBegeining(5)
obj.printDLL()