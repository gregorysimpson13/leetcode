class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        table = defaultdict(int)
        l = r = max_len = 0
        while r < len(s):
            char_count = table[s[r]] = table[s[r]] + 1
            if char_count == 1: max_len = max(max_len, r-l+1)
            while table[s[r]] > 1:
                table[s[l]], l = table[s[l]] - 1, l + 1
            r = r + 1
        return max_len