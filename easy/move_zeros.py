# 283. Move Zeros - EASY

# https: // leetcode.com/problems/move-zeroes/

# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Example:

# w
# i
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:

# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.


def moveZeroes(nums) -> None:
    i, wall = 1, 0
    for i in range(len(nums)):
        if nums[i] != 0 and nums[wall] == 0:
            nums[i], nums[wall] = nums[wall], nums[i]
        if nums[wall] != 0:
            wall = wall + 1
        i = i + 1


nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)

nums1 = [0, 0, 0, 1, 0, 3, 0, 12]
moveZeroes(nums1)
print(nums1)

nums2 = [1, 0, 1]
moveZeroes(nums2)
print(nums2)

nums3 = [0, 1]
moveZeroes(nums3)
print(nums3)
