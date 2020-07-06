# 994. Rotting Oranges
# https://leetcode.com/problems/rotting-oranges/


# In a given grid, each cell can have one of three values:

# the value 0 representing an empty cell;
# the value 1 representing a fresh orange;
# the value 2 representing a rotten orange.
# Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.

# Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.

 

# Example 1:



# Input: [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:

# Input: [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
# Example 3:

# Input: [[0,2]]
# Output: 0
# Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
 

# Note:

# 1 <= grid.length <= 10
# 1 <= grid[0].length <= 10
# grid[i][j] is only 0, 1, or 2.


class Coordinate:
    def __init__(self, row, col):
        self.r = row
        self.c = col

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = []
        ones_set = set()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((Coordinate(row, col), 0))
                if grid[row][col] == 1:
                    ones_set.add((row, col))
        max_minutes = 0    
        while queue:
            coord, minute = queue.pop(0)
            max_minutes = max(max_minutes, minute)
            if (coord.r + 1, coord.c) in ones_set:
                queue.append((Coordinate(coord.r + 1, coord.c), minute + 1))
                ones_set.remove((coord.r + 1, coord.c))
            if (coord.r - 1, coord.c) in ones_set:
                queue.append((Coordinate(coord.r - 1, coord.c), minute + 1))
                ones_set.remove((coord.r - 1, coord.c))
            if (coord.r, coord.c + 1) in ones_set:
                queue.append((Coordinate(coord.r, coord.c + 1), minute + 1))
                ones_set.remove((coord.r, coord.c + 1))
            if (coord.r, coord.c - 1) in ones_set:
                queue.append((Coordinate(coord.r, coord.c - 1), minute + 1))
                ones_set.remove((coord.r, coord.c - 1))
        return max_minutes if not ones_set else -1
