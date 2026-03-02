class CircularQueue:
    def __init__(self):
        self.value = []
    
    def insert(self,data):
        self.value.append(data)