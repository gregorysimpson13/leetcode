# 171. Excel Sheet Column Number
# https://leetcode.com/problems/excel-sheet-column-number/
# Given a column title as appear in an Excel sheet, return its corresponding column number.

# For example:

#     A -> 1
#     B -> 2
#     C -> 3
#     ...
#     Z -> 26
#     AA -> 27
#     AB -> 28 
#     ...
# Example 1:

# Input: "A"
# Output: 1
# Example 2:

# Input: "AB"
# Output: 28
# Example 3:

# Input: "ZY"
# Output: 701

def titleToNumber(self, s: str) -> int:
    from string import ascii_uppercase
    letter_dict = {}
    for val, letter in enumerate(ascii_uppercase,1):
        letter_dict[letter] = val
    result = 0
    for i in range(len(s)):
        result = result + (letter_dict[s[i]] * (26**(len(s)-(i+1))))
    return result

