# 1239. Maximum Length of a Concatenated String with Unique Characters
# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/


# Given an array of strings arr. String s is a concatenation of a sub-sequence of arr which have unique characters.

# Return the maximum possible length of s.


# Example 1:

# Input: arr = ["un","iq","ue"]
# Output: 4
# Explanation: All possible concatenations are "","un","iq","ue","uniq" and "ique".
# Maximum length is 4.
# Example 2:

# Input: arr = ["cha","r","act","ers"]
# Output: 6
# Explanation: Possible solutions are "chaers" and "acters".
# Example 3:

# Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
# Output: 26


# Constraints:

# 1 <= arr.length <= 16
# 1 <= arr[i].length <= 26
# arr[i] contains only lower case English letters.

def maxLength(arr) -> int:
    max_len = len(arr[0])
    next_max_len = 0
    for i in range(1, len(arr)):
        if len(arr[i]) >= max_len:
            next_max_len = max_len
            max_len = len(arr[i])
        elif len(arr[i]) > next_max_len:
            next_max_len = len(arr[i])
    return max_len + next_max_len


def maxLengthGood(arr) -> int:
    max_len = 0
    arr.sort(key=lambda x: len(x), reverse=True)

    def addLetters(i, strSet=set()):
        for char in arr[i]:
            if char in strSet:
                return
            strSet.add(char)
        nonlocal max_len
        if max_len < len(strSet):
            max_len = len(strSet)
        if i >= len(arr):
            return
        for index in range(i+1, len(arr)):
            addLetters(index, strSet)
    addLetters(0, set())
    arr.sort(key=lambda x: len(x))
    addLetters(0, set())
    return max_len


def maxLengthDP(arr) -> int:
    max_len = 0


print(maxLength(["un", "iq", "ue"]), 4)
print(maxLength(["cha", "r", "act", "ers"]), 6)
print(maxLength(["abcdefghijklmnopqrstuvwxyz"]), 26)
print(maxLength(["abcdefghijklmnopqrstuvwxyz", "ab"]), 28)
print(maxLength([["a", "b", "c", "d", "e", "f", "g", "h",
                  "i", "j", "k", "l", "m", "n", "o", "p"], "ab"]), 16)


print("\n\nNew Way")
print(maxLengthGood(["un", "iq", "ue"]), 4)
print(maxLengthGood(["cha", "r", "act", "ers"]), 6)
print(maxLengthGood(["abcdefghijklmnopqrstuvwxyz"]), 26)
print(maxLengthGood(["abcdefghijklmnopqrstuvwxyz", "ab"]), 26)
print(maxLengthGood(["cha", "r", "act", "ers"]), 6)
print(maxLengthGood(["yy", "bkhwmpbiisbldzknpm"]), 0)
print(maxLengthGood(["ab", "cd", "cde", "cdef", "efg", "fgh", "abxyz"]), 11)
print(maxLengthGood([["a", "b", "c", "d", "e", "f", "g", "h",
                      "i", "j", "k", "l", "m", "n", "o", "p"], "ab"]), 16)


print("\n\nNewest Way")

print(maxLengthGood(["un", "iq", "ue"]), 4)
print(maxLengthGood(["cha", "r", "act", "ers"]), 6)
print(maxLengthGood(["abcdefghijklmnopqrstuvwxyz"]), 26)
print(maxLengthGood(["abcdefghijklmnopqrstuvwxyz", "ab"]), 26)
print(maxLengthGood(["cha", "r", "act", "ers"]), 6)
print(maxLengthGood(["yy", "bkhwmpbiisbldzknpm"]), 0)
print(maxLengthGood(["ab", "cd", "cde", "cdef", "efg", "fgh", "abxyz"]), 11)
print(maxLengthGood([["a", "b", "c", "d", "e", "f", "g", "h",
                      "i", "j", "k", "l", "m", "n", "o", "p"], "ab"]), 16)


'''
ans = 11
["ab", "cd", "cde", "cdef", "efg", "fgh", "abxyz"]
  0     1                    2
'''
