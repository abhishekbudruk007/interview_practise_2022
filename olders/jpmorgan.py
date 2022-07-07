#
# # Food.objects.filter(category='Snacks')
# dict1 = {'abhishek':1, 'bhaskar':2 , 'charan':3 }
# list1 = ['A', 'B', 'C']
# zipped_object = list(zip(list1, dict1.values()))
# result = dict(zipped_object)
# print(result)



list1 = ['A', 'B', 'C']


# class Queue:
#     que = []
#     def insert(self, element):
#         if element not in self.que:
#             self.que.append(element)
#
#     def delete(self):
#         self.que.pop(0)
#
#     def display(self):
#         print(self.que)
#
#
# object = Queue()
# object.insert(10)
# object.insert(20)
# object.insert(30)
# object.display()
# object.delete()
# object.delete()
# object.display()


# def iterate_list(arr, batch=100):
#     start_pos = 0
#     end_pos = batch
#     n = len(arr)
#
#     while end_pos <= n:
#         for i in range(start_pos, end_pos):
#             print(i)
#         start_pos = end_pos
#         end_pos = end_pos + batch
#
#
#
# list1 = range()
# batch = 100
#
# result = iterate_list(list1, batch)
# print(result)

#
# arr = range(50)
# batch = 10
# result = [[arr[j] for j in range(batch)] for i in range(0, len(arr), ) ]
# print(result)