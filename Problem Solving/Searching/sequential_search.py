




def sequential_search(arr, element):
    for i in range(len(arr)):
        if arr[i] == element:
            return i
    return None


arr = [3,4,2,5,6,8]
element = 6

result = sequential_search(arr, element)
if result == None:
    print("Element not found in array")
else:
    print(f"Element found in array at index {result}")