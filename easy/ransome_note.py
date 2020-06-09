# 383. Ransom Note - EASY
# https://leetcode.com/problems/ransom-note/

# Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines
# otherwise, it will return false.

# Each letter in the magazine string can only be used once in your ransom note.


# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true


# Constraints:

# You may assume that both strings contain only lowercase letters.


from collections import defaultdict


def canConstruct(ransomNote: str, magazine: str) -> bool:
    magazine_dict = defaultdict(int)
    for letter in magazine:
        magazine_dict[letter] = magazine_dict[letter] + 1
    for letter in ransomNote:
        magazine_dict[letter] = magazine_dict[letter] - 1
        if magazine_dict[letter] < 0:
            return False
    return True
