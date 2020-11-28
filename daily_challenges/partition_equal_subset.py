class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        _sum = sum(nums)
        target = _sum // 2
        @lru_cache(None)
        def find_partition(curr=0, idx=0):
            if curr == target: return True
            if curr > target: return False
            for i in range(idx, len(nums)):
                if find_partition(curr+nums[i], i+1): return True
            return False
        return False if _sum % 2 != 0 else find_partition()
