#
# dict = {}
# X = 2
# Y = 1
# def rateLimit(userid, timestamp):
#     if userid not in dict and "times" not in dict:
#         dict[userid] = 1
#         dict["times"] = timestamp
#     else:
#         dict[userid] += 1
#         dict["times"] = timestamp
#
#     if dict[userid] > X and dict["times"] == timestamp:
#         return  False
#     else:
arr = []
Y = 2

def rateLimit(userid, timestamp):
   window = timestamp + Y
   if len(arr) > 0:
       for i in range(len(arr)):
           if arr[i:i+window]:
               if count(arr, arr[i+window]) > Y :
                   return False
               else:
                   return True
   else:
       arr.append(userid)


print(rateLimit("cerner", 1))
print(rateLimit("cerner", 1))
print(rateLimit("cerner", 1))
print(rateLimit("cerner", 0))
print(rateLimit("cerner", 1))
print(rateLimit("cerner", 1))
print(rateLimit("cerner", 1))
print(rateLimit("cerner", 0))