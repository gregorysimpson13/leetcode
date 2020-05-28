# 520. Detect Capital - EASY
# https://leetcode.com/problems/detect-capital/


# Given a word, you need to judge whether the usage of capitals in it is right or not.

# We define the usage of capitals in a word to be right when one of the following cases holds:

# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital, like "Google".
# Otherwise, we define that this word doesn't use capitals in a right way.
 

# Example 1:

# Input: "USA"
# Output: True
 

# Example 2:

# Input: "FlaG"
# Output: False
 

# Note: The input will be a non-empty word consisting of uppercase and lowercase latin letters.


def detectCapitalUse(word: str) -> bool:
    for i in range(1, len(word)):
        left, right = word[i-1], word[i]
        if left.islower() and right.isupper() or (i > 1 and left.isupper() and right.islower()):
            return False
    return True


print(detectCapitalUse('USA'), True)
print(detectCapitalUse("FlaG"), False)
print(detectCapitalUse("leetcode"), True)
print(detectCapitalUse("FFFFFFFFFg"), False)