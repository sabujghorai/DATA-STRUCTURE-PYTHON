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
            self.item[self.rear] = value

    def Dequeue(self):
        if (self.front == -1): # checks the queue is empty or not
            print("the Queue is Empty")
        elif self.front == self.rear: # means the queue has only one element
            print(self.item[self.front])
            self.front = self.rear = -1
        else:
             print(self.item[self.front])
             self.front = (self.front + 1)% self.size

