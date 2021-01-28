# Runtime: O(n); 35.62%
# Space: O(n)
class Solution:
    def concatenatedBinary(self, n: int) -> int:
        mod = 10**9 + 7
        arr = [str(bin(i)[2:]) for i in range(1,n+1)]
        return int("".join(arr), 2) % mod