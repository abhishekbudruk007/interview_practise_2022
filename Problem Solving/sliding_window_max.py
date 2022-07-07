def sliding(window, k):
    if len(window) < k:
        return
    result_list = [ max(window[i:i+k]) for i in range(len(window)) if len(window[i:i+k])>=k]
    # result_list = []
    # for i in range(len(window)):
    #     if len(window[i:i+k]) >= k:
    #         result_list.append(window[i:i+k])
    return result_list


window = [1,2,3,1,4,5,2,3,6]
n = len(window)
k = 3
print(sliding(window, k))
# result_list= []
# import pdb;pdb.set_trace()
# for i in range(n-k+1):
#     temp_list = []
#     for j in range(i,k):
#         temp_list.append(window[j])
#     result_list.append(temp_list)
# print(result_list)




