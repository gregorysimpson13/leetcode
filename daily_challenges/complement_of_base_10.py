# Runtime: O(n); beats 49.35
# Space: O(n)
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        return int("".join(["1" if b == '0' else "0" for b in bin(N)[2:]]),2)