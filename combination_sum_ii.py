
# https://leetcode.com/problems/combination-sum-ii/

# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

# Each number in candidates may only be used once in the combination.

# Note:

# All numbers (including target) will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:

# Input: candidates = [10,1,2,7,6,1,5], target = 8,
# A solution set is:
# [
#   [1, 7],
#   [1, 2, 5],
#   [2, 6],
#   [1, 1, 6]
# ]
# Example 2:

# Input: candidates = [2,5,2,1,2], target = 5,
# A solution set is:
# [
#   [1,2,2],
#   [5]
# ]
from copy import deepcopy

def combinationSum2(candidates, target):
    candidates.sort()
    result = []
    def combinations(lst, sum, index):
        if sum > target:
            return
        if sum == target:
            nonlocal result            
            result.append(deepcopy(lst))
            #print("printing the list that i am appending to {}\nprinting the result {}".format(lst, result))
            return
        visited = set()
        for i in range(index, len(candidates)):
            item = candidates[i]
            if item in visited: continue
            lst.append(item)
            combinations(lst, sum + item, i + 1)
            lst.pop()
            visited.add(item)    
    combinations([], 0, 0)
    return result


# print(combinationSum2([10,1,2,7,6,1,5], 8))
for item in combinationSum2([10,1,2,7,6,1,5], 8):
    print(item)

