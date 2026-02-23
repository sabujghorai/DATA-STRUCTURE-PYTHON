class Dequeue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def insertAtEnd(self,value):
        self.items.append(value)

    def deleteAtFront(self):
        if (self.isEmpty) == 0:
            print("The Queue is empty")
        else:
            return self.items.pop(0)
        