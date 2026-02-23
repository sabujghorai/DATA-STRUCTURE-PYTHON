class Queue:
    def __init__(self):
        self.qu = []

    def isEmpty(self):
        return len(self.qu) == 0
    
    def insert(self,values):
        self.qu.append(values)

    def delete(self):
        if (self.isEmpty()):
            print("The queue is empty")
        else:
            self.qu.pop(0)
q = Queue()
q.insert(10)
q.insert(20)
q.insert(30)
print(q.delete())