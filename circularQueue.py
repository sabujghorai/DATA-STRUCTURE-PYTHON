class CircularQueue:
    def __init__(self,size):
        self.size = size
        self.item = [None]*size
        self.front = self.real = -1
        