#
# @lc app=leetcode id=1470 lang=python3
#
# [1470] Shuffle the Array
#

# @lc code=start
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for x, y in zip(nums[:n], nums[n:]):
            result.append(x); result.append(y)
        return result
# @lc code=end

