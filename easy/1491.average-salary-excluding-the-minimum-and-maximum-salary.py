#
# @lc app=leetcode id=1491 lang=python3
#
# [1491] Average Salary Excluding the Minimum and Maximum Salary
#

# @lc code=start
class Solution:
    def average(self, salary: List[int]) -> float:
        if len(salary) <= 2: return 0.0
        min_number, max_number = float('inf'), float('-inf')
        for number in salary:
            if number < min_number: min_number = number
            if number > max_number: max_number = number
        return sum([number for number in salary if number != min_number and number != max_number]) / (len(salary) - 2)
# @lc code=end

