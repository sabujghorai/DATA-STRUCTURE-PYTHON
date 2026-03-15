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
class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.data = value

def Height(root):
    if(root == None):
        return 0
    left_Height = Height(root.left)
    right_Height = Height(root.right)

    return 1+max(left_Height,right_Height)

root = Node(70)
root.left = Node(40)
root.right = Node(80)
root.left.left = Node(30)
root.left.right = Node(50)
root.right.left = Node(75)
root.right.right = Node(90)

print("The Height of the tree is :",Height(root))

# Write a function that returns the number of leaf nodes (nodes with no children).

class Node:
    def __init__(self,value):
        self.left = None
        self.right = None
        self.data = value

def Leaf_count(root):
    if(root.left == None and root.right == None):
        return 1
    