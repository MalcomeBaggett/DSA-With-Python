# Write a function, five_sort, that takes in a list of numbers as an argument.
# The function should rearrange elements of the list such that all 5s appear at the end.
# Your function should perform this operation in-place by mutating the original list. The function should return the list.

# Elements that are not 5 can appear in any order in the output, as long as all 5s are at the end of the list.


def five_sort(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        if nums[right] == 5:
            right -= 1
        elif nums[left] == 5:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        else:
            left += 1
    return nums
