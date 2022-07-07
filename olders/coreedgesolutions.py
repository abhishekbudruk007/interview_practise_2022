# # a = {(): []}
# # b = {[]: 3}
# # c = {set(): ()}
# # d = {[]: ()}
# # e = {(): se()}
#
# dict = {"()":"[]", "[]":"3", "set()":"()", "[]":"()", "()":"set()"}
# # dict = {'{():[]}', '{[]:3}', '{set():()}', '{[]:()}', '{():set()}'}
# # enumerate_object = enumerate(dict)
# # print (list(enumerate_object))
# for key, val in dict.items():
#     try:
#         print("key: {}, value {} is possible".format(key, val))
#     except Exception as e:
#         print("key: {}, value {} is not possible".format(key, val))
#         pass
#
# # key: (), value [] is possible
# # key: [], value 3 is not possible

#
l = [(1, 3), (3, 5), (5, 7), (4, 8), ("A", "B")]
# "a:b->4:8->5:7->3:5->1:3"
import datetime
import time
start_date = time.time()
result = "->".join(list(map(lambda x: x[0], [[str(item[i]).lower()+":"+str(item[i+1]).lower() for i in range(len(item)-1)] for item in l[::-1]])))
time.sleep(10)
end_date = time.time()

result_date = end_date-start_date
print(result_date)
print(result)

# resulting_list=[]
# for item in l[::-1]:
#     for i in range(len(item)-1):
#         st = "{}:{}".format(item[i], item[i+1])
#         resulting_list.append(st)
# print(resulting_list)
# print("->".join(resulting_list))




# 10.004438400268555
