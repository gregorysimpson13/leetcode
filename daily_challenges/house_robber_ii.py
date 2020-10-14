# Runtime: O(n); 69.07%
# Space: O(1)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1: return nums[0]
        def rob_houses(start: int, end: int) -> int:
            max_amount, prev_max = 0, 0
            for i in range(start,end):
                prev_max, max_amount = max_amount, max(max_amount, prev_max + nums[i])
            return max_amount
        return max(rob_houses(0, len(nums) - 1), rob_houses(1, len(nums)))