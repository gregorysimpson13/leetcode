# 463. Island Perimeter - EASY

# https://leetcode.com/problems/island-perimeter/
# You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water.

# Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).

# The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

 

# Example:

# Input:
# [[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]

# Output: 16

# Explanation: The perimeter is the 16 yellow stripes in the image below:

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]: return 0
        perimeters = 0
        queue = []
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    queue.append((row,col))
                    break
        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]
        seen_set = set()
        while queue:
            row, col = queue.pop(0)
            if (row, col) in seen_set: continue
            seen_set.add((row, col))
            for i in range(4):
                nr = row + dr[i]
                nc = col + dc[i]
                if nr >= 0 and nr < len(grid) and nc >= 0 and nc < len(grid[0]) and grid[nr][nc] == 1:           
                    queue.append((nr,nc))
                else:
                    perimeters = perimeters + 1
        return perimeters



# input1 = [[0,1,0,0],
#  [1,1,1,0],
#  [0,1,0,0],
#  [1,1,0,0]]
# print(islandPerimeter(input1))
# input2 = [[1,1,1,1],
#  [1,1,1,1],
#  [1,1,1,1],
#  [1,1,1,1]]
# print(islandPerimeter(input2))
# input3 = [[0,0,0,0],
#  [0,0,0,0],
#  [0,0,0,0],
#  [0,0,0,0]]
# print(islandPerimeter(input3))
# input4 = [[0,0,0,0],
#  [0,0,0,0],
#  [0,1,0,0],
#  [0,0,0,0]]
# print(islandPerimeter(input4))
# input5 = [[0,0,0,0],
#  [0,0,0,0],
#  [0,1,1,0],
#  [0,0,0,0]]
# print(islandPerimeter(input5))
input6 = [[1,0]]
print(islandPerimeter(input6))