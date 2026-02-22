class Queue :
    def __init__(self):
        self.q = []

    def isEmpty(self):
        return len(self.q) == 0