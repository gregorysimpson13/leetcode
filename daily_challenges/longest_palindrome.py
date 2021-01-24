# Runtime: O(n); beats 30.06%
# Space: O(n)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        string = "-".join([ch for ch in s])
        ml = mr = j = 0
        for i in range(len(string)):
            l, r = i-1, i+1
            while l >= 0 and r < len(string) and string[l] == string[r]:
                if mr-ml-(string[j]!='-') < r-l-(string[i]!='-'): ml, mr, j = l, r, i
                l, r = l - 1, r + 1
        return string[ml:mr+1].replace("-","")