class CircularQueue:
    def __init__(self,size):
        self.size = size
        self.item = [None]*size
        self.front = self.rear = -1

    def enqueue(self,value): # code for insertion
        if ((self.rear + 1) % self.size == self.front ):
            print("The queue is full")
        elif self.front == -1 : # checks the queue is empty ot not
            self.front = self.rear = 0
            self.item[self.rear] = value
        else:
            self.rear = (self.rear +1) % self.size
            self.item[self.rear] = value

    def dequeue(self):
        if (self.front == -1): # checks the queue is empty or not
            print("the Queue is Empty")
        elif self.front == self.rear: # means the queue has only one element
            print(self.item[self.front])
            self.front = self.rear = -1
        else:
             print(self.item[self.front])
             self.front = (self.front + 1)% self.size

CQ = CircularQueue(4)
CQ.enqueue(10)
CQ.enqueue(20)
CQ.enqueue(30)
CQ.enqueue(40)
CQ.enqueue(50)