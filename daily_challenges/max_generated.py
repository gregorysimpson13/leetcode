class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if not n: return 0
        nums = [1] * (n + 1)
        for i in range(2, n+1):
            nums[i] = nums[i//2] + nums[(i+1)//2] if i % 2 else nums[i//2]
        return max(nums)