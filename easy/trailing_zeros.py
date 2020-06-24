# 172. Factorial Trailing Zeroes
# https://leetcode.com/problems/factorial-trailing-zeroes/

# Given an integer n, return the number of trailing zeroes in n!.

# Example 1:

# Input: 3
# Output: 0
# Explanation: 3! = 6, no trailing zero.
# Example 2:

# Input: 5
# Output: 1
# Explanation: 5! = 120, one trailing zero.
# Note: Your solution should be in logarithmic time complexity.

def trailingZerosNaive(n: int) -> int:
    result = 1
    while n > 1:
        result *= n
        n = n - 1
    zeros = 0
    while result % 10 == 0:
        zeros = zeros + 1
        result = result // 10
    return zeros

def trailingZeros(n: int) -> int:
    count = 0
    while n >= 5:
        count = count + (n // 5)
        n = n // 5
    return count

# print(trailingZeros(8))
# print(trailingZeros(31))


for i in range(5,100,5):
    print(i, trailingZerosNaive(i), trailingZeros(i))