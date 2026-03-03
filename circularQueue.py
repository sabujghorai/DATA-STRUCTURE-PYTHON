class CircularQueue:
    def __init__(self,size):
        self.size = size
        self.item = [None]*size
        self.front = self.real = -1

    def Enqueue(self,value): # code for insertion
        if ((self.rear + 1)% self.front ):
            print("The queue is full")
        