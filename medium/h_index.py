class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations: return 0
        h_index = 0
        for i, val in enumerate(citations):
            new_h = min(val, len(citations)-i)
            h_index = max(h_index, new_h)
        return h_index