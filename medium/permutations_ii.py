# 47. Permutations II
# https://leetcode.com/problems/permutations-ii/

# Given a collection of numbers that might contain duplicates, return all possible unique permutations.

# Example:

# Input: [1,1,2]
# Output:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]
from typing import List
from copy import deepcopy
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result_set = set()
        def permute(arr, seen):
            if len(arr) == len(nums):
                result_set.add(tuple(arr))
                return
            for i in range(len(nums)):
                if i in seen:
                    continue
                seen.add(i)
                permute(arr+[nums[i]], seen)
                seen.remove(i)
        permute([], set())
        return [list(res) for res in result_set]

print(Solution().permuteUnique([1,1,2]))