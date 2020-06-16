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
# start1 = time.time()
# print(longestPalindrome("babaddtattarrattatddetartrateedredividerb"))
# end1 = time.time()
# print(end1 - start1)

# start1 = time.time()
# print(longestPalindromeNew("babaddtattarrattatddetartrateedredividerb"))
# end1 = time.time()
# print(end1 - start1)


def longestPalindrome(s: str) -> str:
    cache = {}

    def palindrome(start=0, end=len(s)-1) -> str:
        if (start, end) in cache:
            return cache[(start, end)]
        if start == end:
            cache[(start, end)] = s[start]
            return s[start]
        if start > end:
            cache[(start, end)] = ""
            return ""
        if s[start] == s[end]:
            val = s[start] + palindrome(start+1, end-1) + s[end]
            cache[(start, end)] = val
            return val
        inc_start = palindrome(start+1, end)
        dec_end = palindrome(start, end-1)
        cache[(start, end)] = inc_start if len(
            inc_start) > len(dec_end) else dec_end
        return cache[(start, end)]
    return palindrome()


def longestPalindrome(s: str) -> str:
    if s[::-1] == s: return s
    leftMax, rightMax = 0, 0
    for i in range(1, len(s)):
        left, right = i, i
        if s[i-1] == s[i]:
            left = i - 1
            if i+1 < len(s) and s[i+1] == s[i-1]:
                right = i + 1
        while left >= 0 and right < len(s):
            if s[left] == s[right]:
                if (rightMax - leftMax) < (right - left):
                    leftMax = left
                    rightMax = right
            if s[left] != s[right]: 
                break
            left = left - 1
            right = right + 1
    return s[leftMax:rightMax+1]
            
        


print("\n\nNEW")
print(longestPalindrome("babad"), "bab")
print(longestPalindrome("bb"), "bb")
print(longestPalindrome("ccd"), "cc")
print(longestPalindrome("dcc"), "cc")
print(longestPalindrome("babaddtattarrattatddetartrateedredividerb"))
print(longestPalindrome("aaabaaaa"), "aaabaaa")
print(longestPalindrome("aaabbaaaa"), "aaabbaaa")
print(longestPalindrome("azwdzwmwcqzgcobeeiphemqbjtxzwkhiqpbrprocbppbxrnsxnwgikiaqutwpftbiinlnpyqstkiqzbggcsdzzjbrkfmhgtnbujzszxsycmvipjtktpebaafycngqasbbhxaeawwmkjcziybxowkaibqnndcjbsoehtamhspnidjylyisiaewmypfyiqtwlmejkpzlieolfdjnxntonnzfgcqlcfpoxcwqctalwrgwhvqvtrpwemxhirpgizjffqgntsmvzldpjfijdncexbwtxnmbnoykxshkqbounzrewkpqjxocvaufnhunsmsazgibxedtopnccriwcfzeomsrrangufkjfzipkmwfbmkarnyyrgdsooosgqlkzvorrrsaveuoxjeajvbdpgxlcrtqomliphnlehgrzgwujogxteyulphhuhwyoyvcxqatfkboahfqhjgujcaapoyqtsdqfwnijlkknuralezqmcryvkankszmzpgqutojoyzsnyfwsyeqqzrlhzbc"), "sooos")
print(longestPalindrome("ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggggg") == "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff")