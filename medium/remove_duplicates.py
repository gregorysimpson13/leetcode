# 80. Remove Duplicates from Sorted Array II
# https: // leetcode.com/problems/remove-duplicates-from-sorted-array-ii/

# Given a sorted array nums, remove the duplicates in-place such that duplicates appeared at most twice and return the new length.

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# Example 1:

# Given nums = [1, 1, 1, 2, 2, 3],

# Your function should return length = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.

# It doesn't matter what you leave beyond the returned length.
# Example 2:

#    last=0
#                     j
#                  i
# Given nums = [0, 0, 1, 1, 1, 1, 2, 3, 3],
[0, 1, 0]

# Your function should return length = 7, with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.

# It doesn't matter what values are set beyond the returned length.
# Clarification:

# Confused why the returned value is an integer but your answer is an array?

# Note that the input array is passed in by reference, which means modification to the input array will be known to the caller as well.


def removeDuplicates(nums) -> int:
    left, wall = 0, len(nums) - 1
    last = float('inf')
    count = 0
    appeared = 1
    while left <= wall:
        if last != nums[left]:
            last = nums[left]
            left = left + 1
            count = count + 1
            appeared = 1
            continue
        elif last == nums[left] and appeared < 2:
            count = count + 1
            appeared = appeared + 1
            left = left + 1
            continue
        idx = left
        while idx < wall:
            nums[idx], nums[idx+1] = nums[idx+1], nums[idx]
            idx = idx + 1
        wall = wall - 1
    return count


inputs = [[1, 1, 1, 2, 2, 3], [0, 0, 1, 1, 1, 1, 2, 3, 3], [1, 2, 3],
          [1, 1, 2, 2, 2, 2, 3, 4, 5], [1, 1, 1, 1, 2, 2, 2, 2, 3], [1]]
for nums in inputs:
    result = removeDuplicates(nums)
    for i in range(result):
        print(nums[i], end='')
    print()
