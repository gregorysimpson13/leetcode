# 50. Pow(x, n)
# https://leetcode.com/problems/powx-n/


# Implement pow(x, n), which calculates x raised to the power n (xn).

# Example 1:

# Input: 2.00000, 10
# Output: 1024.00000
# Example 2:

# Input: 2.10000, 3
# Output: 9.26100
# Example 3:

# Input: 2.00000, -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25
# Note:

# -100.0 < x < 100.0
# n is a 32-bit signed integer, within the range [−231, 231 − 1]



def myPow(x: float, n: int) -> float:
    if n == 0:
        return 1.0
    if n < 0:
        x = 1/x
        n = n * -1
    return x * myPow(x, n-1)

def myPow1(x: float, n: int) -> float:
    if n == 0:
        return 1.0
    if n < 0:
        x = 1/x
        n = n * -1
    result = x
    n = n - 1
    while n > 0:
        result = result * x
    return result



print(myPow(2.0, 10), 1024.0)
print(myPow(2.10, 3), 9.26)
print(myPow(2.0, -2), 0.25)
#print(myPow(1.00001, 123456), 0.25)

print(myPow1(2.0, 10), 1024.0)
print(myPow1(2.10, 3), 9.26)
print(myPow1(2.0, -2), 0.25)
print(myPow1(1.00001, 123456), 0.25)