class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Linkedlist:
    def middleNode(self, head):
        slow = head
        fast = head

        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next

        return slow


# Create nodes
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)
n4 = Node(40)
n5 = Node(50)

# Connect nodes
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5

ll = Linkedlist()
mid = ll.middleNode(n1)

print("Middle Node:", mid.data)

