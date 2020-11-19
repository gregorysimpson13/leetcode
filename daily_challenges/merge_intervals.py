# Runtime: O(n); 44.33%
# Space: O(1)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ret = []
        for start, fin in sorted(intervals):
            if not ret: ret.append([start, fin])
            prev_start, prev_fin = ret[-1]
            if prev_start <= start <= prev_fin: ret[-1][1] = max(ret[-1][1], fin)
            else: ret.append([start, fin])
        return ret
