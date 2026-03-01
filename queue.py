class Queue :
    def __init__(self):
        self.value = []

    def insert(self,data):
        self.value.append(data)

    def delete(self):
        if len(self.value) == 0 :
            print("The queue is empty")
        else:
            return self.pop()