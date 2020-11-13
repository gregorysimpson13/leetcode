# Runtime: O(n logn); beats 12.94%
# Space: O(1)
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, 2
        while sum(math.ceil(n/right) for n in nums) > threshold:
            right = right ** 2
        while left <= right:
            divisor = (left + right) // 2
            curr_sum = sum(math.ceil(n/divisor) for n in nums)
            if curr_sum > threshold: left = divisor + 1
            if curr_sum <= threshold: right = divisor - 1
        return left
