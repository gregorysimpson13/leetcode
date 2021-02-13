# Runtime: O(n); beats 89.91%
# Space: O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)