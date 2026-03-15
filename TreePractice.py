# Write a function that returns the number of nodes in a binary tree.
class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.data = value

def count_Node(root):
    if(root == None):
        return 0
    count_left = count_Node(root.left)
    count_right = count_Node(root.right)

    return 1+count_left+count_right
