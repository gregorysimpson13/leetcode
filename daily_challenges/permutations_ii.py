class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
        def permute(arr=[], idx=set()):
            if len(arr) == len(nums): res.add(tuple(arr)); return
            for i in range(len(nums)):
                if i in idx: continue
                idx.add(i); arr.append(nums[i])
                permute(arr, idx)
                idx.remove(i); arr.pop()
        permute()
        return res
