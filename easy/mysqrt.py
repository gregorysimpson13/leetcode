# 69. Sqrt(x) - EASY
# https://leetcode.com/problems/sqrtx/


# Implement int sqrt(int x).

# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

# Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

# Example 1:

# Input: 4
# Output: 2
# Example 2:

# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since 
#              the decimal part is truncated, 2 is returned.


def mySqrt(x: int) -> int:
    if x == 1: return 1
    low, high = 1, x // 2
    while low <= high:
        mid = (low + high) // 2
        if x == mid ** 2:
            return mid
        elif mid ** 2 < x:
            low = mid + 1
        else: 
            high = mid - 1
    return (low + high) // 2


for i in range(1, 11):
    print("i: {}, i --> {}, i**2 --> {}".format(i, mySqrt(i), mySqrt(i**2)))