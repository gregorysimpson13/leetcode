# Runtime: O(n)
# Space: O(1)
class Solution:
    def romanToInt(self, s: str) -> int:
        look = {'I':1,'IV':4,'V':5,'IX':9,'X':10,'XL':40,'L':50,'XC':90,'C':100,'CD':400,'D':500,'CM':900,'M':1000}
        ans = i = 0
        while i < len(s):
            if i+2 <= len(s) and s[i:i+2] in look: ans+=look[s[i:i+2]]; i += 2
            else: ans+=look[s[i]]; i += 1
        return ans
