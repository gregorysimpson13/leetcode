# 62. Unique Paths: MEDIUM
# https://leetcode.com/problems/unique-paths/


# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

# The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

# How many possible unique paths are there?

# Example 1:

# Input: m = 3, n = 2
# Output: 3
# Explanation:
# From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
# 1. Right -> Right -> Down
# 2. Right -> Down -> Right
# 3. Down -> Right -> Right
# Example 2:

# Input: m = 7, n = 3
# Output: 28
 

# Constraints:

# 1 <= m, n <= 100
# It's guaranteed that the answer will be less than or equal to 2 * 10 ^ 9.



# DP Solution works

def uniquePaths(m,n):
    result = 0
    def paths(row, col, visited=set()):
        if row > m or col > n:
            return
        if (row, col) in visited:
            return
        if row == m and n == col:
            nonlocal result
            result += 1
            return
        visited.add((row, col))
        paths(row+1, col, visited)
        paths(row, col+1, visited)
        visited.remove((row,col))
    paths(1, 1)
    return result

def uniquePaths1(m,n):
    result = 0
    row, col = 1, 1
    queue = [(row, col)]
    visited = set()
    while queue != []:
        row, col = queue.pop(0)
        if row > m or col > n or (row,col) in visited:
            continue
        if row == m or col == n:
            result += 1
            continue
        visited.add((row,col))
        queue.append((row + 1, col))
        queue.append((row, col + 1))
        visited.remove((row,col))
    return result

def uniquePathsDP(m,n):
    cache = {(m,n): 1}
    def paths(row, col):
        if row > m or col > n:
            return 0
        if (row, col) in cache:
            return cache[(row, col)]
        if row == m and n == col:
            return cache[(row, col)] + 1
        result = 0
        result += paths(row+1, col)
        result += paths(row, col+1)
        cache[(row, col)] = result
        return result
    paths(1,1)
    return cache[1,1]





print(uniquePathsDP(3, 2), 3)
print(uniquePathsDP(7, 3), 28)