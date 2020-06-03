# 344. Reverse String - EASY
# https: // leetcode.com/problems/reverse-string/

# Write a function that reverses a string. The input string is given as an array of characters char[].

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# You may assume all the characters consist of printable ascii characters.


# Example 1:

# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]

def reverseString(s) -> None:
    l, r = 0, len(s) - 1
    while l < r:
        s[l], s[r] = s[r], s[l]
        l = l + 1
        r = r - 1


input1 = ["h", "e", "l", "l", "o"]
reverseString(input1)
print(input1)

input2 = ["H", "a", "n", "n", "a", "h"]
reverseString(input2)
print(input2)

input3 = ["h"]
reverseString(input3)
print(input3)
