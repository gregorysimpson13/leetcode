# 34. Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

# Your algorithm's runtime complexity must be in the order of O(log n).

# If the target is not found in the array, return [-1, -1].

# Example 1:

# Input: nums = [5, 7, 7, 8, 8, 10], target = 8
# Output: [3, 4]
# Example 2:

# Input: nums = [5, 7, 7, 8, 8, 10], target = 6
# Output: [-1, -1]


def searchRange(nums, target):
    if not nums: return [-1, -1]
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (right+left)//2
        if nums[mid] == target:
            l_mid, r_mid = mid, mid
            while l_mid > 0 and (nums[l_mid - 1] == target): l_mid = l_mid - 1
            while r_mid < len(nums) - 1 and (nums[r_mid + 1] == target): r_mid = r_mid + 1
            return [l_mid, r_mid]
        if nums[mid] > target:
            right = mid - 1
        if nums[mid] < target:
            left = mid + 1
    return [-1, -1]


inputs = [[5, 7, 7, 8, 8, 10], [5, 7, 7, 8, 8, 10],
          [5, 7, 7, 8, 8], [1], [5], [3, 3, 3, 3], [1, 4], [2,2]]
targets = [8, 6, 8, 1, 0, 3, 4, 3]
outputs = [[3, 4], [-1, -1], [3, 4], [0, 0], [-1, -1], [0, 3], [1, 1], [-1, -1]]

for i in range(len(inputs)):
    result = searchRange(inputs[i], targets[i])
    print(result, outputs[i])
