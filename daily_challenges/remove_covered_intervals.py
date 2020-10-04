from bisect import insort_left, bisect_right
from typing import List
# Runtime: O(logn); beats 98.55
# Space: O(n); beats 26.99
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        arr = []
        for a, b in sorted(intervals, key=lambda x: x[1]-x[0], reverse=True):
            if not arr: insort_left(arr, (a,b)); continue
            i = bisect_right(arr, (a,b))
            if i > 0 and arr[i-1][0] <= a and b <= arr[i-1][1]: continue
            if i < len(arr) and arr[i][0] <= a and b <= arr[i][1]: continue
            insort_left(arr, (a,b))
        return len(arr)