# 367. Valid Perfect Square - EASY
# https://leetcode.com/problems/valid-perfect-square/

# Given a positive integer num, write a function which returns True if num is a perfect square else False.

# Follow up: Do not use any built-in library function such as sqrt.

 

# Example 1:

# Input: num = 16
# Output: true
# Example 2:

# Input: num = 14
# Output: false

def validPerfectSquare(num: int) -> bool:
    if num == 1: return True
    low, high = 1, num//2
    while low <= high:
        mid = (low + high) // 2
        result = mid ** 2
        if result == num:
            return True
        elif result < num:
            low = mid + 1
        else:
            high = mid - 1
    return False



for i in range(1,11):
    print(i, validPerfectSquare(i))
    print(i**2, validPerfectSquare(i**2))