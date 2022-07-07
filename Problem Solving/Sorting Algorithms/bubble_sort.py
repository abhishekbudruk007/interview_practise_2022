


def bubble_sort(my_list):
    # new_arr = []
    # while my_list:
    #     minimum = my_list[0]
    #     for x in my_list:
    #         if x < minimum:
    #             minimum  = x
    #         new_arr.append(minimum)
    #         my_list.remove(minimum)
    # print(new_arr)

    # new_list = []
    # while my_list:
    #     min = my_list[0]
    #     for x in my_list:
    #          if x < min:
    #             min = x
    #     new_list.append(min)
    #     my_list.remove(min)
    # print(new_list)

    # for i in range(len(my_list)):
    #     for j in range(i + 1 , len(my_list)):
    #         if my_list[j] < my_list[i]:
    #             temp = my_list[i]
    #             my_list[i] = my_list[j]
    #             my_list[j] = temp
    # print(my_list)


    for i in range(len(my_list)):
        for j in range(i + 1 , len(my_list)):
            if my_list[j] < my_list[i]:
                my_list[i], my_list[j] = my_list[j], my_list[i]
    print(my_list)







lst = [8,2,6,4,5]


print(bubble_sort(lst))