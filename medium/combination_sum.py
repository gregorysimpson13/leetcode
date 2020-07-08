# 39. Combination Sum
# https://leetcode.com/problems/combination-sum/

# Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

# The same repeated number may be chosen from candidates unlimited number of times.

# Note:

# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:

# Input: candidates = [2,3,6,7], target = 7,
# A solution set is:
# [
#   [7],
#   [2,2,3]
# ]
# Example 2:

# Input: candidates = [2,3,5], target = 8,
# A solution set is:
# [
#   [2,2,2,2],
#   [2,3,3],
#   [3,5]
# ]


'''
rows cols -> target ->
 |
 v
 candidates
'''


from collections import defaultdict
from copy import deepcopy
class Solution:
    def combinationSum(self, candidates, target):
        dp = defaultdict(list)
        for num in candidates:
            for summation in range(num, target+1):
                if len(dp[summation-num]) > 0:
                    for lst in dp[summation-num]:
                        dp[summation].append(deepcopy(lst+[num]))
                elif summation % num == 0:
                    dp[summation].append([num] * (summation//num))
        return dp[target]




print(Solution().combinationSum([2,3,6,7], 7))
print(Solution().combinationSum([2,3,5], 8))
print(Solution().combinationSum([1,2], 4))