#
#
#
# # def cal(lst=[]):
# #     lst.append('PYTHON')
# #     return lst
# #
# #
# # print(cal())
# # print(cal())
#
#
# lst = ["C", "c++", "java", "python"]
#
# import pdb;pdb.set_trace()
# for idx, item in enumerate(lst):
#     lst.pop(idx)
#
# print(lst)
from functools import reduce

words = ["mary","had","a","little","lamb"]

# result = (reduce(lambda x,y: x if len(x) > len(y) else y, words))
result = (reduce(lambda x,y: x if len(x) > len(y) else y, words))
print(result)