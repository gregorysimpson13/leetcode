# Runtime: O(n); 7.44% <-- Lol
# Space: O(n)
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        curr = 0
        min_index = float('inf')
        lookup = defaultdict(lambda: float('inf'))
        for i, n in enumerate(nums):
            curr = curr + n
            lookup[curr] = min(lookup[curr], i)
            if x - curr == 0: min_index = min(min_index, i)
        curr = 0
        for i, n in enumerate(nums[::-1]):
            if x - curr in lookup and lookup[x-curr] < len(nums)-i: min_index = min(min_index, i + lookup[x - curr])
            curr = curr + n
            if x - curr == 0: min_index = min(min_index, i) 
        return min_index + 1 if min_index != float('inf') else -1