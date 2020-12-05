# Runtime: O(n); beats 25.30%
# Space: O(1)
class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        for i in range(1,n+1):
            if k == 1 and n % i == 0: return i
            if n % i == 0: k = k - 1
        return -1