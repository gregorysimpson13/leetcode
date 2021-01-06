# Runtime: O(n); beats 84.04%
# Space: O(1)
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n, i = 1, 0
        while k:
            if i < len(arr) and arr[i] == n: i += 1
            else: k -= 1
            if k: n += 1
        return n