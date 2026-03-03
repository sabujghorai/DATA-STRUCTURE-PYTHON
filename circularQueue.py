class CircularQueue:
    def __init__(self,size):
        self.size = size
        self.item = [None]*size
        self.front = self.real = -1

    def Enqueue(self,value): # code for insertion
        if ((self.rear + 1)% self.front ):
            print("The queue is full")
        elif self.front == -1 : # checks the queue is empty ot not
            self.front = self.rear = 0
            self.item[self.rear] = value
        else:
            self.rear = (self.rear +1) % self.size
