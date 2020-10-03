# beats 51.49%
from typing import List
from copy import deepcopy
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def combination(i=0,curr=0,arr=[]):
            if curr == target: res.append(deepcopy(arr)); return
            if curr > target: return
            for j in range(i,len(candidates)):
                arr.append(candidates[j])
                combination(j, curr+candidates[j], arr)
                arr.pop()
        combination()
        return res
