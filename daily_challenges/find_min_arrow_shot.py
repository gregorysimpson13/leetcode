# Runtime: O(n log n); beats 94.8%
# Space: O(n)
from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        right, count = None, 0
        for a, b in sorted(points, key=lambda x: x[1]):
            if right == None: right = b; count += 1
            elif right < a: right = b; count += 1
        return count