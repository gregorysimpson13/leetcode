# Runtime: O(nlogn); beats 98.1%
# Space: O(1); beats 72.1%

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations: return 0
        citations.sort(reverse=True)
        h_index = 0
        for i, val in enumerate(citations):
            h_index = max(h_index, min(i+1, val))
        return h_index