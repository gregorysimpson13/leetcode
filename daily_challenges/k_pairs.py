# Runtime: O(nlogn); beats 98.8%
# Space: O(n)
from typing import List
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        pairs, seen = set(), set()
        for n in sorted(nums):
            if (n-k) in seen: pairs.add((n-k, n))
            seen.add(n)
        return len(pairs)