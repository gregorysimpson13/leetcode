# Runtime: O(n); beats 94.49%
# Space: O(1)
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        count = k
        for n in nums:
            if n and count < k: return False
            elif n: count = 0
            else: count = count + 1
        return True
        