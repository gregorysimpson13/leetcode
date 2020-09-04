from typing import List
from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        left, right, count = 0, 0, len(p)
        p_dict = Counter(p)
        result = []
        for right, char in enumerate(s):
            if char not in p_dict: count = len(p); p_dict = Counter(p); left = right + 1
            p_dict[char] -= 1
            if p_dict[char] >= 0:
                count -= 1
                if count == 0:
                    result.append(left)
                    p_dict[s[left]] += 1
                    left += 1
                    count += 1
            # handle contract
            while left < right and p_dict[char] < 0:
                p_dict[s[left]] += 1
                if p_dict[s[left]] > 0: count += 1
                left += 1
                if count == 0:
                    result.append(left)
        return result


print(Solution().findAnagrams("cbaebabacd", "abc"), [0,6])
print(Solution().findAnagrams("abab", "ab"), [0,1,2])
print(Solution().findAnagrams("abacbabc", "abc"), [1,2,3,5])
