#Runtime: beats 72%
#Space: beats 62%
​
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        i = len(s) // 2
        while i >= 1:
            for j in range(i, len(s), i):
                if s[0:i] != s[j:i+j]: break
            else: return True
            i = i - 1
            while i > 0 and len(s) % i != 0: i = i - 1
        return False