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

root = Node(50)
root.left = Node(40)
root.right = Node(60)
root.left.left = Node(30)
root.left.right = Node(45)
root.right.left = Node(55)
root.right.right = Node(70)

print("The Number of Node is :",count_Node(root))

# Find the Height of a Binary Tree