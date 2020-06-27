# Perfect Squares
# 6/27/2020

# Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

# Example 1:

# Input: n = 12
# Output: 3 
# Explanation: 12 = 4 + 4 + 4.
# Example 2:

# Input: n = 13
# Output: 2
# Explanation: 13 = 4 + 9.



'''
        sum -> 0 1 2 3 4 5 6
squares
|              0  0  0  0  0  0  0
v              0  1  1  2  3  4  5
               -4 -3 -2 -1 0  1  2



'''


def numSquares(n: int) -> int:
    squares = [i**2 for i in range((n//2)+1)]