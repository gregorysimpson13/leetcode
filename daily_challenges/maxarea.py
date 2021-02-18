# Runtime: O(n); beats 47.36%
# Space: O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        marea = 0
        l, r = 0, len(height) - 1
        while l <= r:
            marea = max(marea, min(height[l], height[r]) * (r-l))
            if height[l] < height[r]: l+=1
            else: r-=1
        return marea
            