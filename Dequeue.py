class Dequeue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def insertAtEnd(self,value):
        self.items.append(value)

    
