class CircularQueue:
    def __init__(self):
        self.value = []
    
    def insert(self,data):
        self.value.append(data)

    def delete(self):
        if len(self.value) == 0:
            raise Exception("The queue is empty")
        else :
            self.value.pop(0)
    
    