# Runtime: O(n); beats 86.29%
# Space: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        stack, paren = [], set(['(', '[', '{'])
        for ch in s:
            if ch in paren: stack.append(ch)
            elif not stack or abs(ord(ch) - ord(stack.pop())) > 2: return False
        return not stack