# 1143. Longest Common Subsequence
# https://leetcode.com/problems/longest-common-subsequence/

# Given two strings text1 and text2, return the length of their longest common subsequence.

# A subsequence of a string is a new string generated from the original string with some characters(can be none) deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). A common subsequence of two strings is a subsequence that is common to both strings.

 

# If there is no common subsequence, return 0.

 

# Example 1:

# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.
# Example 2:

# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
# Example 3:

# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
 

# Constraints:

# 1 <= text1.length <= 1000
# 1 <= text2.length <= 1000
# The input strings consist of lowercase English characters only.

'''
abcde
ace

a-c-e
ace
'''

from collections import defaultdict
        
class Solution1:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        max_length = 0
        def subsequence(idx_1, idx_2, length):
            if idx_1 >= len(text1) or idx_2 >= len(text2):
                nonlocal max_length
                max_length = max(max_length, length)
                return
            if text1[idx_1] == text2[idx_2]:
                subsequence(idx_1+1, idx_2+1, length+1)
            else:
                subsequence(idx_1+1, idx_2, length)
                subsequence(idx_1, idx_2+1, length)
        subsequence(0,0,0)
        return max_length

class Solution2:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if not text1 or not text2: return 0
        cache = {}
        def subsequence(idx_1, idx_2, length):
            if idx_1 >= len(text1) or idx_2 >= len(text2):
                return length
            key = (idx_1, idx_2)
            if idx_1 == len(text1) - 1 and idx_2 == len(text2) - 1:
                cache[key] = length
                return length
            if key in cache:
                return cache[key] + length
            if text1[idx_1] == text2[idx_2]:
                cache[key] = subsequence(idx_1+1, idx_2+1, length+1)
            else:
                val1 = subsequence(idx_1+1, idx_2, length)
                val2 = subsequence(idx_1, idx_2+1, length) 
                cache[key] = max(val1, val2)
            return cache[key]
        return subsequence(0,0,0)

class Solution3:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if text1 == text2: return len(text1)
        def subsequences(i_1, i_2, length):
            if i_1 >= len(text1) or i_2 >= len(text2):
                return 0
            if i_1 == len(text1) -1 and i_2 == len(text2):
                return length
            if text1[i_1] == text2[i_2]:
                return 1 + subsequences(i_1 + 1, i_2 + 1, length + 1)
            return max(subsequences(i_1 + 1, i_2, length), subsequences(i_1, i_2 + 1, length))
        return subsequences(0,0,0)

from collections import defaultdict
class Solution4:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        if text1 == text2: return len(text1)
        cache = defaultdict(int)
        def subsequences(i_1, i_2, length):
            if i_1 >= len(text1) or i_2 >= len(text2):
                return 0
            key = (i_1, i_2)
            if key in cache:
                return cache[key]
            if i_1 == len(text1) -1 and i_2 == len(text2):
                cache[key] = max(cache[key], length)
                return length
            if text1[i_1] == text2[i_2]:
                val = 1 + subsequences(i_1 + 1, i_2 + 1, length + 1)
                cache[key] = max(cache[key], val)
                return val
            val = max(subsequences(i_1 + 1, i_2, length), subsequences(i_1, i_2 + 1, length))
            cache[key] = max(cache[key], val)
            return val
        return subsequences(0,0,0)



# print(Solution().longestCommonSubsequence("abcde", "ace"), 3)
# print(Solution1().longestCommonSubsequence("abcde", "ace"), 3)
# print(Solution().longestCommonSubsequence("a", "ace"), 1)
# print(Solution1().longestCommonSubsequence("a", "ace"), 1)
# print(Solution().longestCommonSubsequence("bl", "yby"), 1)
# print(Solution1().longestCommonSubsequence("bl", "yby"), 1)


print(Solution4().longestCommonSubsequence("abcde", "ace"), 3)
print(Solution4().longestCommonSubsequence("a", "ace"), 1)
print(Solution4().longestCommonSubsequence("abc", "abc"), 3)
print(Solution4().longestCommonSubsequence("bl", "yby"), 1)
print(Solution4().longestCommonSubsequence("ezupkr", "ubmrapg"), 2)