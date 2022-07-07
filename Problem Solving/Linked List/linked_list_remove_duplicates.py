
# class Node:
#     def __init__(self, val):
#         self.val = val
#         self.next = None
#
#
#     def traverse(self):
#         node = self
#         while node != None:
#             print(node.val)
#             node = node.next
#
#     def remove_duplicates(self):
#         els = []
#         node = self
#         # previous = None
#         while node != None:
#             if node.val not in els:
#                 els.append(node.val)
#                 node = node.next
#             else:
#                 # els.append(node.val)
#                 node = node.next
#             # previous = node
#             # node = node.next
#
# if __name__ == "__main__":
#     node1 = Node(1)
#     node2 = Node(2)
#     node3 = Node(3)
#     node4 = Node(1)
#     node1.next = node2
#     node2.next = node3
#     node3.next = node4
#
#     # node1.remove_duplicates()
#     node1.traverse()



class Node:
    def __init__(self,val):
        self.val = val
        self.next = None



class LinkedList:

    def __init__(self):
        self.head = None

    def insert_at_start(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_last(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        n = self.head
        while n.next != None:
            n = n.next
        n.next = new_node
        # n.next = new_node
        # self.head =



    def traverse(self):
        if self.head is None:
            print("List has no elements")
            return
        else:
            n = self.head
            while n != None:
                print(n.val, " ")
                n = n.next


    def search(self, x):
        if self.head is None:
            print("List is Empty")
            return
        n = self.head
        while n != None:
            if n.val == x:
                print("Item Found")
                return
            n = n.next
        print("Item not found")
        return False

    def delete_from_start(self):
        if self.head is None:
            print("List is Empty")
            return

        self.head = self.head.next

    def delete_from_end(self):
        if self.head is None:
            print("List is Empty")
            return
        n = self.head
        while n.next.next is not None:
            n = n.next
        n.next = None

ref_obj = LinkedList()
ref_obj.insert_at_start(10)
ref_obj.insert_at_start(20)
ref_obj.insert_at_last(30)
ref_obj.search(80)
ref_obj.delete_from_start()
ref_obj.delete_from_end()

ref_obj.traverse()