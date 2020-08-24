# Runtime: O(nlogn); beats 17%
# Space: O(1); beats 11%


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        intervals.sort()
        overlaps = 0
        prev_ival = intervals[0]
        for curr_ival in intervals[1:]:
            if prev_ival[0] <= curr_ival[0] and prev_ival[1] > curr_ival[0]:
                overlaps = overlaps + 1
                prev_ival[1] = min(prev_ival[1], curr_ival[1])
            else:
                prev_ival = curr_ival
        return overlaps
                