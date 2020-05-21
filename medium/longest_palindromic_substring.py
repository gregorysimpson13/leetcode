# 5. Longest Palindromic Substring - MEDIUM
# https://leetcode.com/problems/longest-palindromic-substring/

# Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

# Example 1:

# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# Example 2:

# Input: "cbbd"
# Output: "bb"
import time

'''
substring - must be in sequence and 
                       cbbd
                    /       \
                bbd          cbb
              /    \        /    \
             bd      bb    bb     cb

                        bb

'''
def isPalindrome(left, right, s):
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True
def longestPalindrome(s: str):
    max_global = -1
    def recursePalindrome(left, right):
        nonlocal max_global
        if right - left < max_global:
            return ""
        if isPalindrome(left, right, s):
            max_global = right - left
            return s[left:right+1]
        left_string = recursePalindrome(left + 1, right)
        right_string = recursePalindrome(left, right - 1)
        return left_string if len(left_string) > len(right_string) else right_string
    return recursePalindrome(0, len(s) - 1)
def longestPalindromeNew(s: str):
    def recursePalindrome(left, right):
        if isPalindrome(left, right, s):
            return s[left:right+1]
        left_string = recursePalindrome(left + 1, right)
        right_string = recursePalindrome(left, right - 1)
        return left_string if len(left_string) > len(right_string) else right_string
    return recursePalindrome(0, len(s) - 1)



print(longestPalindrome("babad"), "bab")
print(longestPalindrome("cbbd"), "bb")
start1 = time.time()
print(longestPalindrome("babaddtattarrattatddetartrateedredividerb"))
end1 = time.time()
print(end1 - start1)

start1 = time.time()
print(longestPalindromeNew("babaddtattarrattatddetartrateedredividerb"))
end1 = time.time()
print(end1 - start1)