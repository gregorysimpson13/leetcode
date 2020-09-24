from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return [let for let, i in Counter(s+t).items() if i % 2 != 0][0]