# 3rd largest element in an array with single iteration
#
#
# arr = [6,7,8,3,5,6,7]
# result = []
# for ele in arr:
#     pass


# class A:
#     def display(self):
#         print('This is class A ')
#
# class B(A):
#     # def display(self):
#     #     print('This is class B')
#     def display2(self):
#         print('This is class B 2')
# b = B()
# b.display()






# def sequence_square(n):
#     l = range(n)
#     for i in l:
#         yield i
#
#
# gen = sequence_square(5)
# while True:
#     try:
#         print(next(gen))
#     except StopIteration:
#         break



# import re

txt = "The rain in Spain the"
# x = re.search("^The.*Spain$", txt)
# print(x)
#
#
# x = re.findall("^The*$", txt)
# print(x)
#
#


# txt = "The rain in Spain"
# x = re.findall("ai", txt)
# print(x)



numbers = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100]
# result = list(filter(lambda x: x % 2 ==0, numbers))
# print(result)

from functools import reduce
result = reduce(lambda x,y : x+y , numbers)
print(result)