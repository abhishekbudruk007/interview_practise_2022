# final_result = []
# def flatten_list(ele):
#     if type(ele) == int:
#         final_result.append(ele)
#     else:
#         for item in ele:
#             flatten_list(item)
#
# lst = [1, 2, [3,4], [5, [6, 7]]]
#
# # print(flatten_list(lst))
# # #
# # result = []
# # for ele in lst:
# #     result.append(flatten_list(lst))
# # print(result)
# flatten_list(lst)
# print(final_result)
# # result_list = [ item if type(item) == int else [i for i in item] for item in lst]
# # print(result_list)



# bat --> tab
# # bab --> abb
# # Input: strs = ["eat","tea","tan","ate","nat","bat"]
# # Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# cat [ 99, 97, 116] =
# bbt [ 98, 98, 116] =
#
# def anagram(lst):
#     dict = {}
#     for  in lst:
#         if item not in dict.values():
#             dict[item] = list
#     print(dict)
#
lst = ["eat","tea","tan","ate","nat","bat"]
# lst = [sorted(item) for item in lst]
# print(anagram(lst))
# # print(lst)


def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    final_list = []
    hash_map = {}
    for s in strs:
        x = list(s)
        x.sort()
        x = ''.join(x)
        if x in hash_map:
            hash_map[x].append(s)
        else:
            hash_map[x] = [s]
    for i in hash_map:
        final_list.append(hash_map[i])
    return final_list

print(groupAnagrams(lst))

