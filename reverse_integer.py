# EASY: Reverse Integer

# Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output: 321
# Example 2:

# Input: -123
# Output: -321
# Example 3:

# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


def reverse(x: int) -> int:
    sign = -1 if x < 0 else 1
    x = sign * x
    result = 0
    while x > 0:
        result += x % 10
        x = x // 10
        result = result * 10
    ans = int((result / 10) * sign)
    if ans > 2 ** 31 - 1:
        return 0
    if ans < -2 ** 31:
        return 0
    return ans


# print(reverse(-123))
print(reverse(123) == 321)
print(reverse(-123) == -321)
print(reverse(120) == 21)
