# def binary_search(arr, low, high, elem):
#     while low <= high:
#         mid = low + (high - low) // 2
#         if arr[mid] == elem:
#             return mid
#         elif arr[mid] < elem:
#             low = mid + 1
#         else:
#             high = mid - 1
#     return None

# arr = [12, 24, 34, 110, 145, 240, 79]
# # elem = int(input("elem: "))
# elem = 6
# result = binary_search(arr, 0, len(arr) - 1, elem)
# if result == None:
#     print("element not found");
# else:
#     print(f"element found at index {result}")


#
#
#
#
#
#
#
#
def binary_search(arr, low, high, element):
    while low <= high:
        mid = low + (high-low) // 2
        if arr[mid] == element:
            return mid
        elif arr[mid] < element:
            low = mid + 1
        else:
            high = mid - 1

arr = [45,6,7,85,44,35,9,97, 105]
arr = sorted(arr)
print(arr)
element = 85
low = 0
high = len(arr) - 1
result = binary_search(arr, low, high, element)
print(result)