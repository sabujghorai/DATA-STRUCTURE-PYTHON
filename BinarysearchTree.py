class Node :
    def __init__(self,value):
        self.left = None
        self.right = None
        self.data = value
        
def insert(root,value):
    if (root == None):
        return Node(value)
    if (root.data == None):
        return root
    if(root.data > value):
        root.left = insert(root.left,value)
    else:
        root.right = insert(root.right,value)
    return root

def searching(root,value):
    if (root == None):
        print("Element not found..", end = "\n")
        return
    if (root.data == value):
        print("Element found..",end = "\n")
        return
    if(root.data > value):
        searching(root.left,value)
    else:
        searching(root.right,value) 

def Inorder(root):
    if (root != None):
        Inorder(root.left)
        print(root.data, end = " ")
        Inorder(root.right)

root = insert(None,20)
root = insert(root,15)
root = insert(root,30)
root = insert(root,40)
root = insert(root,12)
root = insert(root,18)
root = insert(root,58)
Inorder(root) # this inorder function arrange the element in increasing order
# print("\n")
searching(root,15)
searching(root,33)