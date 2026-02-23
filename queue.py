class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0
    
    def insert(self,values):
        self.items.append(values)

    def delete(self):
        if (self.isEmpty()):
            print("The queue is empty")
        else:
            self.items.pop(0)
q = Queue()
q.insert(10)
q.insert(20)
q.insert(30)
print(q.delete())