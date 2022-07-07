
# class Node:
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#
#     def insert(self, value):
#         if value <= self.value:
#             if self.left == None:
#                 self.left = Node(value)
#             else:
#                 self.left.insert(value)
#         else:
#             if self.right == None:
#                 self.right = Node(value)
#             else:
#                 self.right.insert(value)
#
#     def find(self, value):
#         if value == self.value:
#             return True
#         elif value < self.value:
#             if self.left == None:
#                 return False
#             else:
#                 return self.left.find(value)
#         else:
#             if self.right == None:
#                 return False
#             else:
#                 return self.right.find(value)
#
#     def printInOrder(self):
#         if self.left != None:
#             self.left.printInOrder()
#         print(self.value)
#         if self.right != None:
#             self.right.printInOrder()
#
#
#
# obj = Node(10)
# obj.insert(34)
# obj.insert(89)
# obj.insert(43)
# # obj.find(34)
# obj.printInOrder()









class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val):
        if val <= self.val:
            if self.left == None:
                self.left = Node(val)
            else:
                self.left.insert(val)
        else:
            if self.right == None:
                self.right = Node(val)
            else:
                self.right.insert(val)


    def find(self, val):
        if val == self.val:
            return True
        elif val <= self.val:
            if self.left == None:
                return False
            else:
                self.left.find(val)
        else:
            if self.right == None:
                return False
            else:
                self.right.find(val)


    def printInOrder(self):
        if self.left != None:
            self.left.printInOrder()
        print(self.val, end=" ")
        if self.right != None:
            self.right.printInOrder()


    def printPreOrder(self):
        print(self.val, end=" ")
        if self.left != None:
            self.left.printPreOrder()
        if self.right != None:
            self.right.printPreOrder()

root = Node(10)
root.insert(5)
root.insert(20)
root.insert(3)
root.insert(9)
root.insert(15)
root.insert(25)
root.insert(1)
root.insert(4)
root.insert(13)
root.insert(17)
root.insert(30)

root.printInOrder()

print("\n\n")
root.printPreOrder()
