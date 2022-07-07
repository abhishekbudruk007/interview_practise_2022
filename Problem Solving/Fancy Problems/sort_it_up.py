#This problem is named as sort it up or dush  national flag  problem or sort colors

# Problem Statement
# Interview question for Microsoft , EDB , FB Apple , Amazon , Oracle


# You are given array arr, consisting of only zeroes , ones and twos .
# Sort the array in place and return it . Do not create a new array



# Input
# n - the size of array
# arr - the array itself

# Output

# A sorted Array


# Constraints
# 1 <= n <=100
# 0 <= arr[i] <=2

# Sample Input
# 5
# 2 0 1 0 2

#Sample Output
# 0 0 1 2 2


def sort_it_up(n, arr):
    # import pdb;pdb.set_trace()
    left_bound = 0
    right_bound = n - 1
    i = 0
    while i < right_bound:
        if arr[i] == '2':
            arr[i] = arr[right_bound]
            arr[right_bound] = '2'
            right_bound -= 1
        elif arr[i] == '1':
            i += 1
        else:
            arr[i] = arr[left_bound]
            arr[left_bound] = '0'
            left_bound += 1
            i += 1
    return arr



# n = 9
# arr = "1 2 0 2 1 2 2 0 2".split(" ")
n = 5
arr = "2 0 1 0 2".split(" ")
result = sort_it_up(n , arr)
print(result)


