class Queue :
    def __init__(self):
        self.value = []

    def insert(self,data):
        self.value.append(data)

    def delete(self):
        if len(self.value) == 0 :
            print("The queue is empty")
        else:
            return self.value.pop(0)
    
    def isEmpty(self):
        if len(self.value) == 0:
            raise Exception("The queue is empty")

Q = Queue()
Q.insert(10)
Q.insert(20)
Q.insert(30)
Q.insert(40)
print(Q.delete())
print(Q.delete())
print(Q.delete())
print(Q.delete())
print(Q.delete())