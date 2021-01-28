# Runtime: O(n); beats 24.59%
# Space: O(n)
from string import ascii_lowercase as letters
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        arr = []
        for i in range(n-1,-1,-1):
            let = min(26, k-i)
            k = k - let
            arr.append(letters[let-1])
        return "".join(reversed(arr))