# 168. Excel Sheet Column Title
# https://leetcode.com/problems/excel-sheet-column-title/


# Given a positive integer, return its corresponding column title as appear in an Excel sheet.

# For example:

#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB 
#     ...
# Example 1:

# Input: 1
# Output: "A"
# Example 2:

# Input: 28
# Output: "AB"
# Example 3:

# Input: 701
# Output: "ZY"


from string import ascii_uppercase
def convertToTitle(n: int) -> str:
    result_string = ""
    while n > 0:
        mod = n%26
        result_string = ascii_uppercase[mod-1] + result_string
        if mod - 1 == -1: n = n - 1
        n = n // 26
    return result_string



print(convertToTitle(1), "A")
print(convertToTitle(26), "Z")
print(convertToTitle(27), "AA")
print(convertToTitle(28), "AB")
print(convertToTitle(52), "AZ")
print(convertToTitle(53), "BA")
print(convertToTitle(0), "")
print(convertToTitle(701), "ZY")
print(convertToTitle(11701), "QHA")