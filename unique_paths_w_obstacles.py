# 63. Unique Paths II
# https://leetcode.com/problems/unique-paths-ii/submissions/

# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# Now consider if some obstacles are added to the grids. How many unique paths would there be?

# An obstacle and empty space is marked as 1 and 0 respectively in the grid.

# Note: m and n will be at most 100.

# Example 1:

# Input:
# [
#   [0,0,0],
#   [0,1,0],
#   [0,0,0]
# ]
# Output: 2
# Explanation:
# There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right

def uniquePathsWithObstacles(obstacleGrid) -> int:
    rows, cols = len(obstacleGrid), len(obstacleGrid[0])
    cache = {(rows-1, cols-1): 1}
    def paths(row, col):
        if row >= rows or col >= cols or obstacleGrid[row][col] == 1:
            return 0
        if (row, col) in cache:
            return cache[(row, col)]
        cache[(row,col)] = paths(row + 1, col) + paths(row, col + 1)
        return cache[(row,col)]
    return paths(0,0)




input = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
print(uniquePathsWithObstacles(input), 2)