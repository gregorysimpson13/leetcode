# Runtime: O(n^2)
# Space: O(n)
class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        keys = []
        lookup = {}
        for n in nums:
            i = bisect_left(keys, n)
            if i == 0 and n not in lookup: lookup[n] = []; insort_left(keys, n)
            else:
                for j in keys[:i]:
                    if not lookup[j]: lookup[j].append(n)
                    elif lookup[j] > n: return True
                    lookup[j] = n
        return False
