class Node :
    def __init__(self,value):
        self.left = None
        self.right = None
        self.data = value

root = Node(1)
root.left = Node(3)
root.right = Node(5)