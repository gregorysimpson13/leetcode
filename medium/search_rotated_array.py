# 33. Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/

# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

# You are given a target value to search. If found in the array return its index, otherwise return -1.

# You may assume no duplicate exists in the array.

# Your algorithm's runtime complexity must be in the order of O(log n).

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        while left <= right:
            # print("left - right: ", left, right)
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[left] > nums[right] and (target < nums[left] or target > nums[right]):
                if nums[left] > target:
                    left = left + 1
                else:
                    right = right - 1
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = left + 1
        return -1


print(Solution().search([4,5,6,7,0,1,2], 0), 4)
print(Solution().search([4,5,6,7,0,1,2], 3), -1)
print(Solution().search([3,5,1], 3), 0)
print(Solution().search([4,5,6,7,8,1,2,3], 8), 4)