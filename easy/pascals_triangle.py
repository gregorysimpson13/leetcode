# 118. Pascal's Triangle - EASY
# https://leetcode.com/problems/pascals-triangle/

# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


# In Pascal's triangle, each number is the sum of the two numbers directly above it.

# Example:

# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

def generate(numRows: int):
        result = []
        for row in range(numRows):
            triangle = []
            for col in range(row+1):
                prev_row = row - 1
                left, right = col - 1, col
                if prev_row < 0:
                    triangle.append(1)
                elif left < 0 or right >= len(result[prev_row]):
                    triangle.append(1)
                else:
                    triangle.append(result[prev_row][left] + result[prev_row][right])
            result.append(triangle)
        return result



print(generate(5))