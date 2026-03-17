class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.data = value


def insert(root, value):
    if root is None:
        return Node(value)

    if root.data > value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)

    return root


def searching(root, value):
    if root is None:
        print("Element not found..")
        return

    if root.data == value:
        print("Element found..")
        return

    if root.data > value:
        searching(root.left, value)
    else:
        searching(root.right, value)


def get_successor(root):
    root = root.right
    while root and root.left:
        root = root.left
    return root


def delete(root, value):
    if root is None:
        return root

    if root.data > value:
        root.left = delete(root.left, value)
    elif root.data < value:
        root.right = delete(root.right, value)
    else:
        # Node found
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        # Node with 2 children
        succ = get_successor(root)
        root.data = succ.data
        root.right = delete(root.right, succ.data)

    return root


def Inorder(root):
    if root:
        Inorder(root.left)
        print(root.data, end=" ")
        Inorder(root.right)


# Driver Code
root = insert(None, 20)
root = insert(root, 15)
root = insert(root, 30)
root = insert(root, 40)
root = insert(root, 12)
root = insert(root, 18)
root = insert(root, 58)

print("Original Tree:")
Inorder(root)
print("\n")
root = delete(root, 12)
Inorder(root)
print("\n")
root = delete(root, 40)
Inorder(root)