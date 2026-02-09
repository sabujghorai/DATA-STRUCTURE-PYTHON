class Node:
    def __init__(self,value = None):
        self.data = value
        self.next = None
        self.prev = None

class DoubleLL:
    def __init__(self):
        self.head = None

    def insertAtTheEnd(self,value):
        temp = Node(value)
        
    