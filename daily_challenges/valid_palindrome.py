# Runtime O(n), beats 85%
# Space O(1), beats 54%



class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        s = s.lower()
        while left < right:
            while left < right and not s[left].isalnum(): left = left + 1
            while left < right and not s[right].isalnum(): right = right - 1
            if s[left] != s[right]: return False
            left, right = left + 1, right - 1
        return True