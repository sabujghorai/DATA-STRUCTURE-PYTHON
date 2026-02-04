class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

a = Node(10)
b = Node(20)
c = Node(30)
d = Node(40)

head = a
a.next = b
b.next = c
c.next = d

print(head.data)
print(head.next.data)
print(head.next.next.data)
# print(head.next.next.next.data)