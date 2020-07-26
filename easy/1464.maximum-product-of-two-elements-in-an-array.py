#
# @lc app=leetcode id=1464 lang=python3
#
# [1464] Maximum Product of Two Elements in an Array
#

# @lc code=start
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first_max, second_max = float('-inf'), float('-inf')
        for num in nums:
            if num > first_max:
                second_max, first_max = first_max, num
            elif num > second_max:
                second_max = num
        return (first_max - 1) * (second_max - 1)
# @lc code=end

