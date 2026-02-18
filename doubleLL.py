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