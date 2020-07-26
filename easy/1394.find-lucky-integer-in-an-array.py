#
# @lc app=leetcode id=1394 lang=python3
#
# [1394] Find Lucky Integer in an Array
#

# @lc code=start
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        for number, freq in sorted(Counter(arr).items(), reverse=True):
            if number == freq: return number
        return -1
# @lc code=end

