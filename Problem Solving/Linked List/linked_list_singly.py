

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

    def traverse(self):
        node = self
        while node != None:
            print(node.val)
            node= node.next

node1 = Node(12)
node2 = Node(99)
node3 = Node(37)

node1.next = node2
node2.next = node3
# print(node2.val)
# print(node2.next)

print(node1.traverse())

#
# Output:
# 12
# 99
# 37
# None

print(node2.traverse())


# Output
# 99
# 37
# None


print(node3.traverse())


# Output
# 37
# None
