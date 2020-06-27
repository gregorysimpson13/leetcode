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
    squares = [i**2 for i in range((n//2)+2)]
    sums = [float('inf') for i in range(n+1)]
    sums[0] = 0
    for square in squares:
            if square > n:
                    break
            for i in range(len(sums)):
                    backtrack = sums[i-square] + 1 if i-square >= 0 else float('inf')
                    sums[i] = min(sums[i],backtrack)
    return sums[-1]




print(numSquares(0),0)
print(numSquares(1),1)
print(numSquares(12),3)
print(numSquares(13),2)
print(numSquares(8441),3)
