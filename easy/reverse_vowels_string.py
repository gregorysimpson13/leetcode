# 345. Reverse Vowels or a String - EASY
# https: // leetcode.com/problems/reverse-vowels-of-a-string/

# Write a function that takes a string as input and reverse only the vowels of a string.

# Example 1:

# Input: "hello"
# Output: "holle"
# Example 2:

# Input: "leetcode"
# Output: "leotcede"
# Note:
# The vowels does not include the letter "y".


def reverseVowels(s: str) -> str:
    vowels = set(['a', 'e', 'i', 'o', 'u'])
    stack = []
    result = ''
    for letter in s:
        if letter.lower() in vowels:
            stack.append(letter)
    for letter in s:
        if letter.lower() in vowels:
            result += stack.pop()
        else:
            result += letter
    return result


print(reverseVowels("hello"))
print(reverseVowels("leetcode"))
print(reverseVowels("aA"))
