# 76. Minimum Window Substring
# https://leetcode.com/problems/minimum-window-substring/

# Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

# Example:

# Input: S = "ADOBECODEBANC", T = "ABC"
# Output: "BANC"
# Note:

# If there is no such window in S that covers all characters in T, return the empty string "".
# If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l, r = 0, 0
        min_l, min_r = None, None
        letters_needed = len(t)
        letters_map = defaultdict(int)
        for letter in t:
            letters_map[letter] -= 1
        while r < len(s):
            if s[r] in letters_map:
                letters_map[s[r]] += 1
                if letters_map[s[r]] <= 0: letters_needed -= 1
            while letters_needed == 0:
                if (min_l == None and min_r == None) or ((r - l) < (min_r - min_l)):
                    min_l, min_r = l, r
                removed = s[l]
                l = l + 1
                if removed in letters_map:
                    letters_map[removed] -= 1
                    if letters_map[removed] < 0: letters_needed += 1
            r = r + 1
        return s[min_l:min_r+1] if min_l != None and min_r != None else ""
                
                
print(Solution().minWindow("ADOBECODEBANC", "ABC"))
print(Solution().minWindow("a", "aa"))