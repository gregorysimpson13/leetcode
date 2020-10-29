# Runtime: O(n); beats 72.64%
# Space: O(1)
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        prev_fill, distance = -1, 0
        for i, fill in enumerate(seats):
            if fill and prev_fill == -1: distance = prev_fill = i
            elif fill: distance, prev_fill = max((i - prev_fill)//2, distance), i
        return max((len(seats) - 1 - prev_fill), distance)
