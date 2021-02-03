# Runtime: O(1)
class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum(i=='1' for i in bin(n)[2:])