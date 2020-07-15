# https://leetcode.com/problems/4sum/submissions/
# [-3,-2,-1,0,0,1,2,3]
# 0

from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        results = set()
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                left, right = j + 1, len(nums) - 1
                print(left, right)
                while left < right:
                    four_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if four_sum == target:
                        results.add((nums[i], nums[j], nums[left], nums[right]))
                        left, right = left + 1, right - 1
                        while left < right and nums[left - 1] == nums[left]: left = left + 1
                        while right > left and nums[right + 1] == nums[right]: right = right - 1
                    if four_sum > target:
                        right = right - 1
                    if four_sum < target:
                        left = left + 1
        return [list(res) for res in results]

print(Solution().fourSum([-3,-2,-1,0,0,1,2,3],0))