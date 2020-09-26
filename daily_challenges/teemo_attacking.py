# Runtime: O(n); beats 100%
# Space: O(1)

from typing import List
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        right = res = 0
        for time in timeSeries:
            new_right = time + duration
            res += new_right - max(right, time)
            right = new_right
        return res