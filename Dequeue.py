class Dequeue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def insertAtEnd(self, value):
        self.items.append(value)

    def deleteAtFront(self):
        if self.isEmpty():
            print("The Queue is empty")
            return None
        else:
            return self.items.pop(0)
        
    def insertAtFront(self, value):
        self.items.insert(0, value)

    def deleteAtEnd(self):
        if self.isEmpty():
            print("The Queue is empty")
            return None
        else:
            return self.items.pop()
    
dq = Dequeue()
dq.insertAtEnd(10)
dq.insertAtFront(20)
dq.insertAtEnd(30)
dq.insertAtEnd(40)
dq.insertAtFront(50)

print(dq.deleteAtEnd()) # delete 40 and print 40
print(dq.deleteAtEnd()) # delete 30 and print 30
print(dq.deleteAtFront()) # delete 50 and print 50
print(dq.deleteAtFront()) # delete 20 and print 20
print(dq.deleteAtFront()) # delete 10 and print 10
dq.deleteAtFront() # print The queue is empty
dq.deleteAtEnd() # print The queue is empty