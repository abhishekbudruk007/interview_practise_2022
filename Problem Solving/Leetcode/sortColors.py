# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
#
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
#
# You must solve this problem without using the library's sort function.

# Example 1:
#
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:
#
# Input: nums = [2,0,1]
# Output: [0,1,2]

def sortColors(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    start = 0
    end = len(nums) - 1
    i = 0 #starting index
    while i <= end:
        if nums[i] == 2:
            nums[i] = nums[end]
            nums[end] = 2
            end -= 1
        elif nums[i] == 1:
            i += 1
        else:
            nums[i] = nums[start]
            nums[start] = 0
            start += 1
            i += 1
    return nums


nums = [2,0,2,1,1,0]
print(sortColors(nums))